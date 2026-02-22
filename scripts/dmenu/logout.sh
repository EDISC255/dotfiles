#!/bin/bash
dmenu=$(echo -e "APAGAR\n󰑓REINICIAR\n󰍃CERRAR WM"|dmenu  -nb '#000000' -fn 'Hack Nerd Font Mono: size=14' -l 3)
case "$dmenu" in
"APAGAR") shutdown now;;
"󰑓REINICIAR") reboot;;
"󰍃CERRAR WM") qtile cmd-obj -o root -f shutdown ;;

*) echo  " ";;
esac