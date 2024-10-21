import os
from datetime import datetime, time, timedelta
import re
import math
import io
import numpy as np
import shutil
from tqdm import tqdm
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S", format="%(asctime)s %(levelname)s %(message)s")

# Constants to set
PATH = r'C:\Users\ichobotov\Downloads\1'
BOARD = 'cmnv'
FLAG = '(1|2|4|5|15)'
# true_lat = 55.55555  # in dd.dddddd format
# true_lon = 37.33333 # in dd.dddddd format
true_lat = 55.673784  # in dd.dddddd format
true_lon = 37.505103 # in dd.dddddd format
POS_THRESHOLD = 10
file = 'knk_comnav.log'


result_folder = BOARD+'_trials'
dir_with_files = os.path.join(PATH,result_folder)
result = BOARD+'_results.log'


def find_string(line: bytes, reg_expr: str) -> bool:
    if re.search(reg_expr.encode(), line):
        return True

def time_in_sec(time_str: str) -> float:
    return timedelta(hours=int(time_str[0:2]), minutes=int(time_str[2:4]),
                     seconds=int(time_str[4:6])).total_seconds()


def delta_ll(lat: str, lon: str) -> float:
    lat_deg = int(lat[0:2]) + float(float(lat[2:]) / 60)
    lon_deg = int(lon[0:3]) + float(float(lon[3:]) / 60)
    delta_lat = true_lat - lat_deg
    delta_lon = true_lon - lon_deg
    delta_lat_m = delta_lat * 111134.8611
    delta_lon_m = math.cos(math.radians(true_lat)) * 111321.3778 * delta_lon
    delta_m = math.sqrt(delta_lat_m ** 2 + delta_lon_m ** 2)
    return delta_m

def find_pwr_on_time(file:str) -> Tuple[list,list]:
    pwr_on_time = []
    pwr_off_time = []
    switch_time_search = False
    switch_pwr = False
    pwr = None
    with open(file, 'rb') as f:
        for line in f:
            if find_string(line, 'S,PWR,1,ON'):
                switch_time_search = True
                switch_pwr = True
                pwr = 'on'
                continue
            if find_string(line, '\[--\d+\.\d{2}\--]') and switch_time_search:
                line=line.rstrip()
                line=line[1:-1]
                if pwr == 'on':
                    pwr_on_time.append(line.rstrip().decode())
                if pwr == 'off':
                    pwr_off_time.append(line.rstrip().decode())
                switch_time_search = False
                switch_pwr = True
            if find_string(line, 'S,PWR,1,OFF') and switch_pwr:
                switch_time_search = True
                switch_pwr = False
                pwr = 'off'
                continue
    return pwr_on_time, pwr_off_time

def file_reader(file: io.BytesIO) -> bytes:
    for line in file:
        yield line

def split_to_trials(RESULT_FOLDER: str, FILE: str, PATH: str , time_list: list) -> None :
    os.chdir(PATH)
    if os.path.exists(RESULT_FOLDER):
        shutil.rmtree(RESULT_FOLDER)
        os.mkdir(RESULT_FOLDER)
    else:
        os.mkdir(RESULT_FOLDER)

    i = 1
    switch_pwron_search = True
    switch_pwroff_search = False

    with open (FILE, 'rb') as f:
        for time in time_list:
            for line in tqdm(file_reader(f), desc='splitting...', bar_format="{desc} "):
                if find_string(line, time[0]) and switch_pwron_search:
                    filename = str(i) + '.txt'
                    trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'wb')
                    trial.write(line)
                    switch_pwron_search = False
                    switch_pwroff_search = True
                    continue
                while not find_string(line, time[1]) and switch_pwroff_search:
                    trial.write(line)
                    try:
                        line = next(file_reader(f))
                    except StopIteration:
                        break
                try:
                    io.TextIOWrapper.__instancecheck__(trial)
                except NameError:
                    continue
                trial.write(line)
                trial.close()
                del trial
                switch_pwron_search = True
                switch_pwroff_search = False
                i+=1
                break

#Get lists of PWR ON/OFF events
pwr_on_time, pwr_off_time = find_pwr_on_time('poweroffon.log')


if len(pwr_on_time) > len(pwr_off_time):
    del pwr_on_time[-1]

# Get list of events for each trial, e.g [(start1, end1), (start2, end2),...]
pwr_events = list(zip(pwr_on_time, pwr_off_time))
logging.info('%s trials to be analyzed', len(pwr_events))

split_to_trials(result_folder, file, PATH, pwr_events)
logging.info('%s files are created successfully', len(os.listdir(os.path.join(PATH, result_folder))))

# Future list of all the trials
trials = []

# List of files to be analyzed sorted by name index
files_sorted = sorted(os.listdir(dir_with_files), key=lambda x: int(os.path.splitext(x)[0]))

for filename in tqdm(files_sorted, desc='Files'):

    with open(os.path.join(dir_with_files, filename), 'rb') as f:
        start_stop = []
        switch_gga_search = False
        switch_time_search = True
        for line in f:
            if switch_time_search and b'[--' in line:
                if find_string(line, '\[--\d+\.\d{2}\--]'):
                    print_time = re.match(r'.*\[--(\d+\.\d{2})\--]'.encode(), line).group(1).decode()
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
                        break
            if  switch_gga_search and b'GGA' in line:
                if find_string(line, f'.*\$G.GGA,\d*\.\d*,.*(?<=[E|W],){FLAG},'):
                    lat = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(1)
                    lon = re.match(r'.*\$G.GGA,\d{6}.\d{2},(\d+\.\d+),.,(\d+\.\d+),'.encode(), line).group(2)

                    if delta_ll(lat, lon) > POS_THRESHOLD:
                        continue
                    switch_time_search = True
                    switch_gga_search = False
                    continue
        if len(start_stop) != 0:
            trials.append('fail')

# List of success trials
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


logging.info(f"""
Total trials = {len(trials)}
Failed trials = {trials.count('fail')}
Average = {round(np.mean(success_trials), 2)}
Min = {min(success_trials)}
Max = {max(success_trials)}
P50 = {np.percentile(np.array(success_trials), 50)}
P90 = {np.percentile(np.array(success_trials), 90)}
Stdev = {round(np.std(np.array(success_trials)), 2)}
Trials = {trials}""")
