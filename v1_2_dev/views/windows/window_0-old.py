import PySimpleGUI as sg
#from db import d
import subprocess

# id: Window0 (FIRST WINDOW) ------< ROOT NODE WINDOW >
class window_0:
        """
        WINDOW 0 (first window)
        """
        def __init__(self):
            self.layout = [[sg.Text('LAUNCHER..')],
                        [sg.Button('startLinuxenv')],
                        [sg.Button('GentooUpdate')],
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
                        [sg.Button('HELP')],
                        [sg.T('')],
                        [sg.Quit(button_color=('black', 'orange'))]
                        ]

            #self.xwindow = sg.Window('LAUNCHER BUTTONS', self.layout, location=(1, 1), auto_size_text=True)
            self.xwindow = sg.Window("Borderless Window",
                   self.layout,
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1))


if __name__ == '__main__':
    w0 = window_0()
    w0.xwindow()



