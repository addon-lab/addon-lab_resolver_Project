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

from plugins import evoloadio
from plugins import gamovideo
from plugins import videossh

if __name__ == '__main__':
    # urlz='https://evoload.io/e/V4R2kW59HzGZln'
    # req = evoloadio.get_playable_stream('https://evoload.io/e/V4R2kW59HzGZln')
    # print('Embed url: %s - Streams url: %s,' % (urlz, req))

    print('++++++++++++++++ test evoload.io ++++++++++++++++++++++++++++++++++++')

    urls_test_evoload=['https://evoload.io/e/V4R2kW59HzGZln',
               'https://evoload.io/f/t7nV1zql2rwgr9',
               'https://evoload.io/e/d1dabSVJKYMmWp'
                ]
    for url in urls_test_evoload:
        req=evoloadio.get_playable_stream(url)
        print('Embed url: %s - Streams url: %s' %(url,req))

    print('++++++++++++++++ test gamovideo.com ++++++++++++++++++++++++++++++++++++')

    urls_test_gamovideo = ['http://gamovideo.com/08qrylehmpta',
                           'http://gamovideo.com/avazv9iv7vu5',
                           'http://gamovideo.com/tpd2ioeyuh3m']

    for url in urls_test_gamovideo:
        req = gamovideo.get_playable_stream(url)
        print('Embed url: %s - Streams url: %s' % (url, req))

    print('++++++++++++++++ test videos.sh ++++++++++++++++++++++++++++++++++++')

    urls_test_videos_sh = ['https://videos.sh/embed-ybo6ow0j7lwt.html',
                           'https://videos.sh/embed-ae2zr17mm65s.html'
                           ]
    for url in urls_test_videos_sh:
        req = videossh.get_playable_stream(url)
        print('Embed url: %s - Streams url: %s,' % (url, req))





