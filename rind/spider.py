from rind.enum import Language
from rind.downloader import Downloader


class Spider:
    name: str
    language: Language
    url: str

    enable = True

    async def parse(self, response, **kwargs):
        pass

    async def get_response(self,url=None, callback=None, **kwargs):
        for key, value in kwargs.items():
            print(key, value)
        if url is None:
            url = self.url
        if callback is None:
            callback = self.parse
        response = await Downloader.get_response(url)
        return await callback(response, **kwargs)
