import PySimpleGUI as sg
import subprocess
from db import d

class window_vbd:
    # method --id: Window-vbd -------< BRANCH NODE WINDOW >
    def __init__(self):
        self.layout = [[sg.Text('VBOX + Devices')],
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
        self.xwindow = sg.Window('VBOX BUTTONS', self.layout, location=(1, 1), auto_size_text=True)
        self.__render()
        """
        # window rendering main loop----------< MAIN() >--assigning "button events"
        while True:
            event, values = self.windowvbd.Read()
            print(event, values)

            if event is None or event == 'Exit':
                break
            # button functions here....
            if event in d:
                self.sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            
            if event == 'Quit' or values is None:
                break

        self.windowvbd.close()  # ---END WINDOW

    # method --id : main_window_rendering_loop
    """

    def __render(self):
        while True:
            # This is the code that reads and updates your window
            event, values = self.xwindow.Read()
            print(event, values)

            if event is None or event == 'Exit':
                break

            """
            if event == 'VBOX+D':
                 xwindow_vbd
            if event == 'HELP':
                 xwindow_help

            """
            if event in d:
                self.sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if event == 'Quit' or values is None:
                break

        self.xwindow.Close()


