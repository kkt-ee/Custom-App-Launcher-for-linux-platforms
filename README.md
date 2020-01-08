# Custom-App-Launcher-for-linux-PC
(Analogy: start menu of windows)

This is a PySimpleGUI based Application Launcher.
The Linux shell commands for "launching an APP in an custom virtual environment" are integrated as button events of the launcher.

N.B. This is running demo version of custom launcher as per my personal needs and this project can be further scaled as per any users' personal needs.

--------

USAGE

      1. Setting up environment: 
            pip install pySimpleGUI
            Install any other dependency packages based on the current system
            
      2. Configure shell commands/app launching shell script (Update the following template files)
            a. dbCOMMANDSignature.py with the terminal commands
            b. write .sh scripts for setting up any customized app launches 
               (eg. spyder in a virtual environment, follow example .sh files in this repository)
                        
      3. Make corresponding changes (based on step 2) for GUI buttons and button events in file: _launchUtils_dev.py 
      
      4. Launch the launcher from the terminal using
            python __init__.py
      



