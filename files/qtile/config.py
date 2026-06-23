# -*- coding: utf-8 -*-
# config.py — Monitor detection entry point
#
# At startup, counts the number of connected monitors via xrandr.
# - 1 monitor  → loads default_monitor.py  (laptop screen only)
# - 3 monitors → loads external_monitors.py (laptop + 2 external)
#
# All three files must live in ~/.config/qtile/

import subprocess
import os
import sys

def count_connected_monitors():
    """Return the number of currently connected monitors detected by xrandr."""
    try:
        output = subprocess.check_output(
            ["xrandr", "--query"], stderr=subprocess.DEVNULL
        ).decode()
        return sum(1 for line in output.splitlines() if " connected" in line)
    except Exception:
        return 1  # fall back to single-monitor if xrandr fails

# Add the qtile config directory to the path so the sub-configs can be imported
qtile_config_dir = os.path.dirname(os.path.abspath(__file__))
if qtile_config_dir not in sys.path:
    sys.path.insert(0, qtile_config_dir)

connected = count_connected_monitors()

if connected >= 3:
    from external_monitors import *  # noqa: F401, F403
else:
    from default_monitor import *    # noqa: F401, F403
