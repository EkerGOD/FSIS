from rind.spider import Spider
from rind.enum import Language


class FoodSafetySpider(Spider):
    name = 'foodsafety'
    language = Language.zh_tw
    url = "https://www.foodsafety.gov.mo/c/internews/table"

    enable = False

    def parse(self, response):
        print(response)
        return "Done"