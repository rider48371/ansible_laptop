#! /bin/bash

yay -S qtile-extras picom-git spotify rofi-bluetooth-git i3lock-color
systemctl --user start clipmenud
systemctl --user enable clipmenud
