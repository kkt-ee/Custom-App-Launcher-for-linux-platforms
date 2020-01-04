#import os
import subprocess
import PySimpleGUI as sg      

##COMMANDS DICT (:konsole commands)----------------
d = {  'oa.ai':'konsole -e /root/ai.dev/10413Prototypes/_pySimpleGUI.tutorial/_launch_OA.sh',
     'Jupyter':'/root/anaconda3/bin/jupyter notebook --allow-root',
      'Spyder':'/root/ai.dev/10413Prototypes/_pySimpleGUI.tutorial/_launch_spyder.sh',
      'MATLAB':'konsole -e /usr/local/MATLAB/R2017a/bin/matlab -nodesktop',
     'AnyDesk':'/root/_ToolBox/anydesk-5.0.0/anydesk',
         'XDM':'java -jar /root/_ToolBox/xdman.jar',

   'Ubuntu_dev-vbox':'VBoxManage startvm Ubuntu_dev',
                'xU':'VBoxManage controlvm Ubuntu_dev savestate',
              #'sshU':''
              #'scpU':''
             #'scpU>':''
 
 'kali_dojo-vbox':'VBoxManage startvm kali_dojo',
            'xK' :'VBoxManage controlvm kali_dojo savestate',   
           #'sshU':''
           #'scpU':''
          #'scpU>':''

    'w7_nit-vbox':'VBoxManage startvm w7_nit',
           'xw7' :'VBoxManage controlvm w7_nit savestate',
           #'sshU':''
           #'scpU':''
          #'scpU>':''

        'Android':'VBoxManage startvm Android',
            'xA' :'VBoxManage controlvm Android savestate',

   'MLDB-vbox':'VBoxManage startvm MLDB-20170502',
       'xMLDB':'VBoxManage controlvm MLDB-20170502 savestate',

     
   #'pdmount':'/root/.pdmount',
        #'wifi':'/root/.wifi',
             #7:'simplescreenrecorder'
             }
#--------------------------------END----



##id: Window0 (FIRST WINDOW) ------< ROOT NODE WINDOW >
layout0 = [[sg.Text('LAUNCHER..')],    
           [sg.Button('oa.ai')],
           [sg.Button('Jupyter')],      
           [sg.Button('Spyder')], #xxxxxxx
           [sg.Button('MATLAB')], 
           [sg.Button('AnyDesk')],      
           [sg.Button('XDM')],
           #[sg.Button('Ubuntu_dev-vbox'),sg.Button('xU')],
           #[sg.Button('ssh to ubuntu_dev-vbox')],
           #[sg.Button('kali_dojo-vbox'),sg.Button('ssxK')],
         
           #[sg.Button('ssh to kali_dojo-vbox')],
           #[sg.Button('ssh to ASUS phone')],
           [sg.Button('VBOX+D')],      
           [sg.T('')],      
           [sg.Quit(button_color=('black', 'orange'))]      
          ]      

window0 = sg.Window('LAUNCHER BUTTONS', layout0, location=(1,1), auto_size_text=True)    


##id: Window-vbd -------< BRANCH NODE WINDOW >
def windowvbd():
  layoutvbd = [[sg.Text('VBOX + Devices')],    
               [sg.Button('Ubuntu_dev-vbox'),sg.Button('xU'), sg.Button('sshU'),sg.Button('scpU'),sg.Button('scpU>')],
               [sg.Button('kali_dojo-vbox'),sg.Button('xK'),sg.Button('sshK'),sg.Button('scpK'),sg.Button('scpK>')],
               [sg.Button('w7_nit-vbox'),sg.Button('xw7'),sg.Button('sshw7'),sg.Button('scpw7'),sg.Button('scpw7>')],
               [sg.Button('MLDB-vbox'),sg.Button('xMLDB'),sg.Button('sshMLDB'),sg.Button('scpMLDB'),sg.Button('scpMLDB>')],    
               [sg.Button('sshASUS'),sg.Button('scpASUS'),sg.Button('scpASUS>')], 
          
               #[sg.T('')],      
               [sg.Quit(button_color=('black', 'orange'))]
              ]      
                        

  windowvbd = sg.Window('LAUNCHER BUTTONS', layoutvbd, location=(1,1), auto_size_text=True)  

  while(True):
    event, values = windowvbd.Read()      
    print(event, values)

    if event is None or event == 'Exit':
        break
    #button functions here....
    if event in d:
        sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    """DEPRECATED
    if event == 'Ubuntu_dev-vbox': 
        sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)   
    """
    if event == 'Quit'  or values is None:      
        break
  
  windowvbd.close() #---END WINDOW



#      
# Some place later in your code...      
# You need to perform a Read or Refresh on your window every now and then or    
# else it will appear your program has hung      

#      
# your program's main loop----------< MAIN() >      
if __name__ == '__main__':
  while (True):      
    # This is the code that reads and updates your window      
    event, values = window0.Read()      
    print(event, values)  
    if event is None or event == 'Exit':
        break
    
    if event == 'VBOX+D':
        #sp = subprocess.Popen([windowvbd()], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        windowvbd()
    if event in d:
        sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    
    """DEPRECATED ^^^^^^^^^
    if event == 'Jupyter Notebook':  
        sp = subprocess.Popen([d['jupyter']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

    if event == 'Spyder':  
        sp = subprocess.Popen([d['spyder']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  

    if event == 'MATLAB':  
        sp = subprocess.Popen([d['matlab']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)           
        #os.system("konsole -x /usr/local/MATLAB/R2017a/bin/matlab -nodesktop")

    if event == 'AnyDesk':  
        sp = subprocess.Popen([d['anydesk']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
        print(d[event])
        print(d['anydesk'])
    if event == 'XDM':  
        sp = subprocess.Popen([d['xdm']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  

    if event == 'Ubuntu_dev-vbox':  
        sp = subprocess.Popen([d['Ubuntu_dev']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    if event == 'ssxU':  
        sp = subprocess.Popen([d['ssx-Ubuntu_dev']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    """
    
    if event == 'Quit'  or values is None:      
        break    

  window0.Close()





"""GOLD CODE
if event in d:
        sp = subprocess.Popen([d[event]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
"""