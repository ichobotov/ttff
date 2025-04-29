import io
import os
import time
import socket
import serial
import sys
from time import sleep
from datetime import datetime, timedelta
import re


### Variables to set ###
how_to_connect = int(input('Type of connection?\n1) Serial\n2) Socket\n(press 1 or 2)\n'))
connection_type = 'ser' if how_to_connect == 1 else 'sk'
if connection_type == 'ser':
    ser_port = str(input('Set "com" port\n'))
elif connection_type == 'sk':
    addr, port = str(input('Set IP:port (e.g. 1.1.1.1:2222)\n')).split(':')
    port = int(port)
power_device = int(input('1) arduino?\n2) mp709?\n(press 1 or 2)\n'))
arduino = True if power_device == 1 else False
mp709 = True if power_device == 2 else False
if arduino:
    arduino_port = str(input('Set arduino port\n'))
elif mp709:
    mp709_id = str(input('Set mp709 Id (e.g. 000007B7)\n'))
mp709_path = r'C:\Users\ichobotov\MP709'


#Setup for quick check
# connection_type = 'ser'
# ser_port = 'com3'
# arduino = True
# arduino_port = 'com26'
# mp709 = False

# connection_type = 'sk'
# addr, port = '10.10.9.148', 8888
# arduino = True
# arduino_port = 'com26'
# mp709 = False



sk=None
ser=None


def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
        return True


def send_command (command):
    if ser:
        ser.write(str.encode(command+'\r\n'))
        file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', command+'\n'])
    if sk:
        sk.sendall(str.encode(command + "\r\n"))
        file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', command + '\n'])


def write_messages():
    if ser:
        line = str(ser.readline().decode("ascii"))
        # file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', line if line != "" else '\n']) # Если timeout=x, будут печататься только метки времени для пустых строк
        file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', line]) # Если timeout=None, пустых строк не будет
        return line
    if sk:
        line = sk.makefile().readline()
        # file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', line if line != "" else '\n']) # Если timeout=x, будут печататься только метки времени для пустых строк
        file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']', line]) # Если timeout=None, пустых строк не будет
        return line



def connect(connection_type: str):
    global sk, ser, addr, port, ser_port
    disconnect()
    if connection_type == 'sk':
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((addr, port))
            return True
        except Exception as exc:
            print (exc)
            print("Unable to connect")
            return False
    if connection_type == 'ser':
        try:
            # ser = serial.Serial(port=ser_port, baudrate=115200, timeout=3)
            ser = serial.Serial(port=ser_port, baudrate=115200)
            return True
        except Exception:
            print ("Unable to connect")
            return False


def disconnect():
    global sk, ser
    # sk.close()
    if sk != None :
        ret = sk.close()
        del sk
        sk = None
    if ser != None :
        ret = ser.close()
        ser = None

def query(c, con_type, readlines=False):
    global sk, ser
    connect(connection_type)
    con_type = ser if con_type == 'ser' else sk
    if isinstance(con_type, socket.socket):
        if not readlines:
            sk.sendall(str.encode(c + "\r\n"))
            time.sleep(1)
            ret = sk.recv(4096).decode()
            return ret
        else:
            sk.sendall(str.encode(c + "\r\n"))
            time.sleep(1)
            ret = sk.recv(4096).decode()
            return ret
    if isinstance(con_type, serial.serialwin32.Serial):
        if not readlines:
            ser.write(str.encode(c + "\r\n"))
            return ser.readline().decode()
        else:
            ser.write(str.encode(c + "\r\n"))
            return ser.readlines()


def power_on(arduino=False, mp709=False):
    if arduino:
        ser = serial.Serial(port=arduino_port, baudrate=115200, timeout=1)
        ser.write(str.encode('$PASHS,PWR,1,ON' + "\r\n"))
        time.sleep(1)
        ser.close()
    if mp709:
        os.system(f'start {mp709_path}\MP709.exe {mp709_id}=ON')
        time.sleep(5)
        os.system('taskkill /f /im MP709.exe')


def power_off(arduino=False, mp709=False):
    if arduino:
        ser = serial.Serial(port=arduino_port, baudrate=115200, timeout=2)
        ser.write(str.encode('$PASHS,PWR,1,OFF' + "\r\n"))
        time.sleep(1)
        ser.close()
    if mp709:
        os.system(f'start {mp709_path}\MP709.exe {mp709_id}=OFF')
        time.sleep(5)
        os.system('taskkill /f /im MP709.exe')

connect(connection_type)


file_number = 0
file_name = 'results.txt'

while os.path.exists(os.path.abspath(file_name)):
    file_number += 1
    file_name = f'results{str(file_number)}.txt'

with open(file_name, 'w+') as file_object:
    communication_port = query('$PASHQ,PRT', connection_type)
    # communication_port = query('$PITEQ,SYS.PRT', connection_type)
    while 'PRT' not in communication_port:
        communication_port = query('$PASHQ,PRT', connection_type)
        # communication_port = query('$PITEQ,SYS.PRT', connection_type)
    communication_port = communication_port[communication_port.find('PRT')+4]
    send_command(f'$PASHS,NME,GGA,{communication_port},ON')
    # send_command(f'$PITES,OUT.NMEA.GGA={communication_port},1')
    trial_count = 1
    while True:
        try:
            line = write_messages()
            # line = str(ser.readline().decode("ascii"))
            # file_object.writelines([datetime.now().time().strftime("[%H%M%S.%ff]")[:-6] + ']',line])
            # file_object.writelines([line.strip(), " t = %s \n " % (datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%ff")[:-5])])
            if find_string(line, f'.*\$G.GGA.*(?<=[E|W],)4,'):
                line = write_messages()
                file_object.flush()
                count_messages = 1
                while find_string(line, f'.*\$G.GGA.*(?<=[E|W],)4,') and count_messages != 10:
                    line = write_messages()
                    file_object.flush()
                    count_messages += 1
                if count_messages == 10:
                    file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] --PWR OFF--\n')
                    # send_command('$PITES,SYS.RST=REBOOT')
                    # send_command('$PASHS,INI,0')
                    power_off(arduino,mp709)
                    sleep(10)
                    file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] --PWR ON--\n')
                    power_on(arduino,mp709)
                    file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] trial {trial_count}...\n')
                    print(f"trial {trial_count}...")
                    trial_count += 1
                    if connection_type == 'sk':
                        no_eth_connection = 0
                        while not connect(connection_type):
                            no_eth_connection += 1
                            file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] Connecting Eth...\n')
                            print('Connecting Eth...\n')
                            if no_eth_connection != 5:
                                continue
                            else:
                                file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] No Eth connection...restart\n')
                                print('No Eth connection...restart\n')
                                file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] --PWR OFF--\n')
                                power_off(arduino, mp709)
                                sleep(10)
                                file_object.write(f'{datetime.now().time().strftime("[%H%M%S.%ff]")[:-6]}] --PWR ON--\n')
                                power_on(arduino, mp709)
                                sleep(20)
        except UnicodeDecodeError:
            continue
        finally:
            file_object.flush()
