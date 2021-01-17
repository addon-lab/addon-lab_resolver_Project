# coding=utf-8

"""
    Megaup_net.py : script that gets stream url from megaup.net embed videos
    Copyright (C) 2021 ADDON-LAB, KAR10S

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests
import re

def get_playable_stream(url_):
    import time
    video_urls = ''
    url = validate(url_)
    if url == '': return 'Wrong megaup.net embed video url'
    default_headers = dict()
    default_headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    default_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    default_headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    default_headers["Accept-Charset"] = "UTF-8"
    default_headers["Accept-Encoding"] = "gzip"
    s = requests.session()
    req = s.get(url_, headers=default_headers)
    data=req.text
    regex = "download-timer.*?btn-default.*?href='(.*?)'"
    try:
        url=re.findall(regex,data,re.MULTILINE)[0]
    except:
        return ''

    if url:
        regex_seconds = r"var\s*seconds\s*=\s*(\d*)"
        try:
            seconds = int(re.findall(regex_seconds, data, re.MULTILINE)[0])
        except:
            seconds = 6
        time.sleep(seconds+1)
        data_url = s.get(url,allow_redirects=False)
        media_url = data_url.headers.get('location', '')
        if media_url:
            video_urls=media_url

    return video_urls


def validate(url):
    #https://videos.sh/embed-ybo6ow0j7lwt.html
    regex = r"(https*:\/\/megaup\.net\/.*?\/)"
    try:
        _url_=re.findall(regex,url,re.MULTILINE)[0]
    except:
        return ''
    return _url_

