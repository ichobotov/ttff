import os
from datetime import timedelta
import re
import math
import numpy as np
import shutil
from tqdm import tqdm
import logging

# Constants to set
PATH = r'C:\Users\ichobotov\Desktop\tests\restarts'
BOARD = 'pho_barn_5'  ### cmnv for Comnav is required since used in the script (minus 1 sec)
FLAG = '1'
# EVENT = b'INI=COLDRESET'
# EVENT = b'INI=WARMRESET'
# EVENT = b'RST=REBOOT'
EVENT = 'GGA,(\d{6}.\d{2})?,,,,'
# FLAG = '(1|2|4|5|15)'
# FLAG = '10'
#MDC
# true_lat = 55.673784  # in dd.dddddd format
# true_lon = 37.505103 # in dd.dddddd format
#BARN
true_lat = 53.307362  # in dd.dddddd format
true_lon = 83.776103 # in dd.dddddd format
# POS_THRESHOLD = 0.1
POS_THRESHOLD = 5


# file = BOARD+'_gga.log'
# file = 'Phoenix_test.log'
file = 'Phoenix_test.log'
# file = '1'
result_folder = BOARD+'_trials'
dir_with_files = os.path.join(PATH,result_folder)
result = BOARD+'_results.log'


logging.basicConfig(level=logging.INFO, format='%(message)s')


def find_string(line, reg_expr):
    if re.search(reg_expr.encode(), line):
        return True

def time_in_sec(time_str):
    return timedelta(hours=int(time_str[0:2]), minutes=int(time_str[2:4]),
                     seconds=int(time_str[4:6])).total_seconds()


def delta_ll(lat, lon):
    """
    Computes delta in meters between current and true positions
    Theory of degrees to meters convertion:
    Сколько километров в градусе, минуте и секунде?
    Долгота. Тут все просто: длина окружности (меридиана) постоянна - 40 008,55 км, разделим на 360°, получим:
    111,134861111     км в одном градусе, делим на 60 минут:
    1,85224768519     км в одной минуте, делим на 60 секунд:
    0,0308707947531 км (30,8707947531 м) в одной секунде.

    Широта. Длина окружности различна - 40.075,696 км на экваторе, 0 на полюсах. Расчитывается как длина одного градуса на экваторе умноженного на косинус угла широты.
    Один градус на экваторе - 40 075,696 км / 360° = 111,321377778 км/° (111321,377778 м/°)

    На примере Казани:
    широта 55,79083°, cos(55,79083) = 0,56221574216 * 111321,377778 м/° = 62 586,631026062 м/°
    62,586631026062 км в одном градусе, делим на 60 минут:
    1,043110517 км в одной минуте, делим на 60 секунд:
    0,017385175 км (17,385175 м) в одной секунде.
    """
    lat_deg = int(lat[0:2]) + float(float(lat[2:]) / 60)
    lon_deg = int(lon[0:3]) + float(float(lon[3:]) / 60)
    delta_lat = true_lat - lat_deg
    delta_lon = true_lon - lon_deg
    delta_lat_m = delta_lat * 111134.8611
    delta_lon_m = math.cos(math.radians(true_lat)) * 111321.3778 * delta_lon
    delta_m = math.sqrt(delta_lat_m ** 2 + delta_lon_m ** 2)
    return delta_m


def file_reader(file):
    for line in file:
        yield line

def split_to_trials(RESULT_FOLDER, FILE, PATH):
    os.chdir(PATH)
    if os.path.exists(RESULT_FOLDER):
        shutil.rmtree(RESULT_FOLDER)
        os.mkdir(RESULT_FOLDER)
    else:
        os.mkdir(RESULT_FOLDER)

    i = 1
    write = False
    count = 0
    with open (FILE, 'rb') as f:
        for line in file_reader(f):
            if b'GGA,' in line and count == 0:
                if find_string(line,EVENT):
                    filename = str(i) + '.txt'
                    trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                    trial.write(line)
                    write = True
                    count += 1
                    continue
            while (find_string(line,EVENT) is None or 1 <= count < 60) and write:
                trial.write(line)
                if b'GGA' in line:
                    if find_string(line,EVENT):
                        count += 1
                if find_string(line, 'GGA,\d{6}.\d{2},\d+.\d+,N,\d+.\d+,E,') and count > 0:
                    count = 0
                try:
                    line = next(file_reader(f))
                except StopIteration:
                    logging.debug(f'break {trial}')
                    break
            else:
                if find_string(line,EVENT):
                    write = True
                    trial.close()
                    i += 1
                    filename = str(i) + '.txt'
                    trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                    trial.write(line)
                    count += 1
                else:
                    continue

# for line in tqdm(file_reader(f), desc='creating files, please wait...', bar_format="{desc} "):
tqdm(split_to_trials(result_folder, file, PATH), desc='creating files, please wait...', bar_format="{desc} ")

trials = []


with open(file, 'rb') as f:
        is_first = True
        trial = 0
        start_stop = []
        gga_time = None
        switch_gga_search = False
        switch_time_search = False
        for line in tqdm(f, desc='Computing statistics...',unit='' ):
            if b'GGA' in line:
                if find_string(line, f'.*\$G.GGA,(\d+.\d+),(\d+\.\d+),N,(\d+\.\d+),[E|W],{FLAG},'):
                    group = re.match(r'.*\$G.GGA,(\d{6}.\d{2}),(\d+\.\d+),.,(\d+\.\d+),'.encode(), line)
                    time_stamp = group.group(1)
                    lat = group.group(2)
                    lon = group.group(3)
                    if is_first is True:
                        is_first = False
                        gga_time = int(time_in_sec(time_stamp))
                        continue
                    diff = int(time_in_sec(time_stamp)) - gga_time
                    if diff < 0:
                        diff += 86400
                    if diff > 180:
                        if len(start_stop) == 0:
                            if 'cmnv' in BOARD:
                                start = gga_time + 179
                            else:
                                start = gga_time + 180
                            start_stop.append(start)
                        logging.debug(f'Start {start}')
                        if delta_ll(lat, lon) > POS_THRESHOLD:
                            continue
                        # switch_gga_search = False
                        start_stop.append(int(time_in_sec(time_stamp)))
                        logging.debug(f'Stop {int(time_in_sec(time_stamp))}')
                        if len(start_stop) == 2:
                            ttff = start_stop[1] - start_stop[0]
                            logging.debug(f'ttff {ttff}')
                            if ttff < 0:
                                ttff = ttff + 86400

                            trials.append(ttff)
                            start_stop = []
                            gga_time = int(time_in_sec(time_stamp))
                            continue

                        # switch_gga_search = True
                    else:
                        gga_time = int(time_in_sec(time_stamp))
                        continue

                else:
                    if find_string(line,EVENT):
                        continue
                    if find_string(line, f'.*\$G.GGA,(\d+.\d+),(\d+\.\d+),N,(\d+\.\d+),[E|W],{FLAG},'):
                        group = re.match(r'.*\$G.GGA,(\d{6}.\d{2}),(\d+\.\d+),.,(\d+\.\d+),'.encode(), line)
                        time_stamp = group.group(1)
                        lat = group.group(2)
                        lon = group.group(3)



# trials = list(np.array(trials)-3)
success_trials = [x for x in trials if x != 'fail']
# success_trials = [x for x in trials if x != 'fail' and x < 70]

result_file = open(os.path.join(dir_with_files, result), 'w')
logging.debug(success_trials)
logging.debug(trials)


result_file.write(
    f"""Total trials = {len(trials)}
Failed trials = {trials.count('fail')}
Average = {round(np.mean(success_trials), 2)}
Min = {min(success_trials)}
Max = {max(success_trials)}
P50 = {np.percentile(np.array(success_trials), 50)}
P90 = {np.percentile(np.array(success_trials), 90)}
Stdev = {round(np.std(np.array(success_trials)), 2)}
Trials = {trials}"""
)


logging.info(f"""Total trials = {len(trials)}
Failed trials = {trials.count('fail')}
Average = {round(np.mean(success_trials), 2)}
Min = {min(success_trials)}
Max = {max(success_trials)}
P50 = {np.percentile(np.array(success_trials), 50)}
P90 = {np.percentile(np.array(success_trials), 90)}
Stdev = {round(np.std(np.array(success_trials)), 2)}
Trials = {trials}""")


