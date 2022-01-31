# Custom-App-Launcher-for-linux-platform

This is an Custom Application Launcher created with PySimpleGUI for Linux platforms.
The Linux shell commands and shell scripts are integrated as "button events" of the launcher.
Useful for launching of applications in a customized environment (eg. python applications in a virtual environment).

N.B. This is working demo version of a custom app launcher as per my personal requirements. This project can be further scaled as per the users' specific needs.

Demonstration: https://youtu.be/25uZrlINJh4

--------

## Developer and user guide
1. Setting up environment:
 
            pip install pySimpleGUI
            (If needed) Install any other dependency packages based on the current system
            by following error messages (if any) from terminal. 
                                    
2. Make corresponding changes (based on step 2) for "GUI buttons" and "button events" in file:
 
            db.py with the "terminal commands"
            write x.sh scripts for setting up any customized app launches 
            (eg. spyder in a virtual environment, follow example ./bin/*.sh files in this repository)
                        
3. Make window layout (based on step 2) for "GUI buttons" and "button events" in directory: 

            windows 
            (create more layouts if needed)
      
4. Launch the launcher from the terminal using

            python __init__.py
      
## Comment
Version v1.1 woriking fine.


