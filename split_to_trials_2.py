import io
import re
import os
import shutil
import time

'''
The program splits source file to separate files for each trial.
Each trial file starts from the string with ---PWR ON---
and finishes when ---PWR OFF--- is found.
Source file -  {board}_gga.log
Trials files - 1.txt, 2.txt and etc.
'''

# Constants to set
# RESULT_FOLDER = 'try_delete'
# PATH = r'C:\python\ttff'
# FILE = 'try.txt'


def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
        return True


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
    switch_pwron_search = True
    switch_pwroff_search = False

    with open (FILE) as f:
        for line in file_reader(f):
            if find_string(line, '-PWR ON-') and switch_pwron_search:
                filename = str(i) + '.txt'
                trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'w')
                trial.write(line)
                switch_pwron_search = False
                switch_pwroff_search = True
                continue
            while not find_string(line, '-PWR OFF-') and switch_pwroff_search:
                trial.write(line)
                try:
                    line = next(file_reader(f))
                except StopIteration:
                    break
            try:
                # trial
                io.TextIOWrapper.__instancecheck__(trial) #
            except NameError:
                continue
            trial.write(line)
            trial.close()
            del trial
            switch_pwron_search = True
            switch_pwroff_search = False
            i+=1
# start_time = time.time()
# split_to_trials(RESULT_FOLDER, FILE, PATH)
# print("--- %s seconds ---" % (time.time() - start_time))
