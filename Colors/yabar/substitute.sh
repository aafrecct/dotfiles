#!/bin/bash

templatepath=$1".template"

cp -f $templatepath $1

sed -i s/\#282828/\{-base00-\}/g $1
sed -i s/\#3c3836/\{-base01-\}/g $1
sed -i s/\#504945/\{-base02-\}/g $1
sed -i s/\#665c54/\{-base03-\}/g $1
sed -i s/\#bdae93/\{-base04-\}/g $1
sed -i s/\#d5c4a1/\{-base05-\}/g $1
sed -i s/\#ebdbb2/\{-base06-\}/g $1
sed -i s/\#fbf1c7/\{-base07-\}/g $1
sed -i s/\#fb4934/\{-base08-\}/g $1
sed -i s/\#fe8019/\{-base09-\}/g $1
sed -i s/\#fabd2f/\{-base0A-\}/g $1
sed -i s/\#b8bb26/\{-base0B-\}/g $1
sed -i s/\#8ec07c/\{-base0C-\}/g $1
sed -i s/\#83a598/\{-base0D-\}/g $1
sed -i s/\#d3869b/\{-base0E-\}/g $1
sed -i s/\#d65d0e/\{-base0F-\}/g $1
