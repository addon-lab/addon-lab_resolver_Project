# coding=utf-8

"""
    uqload.py : script that gets stream url from uqload.com embed videos
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

import re
import requests
import urllib


def get_playable_stream(url_):
    url = validate(url_)
    if url == '': return 'Wrong videos.sh embed video url'
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
    regex = r"sources:\s*[['\"]+(?P<url>[^'\"]+)"
    try:
        stream_url =re.findall(regex,data,re.MULTILINE)[0]
    except:
        stream_url= None

    if stream_url:
        headers={}
        headers['Cookie']=req.headers.get('Set-Cookie')
        headers['User-Agent'] = default_headers.get('User-Agent')
        headers['Referer'] = url
        encoded_headers = urllib.urlencode(headers)
        stream_url='|'.join([stream_url,encoded_headers])
        # https://m90.uqload.com/3rfkpm6omvw2q4drdlt7b77ydbqzrmqqzibw6yvurqhe7e4zcbmtz2wg42qa/v.mp4|Cookie=__cfduid%3Dd9256cf196e732dd43cb46344741d0ccb1610842244%3B+expires%3DTue%2C+16-Feb-21+00%3A10%3A44+GMT%3B+path%3D%2F%3B+domain%3D.uqload.com%3B+HttpOnly%3B+SameSite%3DLax&Referer=https%3A%2F%2Fuqload.com%2Fembed-88sk8o25surd.html&User-Agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F70.0.3538.102+Safari%2F537.36+Edge%2F18.18363'

    return stream_url


def validate(url):
    #https://uqload.com/zou067y6840q.html
    _url_=''
    if not 'uqload.com' in url: return ''
    regex = r".*\/([a-zA-Z0-9]+)"
    media_id=re.findall(regex,url)
    if media_id and len(media_id)>0:
        host = 'uqload.com'
        _url_=get_url(host,media_id[0])
    return _url_

def get_url( host, media_id):
    template = 'http://{host}/embed-{media_id}.html'
    return template.format(host=host, media_id=media_id)

