" Path to Python3 executable.
let g:python3_host_prog = '/usr/bin/python3'

" Vim Plug section.
call plug#begin('~/.config/nvim/plugged')

Plug 'chriskempson/base16-vim'
Plug 'dense-analysis/ale'
Plug 'itchyny/lightline.vim'
Plug 'tpope/vim-surround'
Plug 'Shougo/deoplete.nvim'
let g:deoplete#enable_at_startup = 1
Plug 'tbodt/deoplete-tabnine', { 'do': './install.sh' }
Plug 'aafrecct/m88k.vim'

call plug#end()

" Sets colors. Depends on 'chriskempson/base16-vim'.
source ~/.config/nvim/colors.vimrc 

set tabstop=4
set shiftwidth=4
set expandtab
set number relativenumber
set modelines=0
set encoding=utf-8
set autoindent
syntax enable
set autoread
set smartcase
set undofile

