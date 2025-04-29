import os
from datetime import datetime, time, timedelta
import re
import math
import io

import numpy as np
import shutil
# from split_to_trials_ph import split_to_trials
from tqdm import tqdm

# Constants to set
PATH = r'C:\Users\ichobotov\Desktop\tests\restarts'
BOARD = 'pho'
FLAG = '(1|2|4|5|15)'
# FLAG = '10'
#MDC
true_lat = 55.673784  # in dd.dddddd format
true_lon = 37.505103 # in dd.dddddd format
#BARN
# true_lat = 53.307364  # in dd.dddddd format
# true_lon = 83.776109 # in dd.dddddd format
# POS_THRESHOLD = 0.1
POS_THRESHOLD = 10


# file = BOARD+'_gga.log'
file = 'phoenix.log1'
# file = '1'
result_folder = BOARD+'_trials'
dir_with_files = os.path.join(PATH,result_folder)
# dir_with_files = 'C:\\Users\\ichobotov\\Desktop\\tests\\restarts\\pho_cold_3.0.112_trials'
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

# def find_pwr_on_time(file:str) -> None:
#     switch_time_search = False
#     switch_pwr = False
#     pwr = None
#     with open(file, 'rb') as f:
#         for line in f:
#             if find_string(line, 'S,PWR,1,ON'):
#                 switch_time_search = True
#                 switch_pwr = True
#                 pwr = 'on'
#                 continue
#             if find_string(line, '\[--\d+\.\d{2}\--]') and switch_time_search:
#                 line=line.rstrip()
#                 line=line[1:-1]
#                 if pwr == 'on':
#                     pwr_on_time.append(line.rstrip().decode())
#                 if pwr == 'off':
#                     pwr_off_time.append(line.rstrip().decode())
#                 switch_time_search = False
#                 switch_pwr = True
#             if find_string(line, 'S,PWR,1,OFF') and switch_pwr:
#                 switch_time_search = True
#                 switch_pwr = False
#                 pwr = 'off'
#                 continue


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
            # if b'INI=COLDRESET' in line:
            if b'RST=REBOOT' in line:
                # count += 1
                # if count % 2 == 1:
                filename = str(i) + '.txt'
                trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                trial.write(line)
                # switch_coldstart_search = False
                write = True
                continue
                # else:
                #     continue
                # else:
                #     trial.close()
                #     del trial
                #     i += 1
                #     trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                #     trial.write(line)
                #     continue
            # while not b'INI=COLDRESET' in line and write:
            while not b'RST=REBOOT' in line and write:
                trial.write(line)
                try:
                    line = next(file_reader(f))
                except StopIteration:
                    print('break', trial)
                    break
            else:
                # if b'INI=COLDRESET' in line:
                if b'RST=REBOOT' in line:
                    write = True
                    trial.close()
                    # del trial
                    i += 1
                    # count += 1
                    filename = str(i) + '.txt'
                    trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                    trial.write(line)

            # try:
            #     # trial
            #     io.TextIOWrapper.__instancecheck__(trial)
            # except NameError:
            #     continue
            # trial.write(line)
            # trial.close()
            # del trial
            # switch_coldstart_search = True
            # switch_pwroff_search = False
            # i+=1
            # break
#
# pwr_on_time=[]
# pwr_off_time=[]

#
#
# find_pwr_on_time('poweroffon.log')
#
# if len(pwr_on_time) > len(pwr_off_time):
#     del pwr_on_time[-1]
# pwr_events = list(zip(pwr_on_time, pwr_off_time))
# # print(pwr_events)
split_to_trials(result_folder, file, PATH)

trials = []
# print(os.listdir(dir_with_files))
files_sorted = sorted(os.listdir(dir_with_files), key=lambda x: int(os.path.splitext(x)[0]))
# files_sorted = ['126.txt',]
for filename in tqdm(files_sorted, desc='Files'):

    with open(os.path.join(dir_with_files, filename), 'rb') as f:
        start_stop = []
        switch_gga_search = False
        switch_time_search = False
        for line in f:
            # if b'INI=COLDRESET' in line:
            if b'RST=REBOOT' in line:
                switch_time_search = True
                continue
            if switch_time_search and b'[--' in line:
                if find_string(line, '\[--\d+\.\d{2}\--]'):
                    print_time = re.match(r'.*\[--(\d+\.\d{2})\--]'.encode(), line).group(1).decode()
                    print_time_sec = time_in_sec(print_time)

                    if len(start_stop) == 0:
                        start_stop.append(print_time_sec)
                        print(print_time)
                        switch_time_search = False
                        switch_gga_search = True
                        continue
                    else:
                        start_stop.append(print_time_sec)
                        print(print_time)
                        print(start_stop)
                        ttff = start_stop[1] - start_stop[0]
                        print(ttff)
                        if ttff < 3:
                            del start_stop[-1]
                            # print(start_stop)
                            switch_time_search = False
                            switch_gga_search = True
                            continue

                        if ttff < 0:
                            ttff = ttff + 86400

                        trials.append(ttff)
                        start_stop = []
                        # switch_time_search = False
                        break
            # if switch_gga_search and b'GGA' in line:
            if switch_gga_search and b'NAV,' in line:

                # if find_string(line, f'.*\$G.GGA,\d*\.\d*,.*(?<=[E|W],){FLAG},'):
                if find_string(line, f'.*\$NAV,{FLAG},\d+,\d*\.\d\d,\d+\.\d+,N,\d+\.\d+,E,'):
                    # print(line)
                    # lat = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(1)
                    # lon = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(2)
                    lat = re.match(r'.*\$NAV,\d+,\d+,\d*\.\d{2},(\d+\.\d+),N,(\d+\.\d+),E,'.encode(), line).group(1)
                    lon = re.match(r'.*\$NAV,\d+,\d+,\d*\.\d{2},(\d+\.\d+),N,(\d+\.\d+),E,'.encode(), line).group(2)

                    if delta_ll(lat, lon) > POS_THRESHOLD:
                        continue
                    switch_time_search = True
                    switch_gga_search = False
                    continue
        if len(start_stop) != 0:
            trials.append('fail')
success_trials = [x for x in trials if x != 'fail']


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
