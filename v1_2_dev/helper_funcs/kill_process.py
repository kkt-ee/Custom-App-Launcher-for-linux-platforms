import os, signal
   
def pkill(pid:int):
    """kill a process by process id (pid)"""
    print(pid)
    #print(type(pid))
    os.kill(pid, signal.SIGKILL)  

if __name__ == '__main__':
	pkill(9750)