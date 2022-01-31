# !/usr/bin/env python
import PySimpleGUI as sg
import sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)


sys.path.append('/root/ai.dev/mydev/c_launcherMK1/v1_2_dev')
from db import drop_down_items

# Turn off padding in order to get a really tight looking layout.

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))


class window_0:
    def __init__(self):
        self.drop_down_items = drop_down_items

        self.layout = [
            # [sg.Text('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)),
            # sg.Text('0', size=(8, 1))],
            # [sg.Text('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
            # sg.Text('1', size=(8, 1))],
            [sg.Button('dhcp', button_color=('gray50', 'black')),
             [sg.Combo(self.drop_down_items, size=(44, 1)),
              sg.Button('Start', button_color=('gray60', 'springgreen4'))],
             # sg.Button('Start', button_color=('white', 'black')),
             # sg.Button('', button_color=('gray50', 'black')),
             [sg.Button('Stop', button_color=('gray50', '#9B0023')),
              sg.Button('Exit', button_color=('white', '#00406B'))],
             [sg.Output(size=(60, 3))],
             [sg.Text('>>', pad=((3, 0), 0)),
              sg.Input(size=(44, 1), background_color='white', text_color='black')],
             [sg.Text('----@k.kr.t.')]]
        ]

        self.xwindow = sg.Window("Launcher..",
                                 self.layout,
                                 default_element_size=(12, 1),
                                 text_justification='r',
                                 auto_size_text=False,
                                 auto_size_buttons=False,
                                 no_titlebar=True,
                                 grab_anywhere=True,
                                 default_button_element_size=(12, 1),
                                 alpha_channel=.5)


"""
while True:
    event, values = window.read()
    print(f"event>{event}  :  values>{values}")
    print(values)
    print(values[1])
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
"""

if __name__ == '__main__':
    w0 = window_0()
    w0.xwindow()

# sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
