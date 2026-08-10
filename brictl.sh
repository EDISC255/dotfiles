#!/bin/bash
BRICTL=$1
case "$BRICTL" in
"+")
    brightnessctl set +10% > /dev/null
    BRILLO=$(brightnessctl get)
    PORC_BRILLO=$((($BRILLO * 100)/19200))
    dunstify -t 1000 "󰃠 + $PORC_BRILLO %" 
    echo $PORC_BRILLO

;;
"-")
    brightnessctl set 10%- > /dev/null
    BRILLO=$(brightnessctl get) 
    PORC_BRILLO=$((($BRILLO * 100)/19200))
    dunstify -t 1000 "󰃠 - $PORC_BRILLO %"
    echo $PORC_BRILLO
;;

*)echo " ";;
esac
