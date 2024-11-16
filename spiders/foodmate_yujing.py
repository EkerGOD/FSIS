from lxml import etree

from item import Item
from rind.downloader import  extract_all, extract_first
from rind.spider import Spider
from rind.enum import Language




class FoodMateSpider(Spider):
    name = 'foodmate_yujing'
    language = Language.zh_cn
    url = "http://news.foodmate.net/yujing/"

    enable = False

    async def parse(self, response, **kwargs):
        item = Item()
        item['language'] = self.language
        table = response.xpath("/html/body/div[11]/div[2]/div/div/ul")[0]
        li = table.xpath(".//li")
        for i in li:
            a = i.xpath("./a/@href")
            if a:
                full_url = a[0]
                item['url'] = full_url
                item = await self.get_response(url=full_url, callback=self.parse_new, item=item)
        return item

    async def parse_new(self, response, **kwargs):
        item = kwargs["item"]
        item['title'] = response.xpath('//*[@id="title"]/text()')[0]
        item['content'] = extract_all(response, "//*[@id=\"article\"]//text()")
        item['time'] = extract_first(response, "/html/body/div[11]/div[2]/div/div[6]/a/text()")
        return item