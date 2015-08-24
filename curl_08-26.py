#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- 08:00 ~ 26:00に Heroku app を起こし続けるためのスクリプト．
- 上記時間なら 'curl [URL]' を実行．
- Heroku Scheduler により10分おきに実行される．
- 起こす app の URL は urls のリストに記述．
"""
import sys
from datetime import datetime
import pytz
import subprocess

urls = ['https://tweet-predictor.herokuapp.com/',
        'https://trfs.herokuapp.com/']

d = datetime.now(pytz.timezone('Asia/Tokyo'))
if ((d.hour < 3) or (7 < d.hour)) == False:
    sys.exit()
for url in urls:
    cmd = ['curl', url, '-s', '-o', '/dev/null']
    subprocess.call(cmd)
