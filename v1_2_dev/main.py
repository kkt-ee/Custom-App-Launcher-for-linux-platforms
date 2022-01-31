import PySimpleGUI as sg
import subprocess

from views.windows.window_0 import window
from views.windows.window_vbd import window_vbd
from views.windows.window_help import window_help
from db import d
from helper_funcs.kill_process import pkill




def main():
    #w0 = window_0()     # ------< WINDOW 0 INSTANCE
    # lay0 = w0.layout
    # win0 = w0.xwindow

    # ---< TEST
    # w_vbd = window_vbd()
    # lay_vbd = w_vbd.layout
    # win_vbd = w_vbd.xwindow

    # w_help = window_help()
    # --- TEST >
    flag = 0   #--< Flag to keep track of open processes
    #q = Queue()
    flag = {}
    while True:
        """RENDERING window_0---:"""
        event, values = window.Read()
        print(f"event> {event} --:-- values> {values}")
        #print(type(event))
        # Program to launch:
        prog_name = values[0]
        #
        #if event is None or event == 'Exit':#) and flag == 0 :
        #    break
        if event in (sg.WIN_CLOSED, 'Exit'):
            if len(flag) == 0:
                break
            else:
                print("!!! To EXIT: Stop alive processes first.")
        # ---< TO UPDATE: ADD NEW WINDOWS BELOW
        if event is 'dhcp':
            sp = subprocess.Popen([d['dhcp']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if event is 'wpa':
            sp = subprocess.Popen([d['wpa']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if event is 'IITB':
            sp = subprocess.Popen([d['IITB']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


        # W1.
        if prog_name == 'VBOX+D':
            if event is 'Start':
                w_vbd = window_vbd()    # -------------< +WINDOW
        #
        # W2.
        if prog_name == 'HELP':
            if event is 'Start':
                w_help = window_help()  # -------------< +WINDOW
        # -----UPDATE >
        #
        # 
        #if event in d:
        #    sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if prog_name in d:
            if event is 'Start':
                #print(f"starting {prog_name}")
                sp = subprocess.Popen([d[prog_name]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"{prog_name} --:-- pid : {sp.pid}")
                flag[prog_name] = sp.pid
            elif event is 'Stop':
                pid = flag[prog_name]
                pkill(pid)
                del flag[prog_name]
               
        #
        #if event == 'Quit' or values is None:
        #    break
        #
    w0.xwindow.Close()

if __name__=='__main__':
    main()