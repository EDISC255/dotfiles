#!/bin/bash
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep "V" | cut -d '/' -f 2 | xargs)
VOLCTL=$1
case "$VOLCTL" in
"+") 

    if [ ! $VOLUME ==  "150%" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ +5%
        # nf-fa-volume_up
        dunstify -t 1000 "  + $VOLUME %"
    else 
        dunstify -t 1000 "volumen maximo"
    fi
;;
"-")

    if [ ! $VOLUME ==  "0%" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ -5%
        dunstify -t 1000 "  - $VOLUME %"
    else 
        dunstify -t 1000 ""
    fi
 ;;

*) echo  " ";;
esac 
