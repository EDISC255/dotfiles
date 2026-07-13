CERRAR=$(echo -e  "APAGAR\nREINICIAR\nCERRAR SESION" | dmenu -c -nf "$1" -nb "$2" -sf "$3" -sb "$4" -fn 'Hack Nerd Font Mono: size=8'  -l 3 )

case $CERRAR in
   "APAGAR") shutdown now;;
   "REINICIAR") reboot;;
   "CERRAR SESION") 
      case $5 in
         "openbox") openbox --exit;;
         "qtile")  qtile cmd-obj -o cmd -f shutdown;;
         *) exit 1;;
      esac
   ;;
   *) exit 1;;
esac


