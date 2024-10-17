from multiprocessing import Process
from subprocess import run

file_list=['knk_phoenix.cmd', 'knk_comnav.cmd', 'poweroffon.sc', 'phoenix_all_gnss.cmd', 'phoenix_glo_irn_off.cmd']
def run_acom(file):
    run(['acom32', '-u', f'C:\\Users\\ichobotov\\Desktop\\tests\\restarts\\{file}'])


if __name__ == "__main__":
    p_list=[]
    for file in file_list:
        p = Process(target=run_acom, args=(file,))
        p_list.append(p)


    [process.start() for process in p_list]

    [process.join() for process in p_list]