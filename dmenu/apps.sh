APPS=("VS CODE" "BRAVE" "FIREFOX" "DBEAVER" "KITTY" "WPS OFFICE" "THUNAR FM" "PAVUCONTROL")
N=${#APPS[@]}

for ((i=0; i<N; i++)) do
   MENU=$MENU${APPS[$i]}"\n"
done

MENU=${MENU%'\n'}  
LAUNCHER=$(echo -e $MENU |sort| dmenu -c -nf "$1" -nb "$2" -sf "$3" -sb "$4"  -l $N -fn 'Hack Nerd Font Mono: size=8')

case $LAUNCHER in
   "VS CODE") code;;
   "BRAVE") brave;;
   "DBEAVER") dbeaver;;
   "KITTY") kitty;;
   "WPS OFFICE" ) wps;;
   "THUNAR FM" ) thunar;;
   "PAVUCONTROL") pavucontrol;;
   "FIREFOX") firefox;;
   *) exit 1;;
esac