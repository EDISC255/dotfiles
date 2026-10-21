#!/bin/bash
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep "V" | cut -d '/' -f 2 | tr -d ' %')
VOLCTL=$1
case "$VOLCTL" in
"+") 

    if [ ! $VOLUME ==  "150" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ +5%
        # nf-fa-volume_up
        MSG=$((VOLUME+5))
    else 
        MSG= "volumen maximo"
    fi 
    dunstify -t 1000 "  + $MSG %"
;;
"-")

    if [ ! $VOLUME ==  "0%" ]; then 
        pactl set-sink-volume @DEFAULT_SINK@ -5%
        MSG=$((VOLUME-5))
#        dunstify -t 1000 "  - $VOLUME %"
    else 
        MSG="0"
#        dunstify -t 1000 ""
    fi

    dunstify -t 1000 "$MSG %"

 ;;
"+-" )

     pactl set-sink-mute @DEFAULT_SINK@ toggle
     STATUS=$(pactl get-sink-mute @DEFAULT_SINK@) 
     dunstify -t 1000 "$STATUS"

;;
*) echo  " ";;
esac 
