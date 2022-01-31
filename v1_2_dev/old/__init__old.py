"""
INITIALIZE BY--
RENDERING MAIN WINDOW, i.e. window 0

"""

from windows.window_0 import window_0
from windows.window_vbd import window_vbd
from windows.window_help import window_help
from db import d
import subprocess

if __name__ == '__main__':
    w0 = window_0()     # ------< WINDOW 0 INSTANCE
    # lay0 = w0.layout
    # win0 = w0.xwindow

    # ---< TEST
    # w_vbd = window_vbd()
    # lay_vbd = w_vbd.layout
    # win_vbd = w_vbd.xwindow

    # w_help = window_help()
    # --- TEST >

    while True:
        """
        RENDERING ----- WINDOW_0 UP
        """
        event, values = w0.xwindow.Read()
        print(event, values)

        if event is None or event == 'Exit':
            break
        #
        # ---< TO UPDATE: ADD NEW WINDOWS BELOW
        # W1.
        if event == 'VBOX+D':
            w_vbd = window_vbd()    # -------------< +WINDOW
        #
        # W2.
        if event == 'HELP':
            w_help = window_help()  # -------------< +WINDOW
        #
        # -----UPDATE >
        #
        if event in d:
            sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #
        if event == 'Quit' or values is None:
            break
        #
    w0.xwindow.Close()

"""
# # sp = subprocess.Popen([windowvbd()], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
"""