import re
import os
import shutil

'''
The program splits source file to separate files for each trial.
Each trial file starts from the string with ---PWR ON---
and finishes when ---PWR OFF--- is found.
Source file -  {board}_gga.log
Trials files - 1.txt, 2.txt and etc.
'''

# Constants to set
# RESULT_FOLDER = 'comnav_trials'
# PATH = r'C:\python\ttff'
# FILE = 'ComNav_gga_tmp.log'


def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
        return True


def split_to_trials(RESULT_FOLDER, FILE, PATH):

    if os.path.exists(RESULT_FOLDER):
        shutil.rmtree(RESULT_FOLDER)
        os.mkdir(RESULT_FOLDER)
    else:
        os.mkdir(RESULT_FOLDER)

    with open(FILE, 'r') as f:
        i = 1
        switch_pwron_search = True
        switch_pwroff_search = False
        temp = True
        for line in f:
            if find_string(line, '-PWR ON-') and switch_pwron_search:
                # filename = 'trial' + str(i) + '.txt'
                filename = str(i) + '.txt'
                trial = open(os.path.join(PATH, RESULT_FOLDER, filename), 'w')
                trial.write(line)
                switch_pwron_search = False
                switch_pwroff_search = True
                temp = False
                continue
            elif temp:
                continue
            while not find_string(line, '-PWR OFF-') and switch_pwroff_search:
                trial.write(line)
                break
            else:
                trial.close()
                #            os.replace(PATH+trial, os.path.join(PATH, "trials")+trial)
                i += 1
                temp = True
                switch_pwron_search = True

# split_to_trials(RESULT_FOLDER, FILE, PATH)