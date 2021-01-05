from multiprocessing import Process, Pipe, Queue, current_process

from datetime import datetime
import time, random, serial, os

global parent_conn
dta1 = 1

def getSensorData(conn,dta1):
    print("getsensorData gerufen")
    ctr = 0
    while ctr < 10:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print("time: ",timestamp)
        time.sleep(1.5)
        dta_1 = random.randint(0,99)
        dta_2 = random.randint(0,99)
        dta_3 = random.randint(0,99)
        conn.send([timestamp, dta_1,dta_2, dta_3])
        ctr += 1

def Control_Proc():
    p = current_process()
    print('Starting:', p.name, p.pid)
    parent_conn_temp, child_conn_temp = Pipe()
    ptemp = Process(name="getSensorData", target=getSensorData, args=(child_conn_temp,dta1))
    ptemp.daemon = True
    ptemp.start()

    while(True):
        while parent_conn_temp.poll():
            timestamp, data_01,data_02, data_03 = parent_conn_temp.recv()
            print(timestamp, " data01: ",data_01, "data_02: ",data_02, "data_03: ",data_03)
            time.sleep(5)


if __name__ == '__main__':
    Control_Proc()

