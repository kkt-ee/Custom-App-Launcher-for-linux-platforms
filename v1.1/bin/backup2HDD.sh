#!/bin/bash

# TAKING BACKUP OF--
# 1. ai.dev
# 2. keenote notebook
# 3. ~/.config/i3/config
#
#
# rsync -rv source/ destination

#
#----files/dir for backup-------
# [i3 config] 
rsync -av --progress --delete /root/.config/i3/config /run/media/root/My\ Passport/L3460BACKUP/i3config-backup/

# [Keenote Notebook]
rsync -av --progress --delete /root/L3460Notebook/ /run/media/root/My\ Passport/L3460BACKUP/L3460Notebook-backup/

# [keepass data]
rsync -av --progress --delete /root/Documents/.passlocker /run/media/root/My\ Passport/L3460BACKUP/keepass-backup/.passlocker
rsync -av --progress --delete /root/Documents/.Passwords.kdbx /run/media/root/My\ Passport/L3460BACKUP/keepass-backup/.Passwords.kdbx

# [~/ai.dev]
rsync -av --progress --delete /root/ai.dev/ /run/media/root/My\ Passport/L3460BACKUP/ai.dev-backup/

# [~/Documents]
rsync -av --progress --delete /root/Documents/ /run/media/root/My\ Passport/L3460BACKUP/Documents-backup/

# [~/0NOTES]
rsync -av --progress --delete /root/0NOTES/ /run/media/root/My\ Passport/L3460BACKUP/0NOTES-backup/

# [~/bin]
rsync -av --progress --delete /root/bin/ /run/media/root/My\ Passport/L3460BACKUP/bin-backup/

# [~/MYREADINGS]
rsync -av --progress --delete /root/MYREADINGS/ /run/media/root/My\ Passport/L3460BACKUP/MYREADINGS-backup/

# [.bashrc]
rsync -av --progress --delete /root/.bashrc /run/media/root/My\ Passport/L3460BACKUP/bashrc-backup/bashrc 


# []


echo "BACKUP DONE."
