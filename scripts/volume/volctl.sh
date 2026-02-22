#!/bin/bash
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep "V" | cut -d '/' -f 2 | xargs)
VOLCTL=$1
case "$VOLCTL" in
"+") 

    if [ ! $VOLUME ==  "150%" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ +5%
        dunstify -i ~/.config/volume/volume-loud-svgrepo-com.svg -t 1000 "$VOLUME %"
    else 
        dunstify -i ~/.config/scripts/volume/volume-loud-svgrepo-com.svg -t 1000 "volumen maximo"
    fi
;;
"-")

    if [ ! $VOLUME ==  "0%" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ -5%
        dunstify -i /home/eduardo/.config/scripts/volume/volume-small-svgrepo-com.svg -t 1000 "$VOLUME %"
    else 
        dunstify -i /home/eduardo/.config/scripts/volume/volume-svgrepo-com.svg -t 1000 ""
    fi
 ;;

*) echo  " ";;
esac 
