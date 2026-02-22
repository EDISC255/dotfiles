#!/bin/sh
# xrandr --output DP-3 --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-0 --off &
barrier &

#conky &
dunst &
sh .config/bg.sh &
indicator-stickynotes &
picom & 
setxkbmap latam &
udiskie -a -t &

# volumeicon &
# xrandr --output HDMI-6 --mode 1366x768 --pos 0x0 --rotate normal --output DP-4 --mode 1366x768 --pos 1366x0 --rotate normal
# blueman-applet &
# cbatincon &
