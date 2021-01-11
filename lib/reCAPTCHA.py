# coding=utf-8

"""
    reCAPTCHA : script that solves the Google invisible recaptcha
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

#For evoload.io
#key = "6Ldv2fYUAAAAALstHex35R1aDDYakYO85jt0ot-c";
#co = "aHR0cHM6Ly9ldm9sb2FkLmlvOjQ0Mw..";
#loc = "https://evoload.io"; referer

#get_token(key,co,"",loc);

def get_token(site_key, co, sa, loc):
    default_headers = dict()
    default_headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    default_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    default_headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    default_headers["Accept-Charset"] = "UTF-8"
    default_headers["Accept-Encoding"] = "gzip"
    default_headers["Referer"]=loc

    url1='https://www.google.com/recaptcha/api.js'
    s = requests.session()
    req = s.get(url1, headers=default_headers)
    data = req.text
    # in data can be found v
    # po.src = 'https://www.gstatic.com/recaptcha/releases/qc5B-qjP0QEimFYUxcpWJy5B/recaptcha__es.js';
    regex = r"releases\/(.*?)\/"
    v=re.findall(regex,data,re.MULTILINE)[0]
    cb='123456789'

    # https://www.google.com/recaptcha/api2/anchor?
    # ar=1&
    # k=6Ldv2fYUAAAAALstHex35R1aDDYakYO85jt0ot-c&
    # co=aHR0cHM6Ly9ldm9sb2FkLmlvOjQ0Mw..&
    # hl=es&
    # v=qc5B-qjP0QEimFYUxcpWJy5B&
    # size=invisible&
    # cb=bz0ghw418wug

    url2="https://www.google.com/recaptcha/api2/anchor?ar=1&k=" + site_key + "&co=" +co +"&hl=ro&v=" + v + "&size=invisible&cb=" + cb

    req = s.get(url2)
    data = req.text
    data= data.replace('\x22','')

    c=''
    try:
        regex = r"recaptcha-token.*?=(.*?)>"
        c = re.findall(regex, data, re.MULTILINE)[0]
    except:
        print('error getting recaptcha-token')
        return

    url3 = "https://www.google.com/recaptcha/api2/reload?k=" + site_key

    post_data={'v':v,
       'reason':'q',
       'k':site_key,
       'c':c,
       'sa':sa,
       'co':co}

    headers = dict()
    headers['Accept']='*/*'
    headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    headers["Connection"] = "keep-alive"
    headers["Accept-Encoding"] = "deflate"
    headers["Content-Type"] = "application/x-www-form-urlencoded;charset=utf-8"
    headers["Referer"] = url2

    req_url3=s.post(url3,data=post_data,headers=headers)
    data=req_url3.text
    regex = r"resp\",\"(.*?)\""
    token=re.findall(regex,data,re.MULTILINE)[0]
    return token
