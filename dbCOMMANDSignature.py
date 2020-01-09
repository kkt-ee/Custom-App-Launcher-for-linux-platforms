# COMMANDS DICTIONARY
# schema:
#     {key : terminal command}


d = {
    'startLinuxenv': 'konsole -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_startenv.sh',  # shell script
    'GentooUpdate': 'konsole -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_updateGentooScript_01.sh', # shell script
    'oa.ai': 'konsole -e /root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_launch_OA.sh',         # shell script
    'Jupyter': '/root/anaconda3/bin/jupyter notebook --allow-root',                                # shell command
    'Spyder': '/root/ai.dev/10413Prototypes/_launcherMK1.dev/bin/_launch_spyder.sh',               # shell script
    'MATLAB': 'konsole -e /usr/local/MATLAB/R2017a/bin/matlab -nodesktop',                         # shell command
    'AnyDesk': '/root/_ToolBox/anydesk-5.0.0/anydesk',                                             # shell command
    'XDM': 'java -jar /root/_ToolBox/xdman.jar',                                                   # shell command

    'Ubuntu_dev-vbox': 'VBoxManage startvm Ubuntu_dev',                                            # shell command
    'xU': 'VBoxManage controlvm Ubuntu_dev savestate',                                             # shell command
    # 'sshU':''
    # 'scpU':''
    # 'scpU>':''

    'kali_dojo-vbox': 'VBoxManage startvm kali_dojo',  # shell command
    'xK': 'VBoxManage controlvm kali_dojo savestate',  # shell command
    # 'sshU':''
    # 'scpU':''
    # 'scpU>':''

    'w7_nit-vbox': 'VBoxManage startvm w7_nit',        # shell command
    'xw7': 'VBoxManage controlvm w7_nit savestate',    # shell command
    # 'sshU':''
    # 'scpU':''
    # 'scpU>':''

    'Android': 'VBoxManage startvm Android',           # shell command
    'xA': 'VBoxManage controlvm Android savestate',    # shell command

    'MLDB-vbox': 'VBoxManage startvm MLDB-20170502',          # shell command
    'xMLDB': 'VBoxManage controlvm MLDB-20170502 savestate',  # shell command

    # 'pdmount': '/root/.pdmount',
    # 'wifi': '/root/.wifi',
    # 'screenRecord': 'simplescreenrecorder'

    # ...ADD MORE...
    # ..
    # ..
}

# ----END----
