# coding=utf-8
"""
    test for evoload.io, gamovideo.com, videos.sh , reCAPTCHA
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
from plugins import uqload
from plugins.resolver import Switcher

if __name__ == '__main__':
    # url='https://uqload.com/zou067y6840q.html'
    # result=uqload.get_playable_stream(url)




    urls_test =['https://uqload.com/zou067y6840q.html',
                'https://evoload.io/v/6lPcW5MOLkV8nx',
                'https://evoload.io/e/V4R2kW59HzGZln',
                'https://evoload.io/f/t7nV1zql2rwgr9',
                'https://evoload.io/e/d1dabSVJKYMmWp',
                'http://gamovideo.com/3rw8gp8h6fwa',
                'http://gamovideo.com/08qrylehmpta',
                'http://gamovideo.com/avazv9iv7vu5',
                'http://gamovideo.com/tpd2ioeyuh3m',
                'https://videos.sh/embed-ybo6ow0j7lwt.html',
                'https://videos.sh/embed-ae2zr17mm65s.html',
                'https://megaup.net/3CJDR/4.chr1stm4s.g1ft.fr0m.b0b.2020.hdrip.720p.subesp.mp4',
                'https://megaup.net/1AJj6/1p.m4n.4.th3.f1n4l3.2019.brrip.720p.latino.mp4',
                'https://megaup.net/1ACs8/w0nd3r.w0m4n.1984.2020.hdrip.720p.subesp.mp4',
                'https://megaup.net/2WCkC/w0nd3r.w0m4n.1984.brrs.720p.castellano.mp4'
                ]
    for url in urls_test:
            #if 'videos.sh' in url:
            resolved = Switcher(url).get_server()
            print(url + '  :  '  + resolved)






