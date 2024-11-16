import re

import requests
import aiohttp
from lxml import html, etree


class Downloader:
    def __init__(self):
        pass

    @staticmethod
    async def get_response(url, callback=None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return html.fromstring(await response.text())


def extract_first(response, xpath):
    # print('first')
    if response.xpath(xpath):
        element = response.xpath(xpath)[0]
        return clean_text(element)
    else:
        return None

def extract_all(response, xpath):
    # print('all')
    if response.xpath(xpath):
        # print(''.join(response.xpath(xpath)))
        return clean_text(''.join(response.xpath(xpath)), clean_space=True)
    else:
        return None


def clean_text(text, clean_space=False):
    cleaned_text = re.sub(r'\r\n|\xa0|\u3000', ' ', text)
    cleaned_text = cleaned_text.replace('\r', '').replace('\n', '').replace('\t', '')
    if clean_space:
        cleaned_text = cleaned_text.replace(' ', '')
    return cleaned_text

# class Response:
#     def __init__(self, HtmlElement):
#         self.HtmlElement = HtmlElement
#
#     def safety_xpath(self, xpath):
#         if self.HtmlElement.xpath(xpath):
#             return self.HtmlElement.xpath(xpath)[0]
#         else:
#             return None
