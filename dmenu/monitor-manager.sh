#!/bin/sh
MONITOR=$(echo -e  "LAPTOP\nESPEJO\nEXTENDER\nPROYECTOR" | dmenu -fn 'Hack Nerd Font Mono: size=8' -c -nf "$1" -nb "$2" -sf "$3" -sb "$4"  -l 4)
case $MONITOR in
   "LAPTOP")    xrandr --output LVDS-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off --output VGA-1 --off;;
   "ESPEJO")    xrandr --output LVDS-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --mode 1366x768 --pos 0x0 --rotate normal --output DP-1 --off --output VGA-1 --off;;
   "EXTENDER")  xrandr --output LVDS-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --mode 1366x768 --pos 1366x0 --rotate normal --output DP-1 --off --output VGA-1 --off;;
   "PROYECTOR") xrandr --output LVDS-1 --off --output HDMI-1 --mode 1366x768 --pos 1366x0 --rotate normal --output DP-1 --off --output VGA-1 --off;;
   *) exit 1;;
esac