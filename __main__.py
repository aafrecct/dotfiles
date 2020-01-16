#!/usr/bin/env python

from subprocess import run
from os import listdir, path
from shutil import which
from json import load

'''
Sets up the system.
This inlcludes:
    * Checking the right packages are installed.
        - light-locker
        - webkit-greeter
        - rofi
        - polybar
        - zsh (and oh-my-zsh)
        - feh
        - kitty
        - bspwm
        - sxhkd
        - ranger
        - compton
    * Checking if the config files are there.
        if the config files exist and are not symlinks:
            | delete and create symlinks.
        elif the config files are already symlinks or dont exist:
            | replace them with the ones in the repo.
        The following files are needed:
            - Polybar:
                - the .config polybar filenames
                - the .polybar home folder
            - Ranger
            - Kitty
            - Bspwm
            - Sxhkd:
            - Compton:
            - Rofi:
            - Xresources
            - zshrc
            - fehbg

'''
current_dir = path.realpath('./')
in_home = '/home/' in current_dir and current_dir.count('/') == 2
folder = path.dirname(__file__) + '/' if path.dirname(__file__) != '' else ''

with open(folder + 'options.json') as file:
    options = load(file)

config_files = [i for i in listdir(folder + 'files/.config')]
config_dir = [i for i in listdir('.config/')]
dot_files = [i for i in listdir(folder + 'files/') if i[0] == '.' and i not in ['.git', '.config']]
dot_dir = [i for i in listdir('.config/')]
exec_files = [i for i in listdir(folder + 'scripts')]

if in_home and run('whoami', capture_output=True).stdout.decode('UTF-8') == 'root\n':
    # Check for the programs.
    for pkg in options['packages']:
        if which(pkg) == None:
            print(pkg + " is missing! Install it before you run this!")
            exit()

    # Check for necesary dirs
    for i in options['needed_dirs']:
        if not path.exists(i):
            print('Please create the following directory: ' + current_dir + i)

    # Check for the files.
    for i in config_files:
        if i in config_dir and not path.islink('.config/' + i):
            if input("Delete .config/" + i + "? [Y/n] ").lower() != n:
                run(['rm', '-r', '.config/' + i])

    # Replace the links.
    run(['ln', '-srf', folder + 'files/*'])
    for i in exec_files:
        run(['ln', '-srf', folder + 'scripts/{0}'.format(i), '/bin/{0}'.format(i)])

elif in_home:
    print('Run this script with sudo so that symlinks can be created in /bin/.')
else:
    print('It looks like you\'re not running the script from your home folder.')
