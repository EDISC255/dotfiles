#!/bin/bash
BRICTL=$1
MAX_BRI=$(brightnessctl max)
case "$BRICTL" in
"+")
    brightnessctl set +10% > /dev/null
    BRILLO=$(brightnessctl get)
    PORC_BRILLO=$((($BRILLO * 100)/$MAX_BRI))
    dunstify -t 1000 "󰃠 + $PORC_BRILLO %" 
    echo $PORC_BRILLO

;;
"-")
    brightnessctl set 10%- > /dev/null
    BRILLO=$(brightnessctl get) 
    PORC_BRILLO=$((($BRILLO * 100)/$MAX_BRI))
    dunstify -t 1000 "󰃠 - $PORC_BRILLO %"
    echo $PORC_BRILLO
;;

*)echo " ";;
esac
