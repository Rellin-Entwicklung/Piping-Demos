from multiprocessing import Process, Pipe, Queue, current_process

import time, random, serial, os

global parent_conn, parent_connB, parent_connC, statusQ, statusQ_B, statusQ_C
myTempSensor = 1

def gettempProc(conn,dta2):
    print("gettempproc gerufen")
    while (True):
        t = time.time()
        print("time: ",t,dta2)
        time.sleep(1.5) #.1+~.83 = ~1.33 seconds
        dta_1 = 34
        dta_2 = 35
        dta_3 = 36
        conn.send([dta_1,dta_2])

def Control_Proc():
    p = current_process()
    print('Starting:', p.name, p.pid)
    parent_conn_temp, child_conn_temp = Pipe()
    ptemp = Process(name="gettempProc", target=gettempProc, args=(child_conn_temp, myTempSensor))
    ptemp.daemon = True
    ptemp.start()

    while(True):
        while parent_conn_temp.poll():
            data_01,data_02 = parent_conn_temp.recv()
            print("data: ",data_01)


if __name__ == '__main__':
    Control_Proc()

