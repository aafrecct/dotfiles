#!/usr/bin/env python


from subprocess import run
from os import listdir

config_files = [i for i in listdir('./.config')]
dot_files = [i for i in listdir('./') if i[0] == '.' and i not in ['.git', '.config']]
exec_files = [i for i in listdir('./scripts')]

# for i in config_files:
#     run(['ln', '-srf', './.config/{0}'.format(i) '~/.config/{0}'.format(i)])
#
# for i in exec_files:
#     run(['ln', '-srf', './scripts/{0}'.format(i), '/bin/{0}'.format(i)])

print(dot_files)

for i in dot_files:
    run(['ln', '-srf', './{0}'.format(i), '~/{0}'.format(i)])
