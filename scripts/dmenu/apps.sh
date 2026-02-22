#!/bin/bash
dmenu=$(echo -e "SCREENKEY\nKITTY\nOBS\nBRAVE\nFIREFOX\nPCMANFM\nVSCODE\nWPSOFFICE\nANDROIDSTUDIO\nNETBEANS\nANYDESK\nDBEAVER\nVIRTUALBOX\nGIMP\nPAVUCONTROL" | sort | dmenu -i -nb '#000000' -fn 'Hack Nerd Font Mono: size=14' -p "APLICACIONES")
case "$dmenu" in
"SCREENKEY") screenkey;;
"KITTY") kitty;;
"BRAVE") sh $HOME"/.config/qtile/scripts/brave.sh"   ;;
"FIREFOX") firefox;;
"PCMANFM") pcmanfm ;;
"WPSOFFICE") wps;;
"VSCODE") code;;
"ANDROIDSTUDIO") android-studio ;;
"NETBEANS") netbeans;;
"ANYDESK") anydesk;;
"DBEAVER") dbeaver ;;
"VIRTUALBOX") virtualbox;;
"GIMP") gimp ;;
"PAVUCONTROL") pavucontrol;;
"OBS") obs;;
*) echo  " ";;
esac 
