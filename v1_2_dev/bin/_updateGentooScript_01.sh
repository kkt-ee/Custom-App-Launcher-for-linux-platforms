#!/bin/bash
keypress() {
  echo -n "hit any key to continue..."
  read -n1 -e -r 2> /dev/null
  echo
}

clear
echo "System Upgrade Script"
echo "--------------------------------------------------------------------------------"
echo
echo -n -e "portage sync ? ([y]/n) "
read key -n1 -e -r 2> /dev/null
if [ "$key" == "n" ]; then
    echo
else
    echo "Portage Sync"
    emerge --sync
fi

echo
echo "Complete system upgrade (emerge -uDU --ask --keep-going --with-bdeps=y @world)"
keypress
START=`date`
emerge -uDU --ask --keep-going --with-bdeps=y @world
# OR
# emerge --ask --update --deep --newuse world
# emerge --ask -uDN @world
STOP=`date`
echo "Start : "$START
echo "End   : "$STOP

echo
echo "Configuration files upgrade (dispatch-conf)"
keypress
dispatch-conf
# OR
# etc-update

echo
echo "Dependencies Clean (emerge -av --depclean)"
keypress
emerge -av --depclean

#echo
#echo "Dependencies Check and Rebuild (revdep-rebuild)"
#keypress
#revdep-rebuild

echo
echo "Freeing up disk space (eclean-dist --deep)"
keypress
eclean-dist --deep
eclean-pkg --deep

echo
echo
echo
echo "--------------------------------------------------------------------------------"
echo "                      System Upgrade Completed"
echo "--------------------------------------------------------------------------------"
echo
echo

### code for 'exit terminal' on keypress
echo "Press any key to exit..."
keypress