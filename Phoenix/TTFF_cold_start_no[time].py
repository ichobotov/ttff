import os
from datetime import datetime, time, timedelta
import re
import math
import io
import time as t

import numpy as np
import shutil
from tqdm import tqdm

# Constants to set
PATH = r'C:\python\github\ttff\Phoenix'
BOARD = 'pho_reboot'
FLAG = '1'
EVENT = b'INI=COLDRESET'
# EVENT = b'INI=WARMRESET'
# EVENT = b'RST=REBOOT'
# FLAG = '(1|2|4|5|15)'
# FLAG = '10'

#MDC
# true_lat = 55.673784  # in dd.dddddd format
# true_lon = 37.505103 # in dd.dddddd format
#BARN
true_lat = 53.307364  # in dd.dddddd format
true_lon = 83.776109 # in dd.dddddd format
# POS_THRESHOLD = 0.1
POS_THRESHOLD = 10
DURATION = 601


# file = BOARD+'_gga.log'
file = '20241023_3.0.111.4753_114424.00.log1'
# file = 'train.txt'
# file = '1'
result_folder = BOARD+'_trials'
dir_with_files = os.path.join(PATH,result_folder)
result = BOARD+'_results.log'



# def find_string(line, reg_expr):
#     if re.findall(reg_expr, line):
#         return True


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
    switch_coldstart_search = True
    switch_pwroff_search = False
    write = False
    count = 0
    with open (FILE, 'rb') as f:
        for line in file_reader(f):
            if EVENT in line:
            # if b'INI=WARMRESET' in line:
            # if b'RST=REBOOT' in line:
                filename = str(i) + '.txt'
                trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                trial.write(line)
                write = True
                continue
            while not EVENT in line and write:
            # while not b'INI=WARMRESET' in line and write:
            # while not b'RST=REBOOT' in line and write:
                trial.write(line)
                try:
                    line = next(file_reader(f))
                except StopIteration:
                    print('break', trial)
                    break
            else:
                if EVENT in line:
                # if b'INI=WARMRESET' in line:
                # if b'RST=REBOOT' in line:
                    write = True
                    trial.close()
                    i += 1
                    filename = str(i) + '.txt'
                    trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                    trial.write(line)

# split_to_trials(result_folder, file, PATH)

trials = []


with open(file, 'rb') as f:
        # is_failed = False
        trial = 0
        success_trial = 0
        counter_good_pos = 0
        start_stop = []
        time_is_empty = False
        switch_gga_search = False
        switch_time_search = False
        for line in tqdm(f, desc='In process...',unit='' ):
            if (b'NAV,' in line or EVENT in line) and switch_gga_search == False:
            # if (b'NAV,' in line or b'RST=REBOOT' in line) and switch_gga_search == False:
            # if (b'NAV,' in line or b'INI=WARMRESET' in line) and switch_gga_search == False:
                if b'NAV,' in line:
                    # if find_string(line, f'\$NAV,\d+,\d+,\d+\.\d\d,\d+\.\d+,N,\d+\.\d+,E,'):
                    if find_string(line, f'\$NAV,\d+,\d+,\d+\.\d\d,'):
                        # time = re.match(f'.*\$NAV,\d+,\d+,(\d+\.\d\d),\d+\.\d+,N,\d+\.\d+,E,'.encode(), line).group(1)
                        time = re.match(f'.*\$NAV,\d+,\d+,(\d+\.\d\d),'.encode(), line).group(1)
                        nav_time = time_in_sec(time)
                if EVENT in line:
                    trial += 1
                    # if is_failed == True:
                    #     print(f'Trial:{trial}')
                    #     trials.append('fail')
                    #     print('!!! Fail !!!')

                # if b'RST=REBOOT' in line:
                # if b'INI=WARMRESET' in line:
                #     if nav_time != '':
                    start_stop.append(nav_time)
                    switch_gga_search = True
                    print('*'*20)
                    start_time = t.strftime('%H:%M:%S', t.gmtime(nav_time))
                    print(f'Trial {trial} start:{nav_time}; {start_time}')
                    # nav_time = ''
                continue
            if (b'NAV,' in line or EVENT in line) and switch_gga_search == True:
            # if switch_gga_search and b'NAV,' in line:
                # if find_string(line, f'.*\$G.GGA,\d*\.\d*,.*(?<=[E|W],){FLAG},'):
                if find_string(line, f'\$NAV,{FLAG},\d+,\d*\.\d\d,\d+\.\d+,N,\d+\.\d+,E,'):
                    # print(line)
                    # lat = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(1)
                    # lon = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(2)
                    time = re.match(r'.*\$NAV,\d+,\d+,(\d+\.\d\d),(\d+\.\d+),N,(\d+\.\d+),E,'.encode(), line).group(1)
                    lat = re.match(r'.*\$NAV,\d+,\d+,(\d+\.\d\d),(\d+\.\d+),N,(\d+\.\d+),E,'.encode(), line).group(2)
                    lon = re.match(r'.*\$NAV,\d+,\d+,(\d+\.\d\d),(\d+\.\d+),N,(\d+\.\d+),E,'.encode(), line).group(3)
                    nav_time = time_in_sec(time)
                    time_is_empty = False

                    if delta_ll(lat, lon) > POS_THRESHOLD:
                        print(f'delta {delta_ll(lat, lon)}; {time}')
                        counter_good_pos = 0
                        # if len(start_stop) == 2:
                        #     del start_stop[-1]
                        continue
                    print(counter_good_pos)
                    if counter_good_pos == 0:
                        expected_ttff = time_in_sec(time)
                        start_stop.append(expected_ttff)
                    # print(start_stop)
                    # if len(start_stop) == 2:
                    #     ttff = start_stop[1] - start_stop[0]
                    print(start_stop)
                    if start_stop[-1] - start_stop[0] < 3:
                        del start_stop[-1]
                        counter_good_pos = 0
                        # print(start_stop)
                        switch_time_search = False
                        switch_gga_search = True
                        continue

                    counter_good_pos += 1
                    if counter_good_pos < 10:
                        continue
                    # start_stop.append(expected_ttff)
                    ttff = start_stop[-1] - start_stop[0]

                    if ttff < 0:
                        ttff = ttff + 86400

                    trials.append(ttff)
                    stop_time = t.strftime('%H:%M:%S', t.gmtime(expected_ttff))
                    print(f'Trial {trial} stop:{expected_ttff}; {stop_time}')
                    success_trial = trial
                    # is_failed = False
                    start_stop = []
                    counter_good_pos = 0
                    # switch_time_search = False
                    switch_gga_search = False
                    continue
                if find_string(line, f'\$NAV,\d*,\d*,,'):
                    time_is_empty = True
                if find_string(line, f'\$NAV,\d*,\d*,\d*\.\d\d,.*?\*'):
                    time = re.match(r'.*\$NAV,\d*,\d*,(\d*\.\d\d),.*?\*'.encode(), line).group(1)
                    nav_time = time_in_sec(time)
                    time_is_empty = False

                if EVENT in line:
                    trial += 1
                    trials.append('fail')
                    print('\n!!! Fail !!!')
                    print(f'nav_time {nav_time}')
                    # nav_time = ''
                    start_stop = []
                    if time_is_empty:
                        print('Zero time')
                        nav_time = nav_time + DURATION * (trial - 1 - success_trial)
                    start_stop.append(nav_time)
                    # switch_gga_search = False
                    # is_failed = True
                    continue

            # if switch_gga_search and b'GGA' in line:
        # if len(start_stop) != 0:
        #     trials.append('fail')

# trials = list(np.array(trials)-3)
success_trials = [x for x in trials if x != 'fail']
# success_trials = [x for x in trials if x != 'fail' and x < 70]

result_file = open(os.path.join(dir_with_files, result), 'w')
print(success_trials)
print(trials)


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


print(f"""Total trials = {len(trials)}
Failed trials = {trials.count('fail')}
Average = {round(np.mean(success_trials), 2)}
Min = {min(success_trials)}
Max = {max(success_trials)}
P50 = {np.percentile(np.array(success_trials), 50)}
P90 = {np.percentile(np.array(success_trials), 90)}
Stdev = {round(np.std(np.array(success_trials)), 2)}
Trials = {trials}""")


### для проверки с предыдущей версией
old = [32.0, 33.0, 35.0, 42.0, 29.0, 28.0, 26.0, 26.0, 25.0, 24.0, 23.0, 22.0, 41.0, 40.0, 41.0, 38.0, 39.0, 40.0, 41.0, 40.0, 39.0, 38.0, 38.0, 36.0, 36.0, 34.0, 40.0, 32.0, 182.0, 33.0, 70.0, 29.0, 28.0, 38.0, 26.0, 25.0, 24.0, 29.0, 540.0, 583.0, 40.0, 20.0, 40.0, 39.0, 39.0, 42.0, 42.0, 39.0, 41.0, 37.0, 37.0, 94.0, 35.0, 31.0, 30.0, 29.0, 24.0, 24.0, 30.0, 22.0, 43.0, 41.0, 44.0, 43.0, 44.0, 42.0, 41.0, 41.0, 41.0, 36.0, 35.0, 34.0, 33.0, 263.0, 28.0, 27.0, 38.0, 255.0, 24.0, 45.0, 44.0, 47.0, 42.0, 45.0, 43.0, 43.0, 46.0, 44.0, 44.0, 43.0, 42.0, 41.0, 42.0, 39.0, 42.0, 37.0, 37.0, 35.0, 34.0, 33.0, 33.0, 31.0, 30.0, 275.0, 28.0, 27.0, 26.0, 26.0, 76.0, 43.0, 42.0, 41.0, 212.0, 39.0, 40.0, 40.0, 39.0, 41.0, 43.0, 40.0, 39.0, 38.0, 36.0]
# print(new[75])
res = list(zip(old, trials))
print(res)
for i in range(len(res)):
    if res[i][0] != res[i][1]:
        print(f'trial - {i+1}; old - {res[i][0]}; new - {res[i][1]}')