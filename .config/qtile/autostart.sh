#!/bin/sh
# xrandr --output DP-3 --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-0 --off &
# xrandr --output HDMI-0 --mode 1366x768 --pos 0x0 --rotate normal --output DP-3 --mode 1366x768 --pos 1366x0 --rotate normal
feh --bg-fill .config/qtile/wallpaper.png &
setxkbmap latam &
# blueman-applet &
indicator-stickynotes &
conky &
barrier &
# cbatincon &
volumeicon &|