syntax on
set number
set background=dark
set termguicolors
set noshowmode
set ts=4 sw=4 et
set tabstop=4
so ~/.config/nvim/plug.vim
so ~/.config/nvim/key.vim
let ayucolor='dark'

let g:airline_powerline_fonts=1
let NERDTreeWinPos = "right"
colorscheme ayu
"colorscheme onedark_dark

hi Normal guibg=NONE ctermbg=NONE
hi NormalNC guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE
hi SignColumn guibg=NONE ctermbg=NONE
hi LineNr guibg=NONE ctermbg=NONE

