# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):
    def __init__(self):
        self.file = open('movie.json','w')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        return item

    def __del__(self):
        self.file.close()
