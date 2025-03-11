#! /bin/bash

yay -S qtile-extras picom-git spotify rofi-bluetooth-git i3lock-color plex-desktop notion-app-electron 1password nordvpn-bin visual-studio-code-bin spotify proton-ge-custom-bin primevideo netflix disneyplus google-chrome messenger-nativefier &
systemctl --user start clipmenud &
systemctl --user enable clipmenud
