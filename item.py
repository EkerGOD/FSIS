import rind
from rind.item import BaseItem, Field


class Item(BaseItem):
    title = Field()
    content = Field()
    time = Field()
    language = Field()
    url = Field()
