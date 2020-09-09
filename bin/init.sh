#!/bin/bash

source /root/anaconda3/etc/profile.d/conda.sh

##write how to open a console


conda --version
conda activate L3460launcher && echo 'launcher env activated...'
python /root/ai.dev/10413Prototypes/_launcherMK1.dev/__init__.py &
