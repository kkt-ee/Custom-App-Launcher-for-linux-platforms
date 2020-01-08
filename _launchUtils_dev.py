# import os

import subprocess
import PySimpleGUI as sg
from dbCOMMANDSignature import d  # importing custom command dictionary


class launcher():
    def __init__(self):
        # id: Window0 (FIRST WINDOW) ------< ROOT NODE WINDOW >
        self.layout0 = [[sg.Text('LAUNCHER..')],
                        [sg.Button('startLinuxenv')],
                        [sg.Button('oa.ai')],
                        [sg.Button('Jupyter')],
                        [sg.Button('Spyder')],  # xxxxxxx
                        [sg.Button('MATLAB')],
                        [sg.Button('AnyDesk')],
                        [sg.Button('XDM')],
                        # [sg.Button('Ubuntu_dev-vbox'),sg.Button('xU')],
                        # [sg.Button('ssh to ubuntu_dev-vbox')],
                        # [sg.Button('kali_dojo-vbox'),sg.Button('ssxK')],

                        # [sg.Button('ssh to kali_dojo-vbox')],
                        # [sg.Button('ssh to ASUS phone')],
                        [sg.Button('VBOX+D')],
                        [sg.T('')],
                        [sg.Quit(button_color=('black', 'orange'))]
                        ]

        self.window0 = sg.Window('LAUNCHER BUTTONS', self.layout0, location=(1, 1), auto_size_text=True)

    # method --id: Window-vbd -------< BRANCH NODE WINDOW >
    def windowvbd(self):
        self.layoutvbd = [[sg.Text('VBOX + Devices')],
                          [sg.Button('Ubuntu_dev-vbox'), sg.Button('xU'), sg.Button('sshU'), sg.Button('scpU'),
                           sg.Button('scpU>')],
                          [sg.Button('kali_dojo-vbox'), sg.Button('xK'), sg.Button('sshK'), sg.Button('scpK'),
                           sg.Button('scpK>')],
                          [sg.Button('w7_nit-vbox'), sg.Button('xw7'), sg.Button('sshw7'), sg.Button('scpw7'),
                           sg.Button('scpw7>')],
                          [sg.Button('MLDB-vbox'), sg.Button('xMLDB'), sg.Button('sshMLDB'), sg.Button('scpMLDB'),
                           sg.Button('scpMLDB>')],
                          [sg.Button('sshASUS'), sg.Button('scpASUS'), sg.Button('scpASUS>')],

                          # [sg.T('')],
                          [sg.Quit(button_color=('black', 'orange'))]
                          ]
        self.windowvbd = sg.Window('LAUNCHER BUTTONS', self.layoutvbd, location=(1, 1), auto_size_text=True)

        # window rendering main loop----------< MAIN() >--assigning "button events"
        while True:
            event, values = self.windowvbd.Read()
            print(event, values)

            if event is None or event == 'Exit':
                break
            # button functions here....
            if event in d:
                self.sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            """DEPRECATED code
            if event == 'Ubuntu_dev-vbox': 
                sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
            """
            if event == 'Quit' or values is None:
                break

        self.windowvbd.close()  # ---END WINDOW

    # method --id : main_window_rendering_loop
    def showx(self):
        # window rendering main loop----------< MAIN() >
        while True:
            # This is the code that reads and updates your window
            event, values = self.window0.Read()
            print(event, values)
            if event is None or event == 'Exit':
                break

            if event == 'VBOX+D':
                # sp = subprocess.Popen([windowvbd()], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.windowvbd()
            if event in d:
                self.sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if event == 'Quit' or values is None:
                break

        self.window0.Close()


"""
#      
# Some place later in your code...      
# You need to perform a Read or Refresh on your window every now and then or    
# else it will appear your program has hung      

"""

"""GOLD CODE
if event in d:
        sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
"""
