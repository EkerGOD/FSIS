import asyncio
import importlib.util
import inspect
import os

from rind import settings
from rind.spider import Spider


async def main():
    # 加载爬虫并添加任务
    tasks = []
    for cls in find_spider(settings.SPIDER_DICTIONARY):
        tasks.append(task(cls))
    await asyncio.gather(*tasks)

async def task(cls):
    spider = cls()
    item = await spider.get_response()
    print(item)

def load_class_from_file(filepath):
    # 提取模块名（去掉.py后缀）
    module_name = os.path.splitext(os.path.basename(filepath))[0]

    # 动态加载模块
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # 查找模块中的类
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, Spider):
            return obj

def find_spider(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            cls = load_class_from_file(filepath)

            if cls:
                if cls.enable:
                    yield cls