import PySimpleGUI as sg
import subprocess


layout = [
    [sg.Text("1. Start ssh server in ASUS and get ip and port.. \n(eg. 192.168.43.89:2222)")], #[sg.Button("2")],
    [sg.Text("2. connect to ASUS: \nssh -p 2222 ASUS-X01AD-k@192.168.43.89")],
    [sg.Text("3. copy files to L3460: \nrsync -avz bluetooth root@192.168.43.133:~/tmp")], #[sg.Button("1")],
    [sg.Button("OK")]
]


# Create the window
window = sg.Window("ssh ASUS android", layout)

# Create an event loop
while True:
    event, values = window.Read()
    print(event, values)

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()  # ---END WINDOW


