#!/bin/bash
dmenu=$(echo -e "SCROT\nSCROT-REGION"|dmenu  -nb '#000000' -fn 'Hack Nerd Font Mono: size=14' -l 3)
case "$dmenu" in
"SCROT") scrot;;
"SCROT-REGION") scrot -s;;

*) echo  " ";;
esac
