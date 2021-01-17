# coding=utf-8

"""
    evoloadio : script that get stream url from evoload.io embed videos
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

import json
import requests
import re
from lib import reCAPTCHA


def get_playable_stream(url_):
    url=validate_url(url_)
    if url == '': return 'Wrong evoload.io embed video url'
    code=get_movie_code(url_)
    default_headers = dict()
    default_headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    default_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    default_headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    default_headers["Accept-Charset"] = "UTF-8"
    default_headers["Accept-Encoding"] = "gzip"
    s= requests.session()
    req=s.get(url_,headers=default_headers)

    key = "6Ldv2fYUAAAAALstHex35R1aDDYakYO85jt0ot-c"     #key .Its is always the same for evoload.io. Could be obtain for evoload.io from https://cdn1.evosrv.com/html/jsx/e.jsx
    co = "aHR0cHM6Ly9ldm9sb2FkLmlvOjQ0Mw.."              #co . Its is always the same for evoload.io
    loc = "https://evoload.io"                           #loc: referer / origin

    token= reCAPTCHA.get_token(key, co, '', loc)
    if token == None or token=='':
        return ' No token obtained'

    secureplayer_url="https://evoload.io/SecurePlayer"
    #{"code":"wEZkuDhnkURe5j","token":"03AGdBq27nr_noUxcJ98JorBLQ7m6ydE-3RfSJBX7eAQGL16Rdu0x1uT8y4Pbm5HPUcR1TmH-sjoBqgQSJUWjmAbCqOzSgcQ5VujY_mUPgs-r1eQ6pmHdhTjZnNfop5upf63-neQUEfONx3-e0roY8g8szPcog5Yu00Fk8twYd228ySQ7s-DC7ijIHv21kTAIt-BivAeqBRedao-aNLaYOANSVWSAShrFN0xOroiXVm31H8il0VJySos13fOUYXuLwSSwEVI3_yEhM7SIBut0T89oVMq6F73LPWxyo-k46hGTAym4rJoYAhUN9RJb5uo8JzWlCCri2GbhKqpc2yxgwwelnh6RMoZRDGhyYvQhF42JaTHS8joDU0xAuzdsf4r5dFIJERxj9Xeud8E3CMbBEx2MADE9vpON4WlW8fVKEQfnKmMaUGHgKIcM"}
    #json
    post='{"code":"' + code + '","token":"'+ token + '"}'
    xsrf=""                             # could be obtained from cookies, but it is not necessary
    header={}
    header['Accept']='Accept: application/json, text/plain, */*'
    header['Accept-Language'] = 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
    header['Accept-Encoding'] = 'deflate'
    header['Content-Type'] = 'application/json;charset=utf-8'
    header['X-XSRF-TOKEN'] = xsrf
    header['Origin'] = loc                       # 'https://evoload.io'
    header['Connection'] = 'keep-alive'
    header['Referer'] = url_
    req=s.post(secureplayer_url,data=post,headers=header)
    jso= json.loads(req.text)
    url_stream=jso.get('stream').get('src')
    return url_stream


def get_movie_code(url):
    partes=url.split("/")
    p=len(partes)
    code=partes[p-1]
    return code

def prepare_url(url):
    url=url.replace('/f/','/e/')
    url = url.replace('/v/', '/e/')
    return url

def validate_url(url):
    regex = r"https*:\/\/evoload\.io\/(?:e|f|v)\/.*?$"
    try:
        url=re.findall(regex,url)[0]
        url=prepare_url(url)
    except:
        url=''
    return url





