#!/bin/bash

source /root/anaconda3/etc/profile.d/conda.sh

##write how to open a console


conda --version
# conda info --envs
conda activate L3460launcher && echo 'launcher env activated...'
cd /root/ai.dev/mydev/c_launcherMK1/v1_2_dev
pwd
python __init__.py &
