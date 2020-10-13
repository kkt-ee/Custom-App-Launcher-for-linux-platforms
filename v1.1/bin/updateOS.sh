#!/bin/bash

konsole --noclose -e echo $'Gentoo update copy/paste commands:
 $ emaint -a sync
 (optional) $ emerge --oneshot sys-apps/portage
 $ emerge --ask -uDU --keep-going --with-bdeps=y @world
 Thank You.' &
# \no emaint -a sync \no running in other terminal...' &
#konsole --noclose -e emaint -a sync &
konsole &


#function F1()
#{
#    retval='I like programming'
#}

#retval='I hate programming'
#echo $retval
#F1
#echo $retval

#<<COMMENT
#function F2()
#{
#    local  retval='Using BASH Function'
#    echo "$retval"
#}

#getval=$(F2)  
#echo $getval
#COMMENT


# https://linuxhint.com/return-string-bash-functions/
# https://www.linuxjournal.com/content/return-values-bash-functions
