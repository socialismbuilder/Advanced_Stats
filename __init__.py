# -*- coding: utf-8 -*-

from aqt import gui_hooks
from .stats import add_stats

def init_addon():
    # 注册统计选项卡hook
    gui_hooks.stats_dialog_will_show.append(add_stats)
    print("Advanced Stats Addon Loaded - Statistics Only Version")

init_addon()
