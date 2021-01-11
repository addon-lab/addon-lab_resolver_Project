# coding=utf-8

"""
    Gamovideo.py : script that gets stream url from gamovideo.com embed videos
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
from lib import jsunpack

def get_playable_stream(url_):
    url=validate(url_)
    if url =='': return 'Wrong gamovideo.com embed video url'
    default_headers = dict()
    default_headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    default_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    default_headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    default_headers["Accept-Charset"] = "UTF-8"
    default_headers["Accept-Encoding"] = "gzip"
    s = requests.session()
    req = s.get(url, headers=default_headers)
    data=req.text
    if not 'mp4' in data:
        req = s.get(url, headers=default_headers)
    data = req.text

    regex = r"<script type='text\/javascript'>(eval\(function\(p,a,c,k,e,d\).*?)$"
    try:
        packed_data=re.findall(regex,data,re.MULTILINE)[0]
    except:
        print('Error getting packed data')
        return ''

    unpacked_data= jsunpack.unpack(packed_data)
    regex = r"file:\"(https*:.*?)\""
    try:
        stream_url=re.findall(regex,unpacked_data,re.MULTILINE)[0]
    except:
        print('Error getting stream url from unpacked data')
        return ''

    return stream_url

def validate(url):
    #http://gamovideo.com/08qrylehmpta
    #http://gamovideo.com/embed-08qrylehmpta-640x360.html
    regex = r"gamovideo\.com\/(?:embed-|)([a-z0-9]+)"
    try:
        key=re.findall(regex,url,re.MULTILINE)[0]
    except:
        return ''
    return 'http://gamovideo.com/' + key




