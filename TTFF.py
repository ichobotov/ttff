import os
from datetime import datetime, time, timedelta
import re
import math
import numpy as np
import shutil
from split_to_trials import split_to_trials

# Constants to set
PATH = r'C:\python\ttff'
BOARD = 'ComNav'
FLAG = '(1|2|4|5|15)'
# FLAG = '10'
true_lat = 55.673688  # in dd.dddddd format
true_lon = 37.5051  # in dd.dddddd format
# POS_THRESHOLD = 0.1
POS_THRESHOLD = 10


file = BOARD+'_gga.log'
result_folder = BOARD+'_trials'
dir_with_files = os.path.join(PATH,result_folder)
result = BOARD+'_results.log'



def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
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
    delta_lon_m = math.cos(true_lat) * 111321.3778 * delta_lon
    delta_m = math.sqrt(delta_lat_m ** 2 + delta_lon_m ** 2)
    return delta_m


split_to_trials(result_folder, file, PATH)

trials = []

files_sorted = sorted(os.listdir(dir_with_files), key=lambda x: int(os.path.splitext(x)[0]))

for filename in files_sorted:

    with open(os.path.join(dir_with_files, filename), 'r') as f:
        start_stop = []
        switch_gga_search = False
        switch_time_search = False
        for line in f:
            if find_string(line, '-PWR ON-'):
                switch_time_search = True
                continue
            if find_string(line, '\[\d+\.\d{2}\]') and switch_time_search:
                print_time = re.match(r'.*\[(\d+\.\d{2})\]', line).group(1)
                print_time_sec = time_in_sec(print_time)

                if len(start_stop) == 0:
                    start_stop.append(print_time_sec)
                    switch_time_search = False
                    switch_gga_search = True
                    continue
                else:
                    start_stop.append(print_time_sec)
                    ttff = start_stop[1] - start_stop[0]

                    if ttff < 0:
                        ttff = ttff + 86400

                    trials.append(ttff)
                    start_stop = []
                    switch_time_search = False
                    break
            if find_string(line, f'.*\$G.GGA.*(?<=[E|W],){FLAG},') and switch_gga_search:
                lat = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),', line).group(1)
                lon = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),', line).group(2)

                if delta_ll(lat, lon) > POS_THRESHOLD:
                    continue
                switch_time_search = True
                switch_gga_search = False
                continue
        if len(start_stop) != 0:
            trials.append('fail')
success_trials = [x for x in trials if x != 'fail']

result_file = open(os.path.join(dir_with_files, result), 'w')


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
