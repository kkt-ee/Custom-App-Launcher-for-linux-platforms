import sys
sys.path.append('/root/ai.dev/__mytools__') 
from myplugs.ProcessLauncherUnit_v1_1 import ProcessLaucherUnit
from log_clipboard import log_clipboard

#pass
#myprocess = 'keepnote'
#ProcessLaucherUnit(myprocess)
ProcessLaucherUnit(log_clipboard)
