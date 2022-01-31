import PySimpleGUI as sg
import sys
sys.path.append('/root/ai.dev/mdev/c_launcherMK1/v1_2_dev')
from db import drop_down_items

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))

layout = [
     [sg.Button('dhcp', button_color=('gray50', 'black')),
      sg.Button('wpa', button_color=('green', 'gray10'))],
     [sg.Combo(drop_down_items, size=(44, 1),background_color='springgreen4'),
      sg.Button('Start', button_color=('gray60', 'springgreen4'))],
     [sg.Button('Stop', button_color=('gray50', '#9B0023')),
      sg.Button('Exit', button_color=('white', '#00406B'))],
     [sg.Output(size=(60, 3))],
     [sg.Button('IITB', button_color=('orange', 'gray10'))],
     [sg.Text('>>', pad=((3, 0), 0)),
      sg.Input(size=(44, 1), background_color='white', text_color='black')],
     [sg.Text('----@k.kr.t.')]
]

window = sg.Window("root LAUNCHER",
                   layout,
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1),
                   alpha_channel=.5)

if __name__ == '__main__':
    window()



"""
 # [sg.Text('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)),
    # sg.Text('0', size=(8, 1))],
    # [sg.Text('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
    # sg.Text('1', size=(8, 1))],
    # sg.Button('Start', button_color=('white', 'black')),
     # sg.Button('', button_color=('gray50', 'black')),
"""