#!/bin/bash

source /root/anaconda3/etc/profile.d/conda.sh
#source /root/anaconda3/bin/activate

##write how to open a console


conda --version
conda activate ai && echo 'AI env activated...'
cd /root/ai.dev/oa-core-master.dev/ && echo 'Starting oa-core-master.dev'
python -m oa 


#/root/anaconda3/etc/profile.d/conda.sh /root/anaconda3/bin/activate ai
