import PySimpleGUI as sg
import subprocess


cmd = {
    '1': 'konsole -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_startenv.sh',  # shell script
    '2': 'konsole --noclose -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/updateOS.sh &', # shell script
    '3': 'konsole -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_launch_OA.sh',         # shell script
 }

layout = [[sg.Text("Use commands below:")],
          [sg.Text("$ emaint -a sync")], #[sg.Button("1")],
          [sg.Text("(optional) $ emerge --oneshot sys-apps/portage")], #[sg.Button("2")],
          [sg.Text("$ emerge --ask -uDU --keep-going --with-bdeps=y @world ")], #[sg.Button("3")],
          [sg.Button("OK")]]


# Create the window
window = sg.Window("Gentoo update", layout)

# Create an event loop
while True:
    event, values = window.Read()
    print(event, values)

    #if event == "1":
    #    subprocess.Popen([cmd['1']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #if event == "2":
    #    subprocess.Popen([cmd['2']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #if event == "3":
    #    subprocess.Popen([cmd['3']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()  # ---END WINDOW


