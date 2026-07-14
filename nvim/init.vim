syntax on "activar el resaltado de sintaxys
set number "numero de  linea
set background=dark "resaltado para fondo negro
set termguicolors "esquema de colores del terminal
set noshowmode "desactivar el indicador de modo nativo de vim
set ts=4 sw=4 et "tamaño de tabulaion
set tabstop=4 "tamaño de tabulaion

so ~/.config/nvim/plug.vim "importa el archivo de pluggins
so ~/.config/nvim/key.vim "importa el archivo de atajos de teclado

let ayucolor='dark' "define el esquema de color del tema ayu
let g:deoplete#enable_at_startup = 1 "iniciar deoplete al iniciar neovim
let g:airline_powerline_fonts=1 "se activa el decorador powerline para la barra de estado de airline
let NERDTreeWinPos = "right" "mover la barra NERDTree a la derecha
colorscheme ayu  "esquema de colores ayu
"colorscheme onedark_dark

"transparencias{
hi Normal guibg=NONE ctermbg=NONE
hi NormalNC guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE
hi SignColumn guibg=NONE ctermbg=NONE
hi LineNr guibg=NONE ctermbg=NONE
"}




"autocmd FileType java lua require
