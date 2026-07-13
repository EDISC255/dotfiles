#!/bin/bash
dmenu=$(echo -e "SCROT\nSCROT-REGION\nSCROT-WINDOW"| dmenu -c -nf "$1" -nb "$2" -sf "$3" -sb "$4" -l 3 -fn 'Hack Nerd Font Mono: size=8')
case "$dmenu" in
"SCROT") scrot;;
"SCROT-REGION") scrot -s;;
"SCROT-WINDOW") scrot -u;;
*) echo  " ";;
esac
