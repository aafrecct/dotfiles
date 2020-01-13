#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch bar1 and bar2
polybar tray -c ~/.config/polybar/config-tray.ini &
ln -sf /tmp/polybar_mqueue.$! /home/aafrecct/.polybar/traybar
polybar top -c ~/.config/polybar/config-top.ini &
