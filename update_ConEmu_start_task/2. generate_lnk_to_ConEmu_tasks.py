#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
sys.path.append('..')

from config import DIR_GIST_FILES, DIR_LNKS, PATTERN_NAME_TASK, RE_PATTERN_FILE_TASK
from win_create_shortcut_lnk import create_shortcut


for file_name in DIR_GIST_FILES.glob('*'):
    m = RE_PATTERN_FILE_TASK.search(file_name.stem)
    if not m:
        continue

    name = PATTERN_NAME_TASK.format(m.group(1))
    file_name_lnk = str(DIR_LNKS / f"ConEmu start task '{name}'.lnk")
    create_shortcut(
        file_name=file_name_lnk,
        target=r'C:\Program Files (x86)\ConEmu\ConEmu.exe',
        work_dir=r"C:\Program Files (x86)\ConEmu",
        arguments='/cmd {%s} -new_console' % name,
    )
