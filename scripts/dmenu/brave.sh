menu=$(echo -e "YOUTUBEMUSIC\nYOUTUBE\nGOOGLE\nGMAIL\nCHATGPT\nGDRIVE\nGITHUB\nWHATSAPP\nGMEET\nEXCALIDRAW\nDOCKERHUB" | sort | dmenu -i -nb '#000000' -fn 'Hack Nerd Font Mono: size=14' -p 'PAGINAS FRECUENTES')
case "$menu" in
    "YOUTUBE") brave "https://youtube.com/";;

    "YOUTUBEMUSIC") brave "https://music.youtube.com/";;

    "GOOGLE") brave "https://google.com/";;

    "GMAIL") brave "https://mail.google.com/";;
    
    "CHATGPT") brave "https://www.chatgpt.com/";;
    
    "GITHUB") brave "https://www.github.com/";;

    "GDRIVE") brave "https://drive.google.com/";;

    "WHATSAPP") brave "https://web.whatsapp.com/";;

    "GMEET") brave "https://meet.google.com/";; 
    
    "EXCALIDRAW") brave "https://excalidraw.com/";;

    "DOCKERHUB") brave "https://hub.docker.com/";;

    *) echo  " ";;
esac
