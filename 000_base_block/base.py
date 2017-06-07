# -*- coding: utf-8 -*-
import json
class Test0Pipeline(object):

    def __init__(self):
        self.file = open('items00.jl', 'wb')
  
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
#需在setting打开pipe：
ITEM_PIPELINES = {
    'test0.pipelines.Test0Pipeline': 1,
}

