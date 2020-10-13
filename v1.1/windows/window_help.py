import PySimpleGUI as sg
from db import d
import subprocess

class window_help:
        """
        main launcher window (first window)
        """
        def __init__(self):
            self.layout = [[sg.Text('HELP TOPICS')],
                        [sg.Button('GentooUpdate')],
                        [sg.Button('Backup2HDD')],
                        [sg.Button('ssh_ASUS')],
                        [sg.Button('4.')],
                        [sg.Button('5.')],  # xxxxxxx
                        [sg.Button('6.')],
                        [sg.Button('7.')],
                        [sg.Button('8.')],
                        [sg.Button('9.')],
                        [sg.Button('10.')],

                        #[sg.Button('VBOX+D')],
                        [sg.T('')],
                        [sg.Quit(button_color=('black', 'orange'))]
                        ]

            self.xwindow = sg.Window('HELP TOPICS', self.layout, location=(1, 1), auto_size_text=True)
            self.__render()

        def __render(self):
            while True:
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


