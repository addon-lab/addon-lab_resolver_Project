import re

from plugins import evoloadio, gamovideo, videossh


class Switcher(object):
    def __init__(self,url):
        self.url = url

    def get_server(self):

        """Dispatch method"""
        method_name = self.get_method(self.url)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "url cannot be resolved")
        # Call the method as we return it
        return method()

    def evoloadio(self):
        result = evoloadio.get_playable_stream(self.url)
        return result

    def gamovideo(self):
        result = gamovideo.get_playable_stream(self.url)
        return result

    def videossh(self):
        result = videossh.get_playable_stream(self.url)
        return result

    def get_method(self,url):
        patron_evoload = r"https*:\/\/(evoload\.io)\/(?:e|f)\/.*?$"  # dev evoload.io
        patron_gamovideo = r"(gamovideo\.com)\/(?:embed-|)[a-z0-9]+"  # dev gamovideo.com
        patron_videossh = r"https*:\/\/(videos\.sh)\/embed-\w+.html"  # dev videos.sh

        resultado = re.findall(patron_evoload, url)
        if len(resultado) > 0: return 'evoloadio'

        resultado = re.findall(patron_gamovideo, url)
        if len(resultado) > 0: return 'gamovideo'

        resultado = re.findall(patron_videossh, url)
        if len(resultado) > 0: return 'videossh'

        return ''
