# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import requests
import urllib
import urllib2
import cookielib
from xiaohua import settings

class XiaohuaPipeline(object):
    
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = '%s/%s/images' % (settings.IMAGES_STORE, spider.name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            #for image_url in item['image_urls']:
            name = item['name']+"."+item['image_urls'].split('.')[1]
            #image_file_name = '_'.join(us)
            file_path = '%s/%s' % (dir_path, name)
            print "file_path: " + file_path
            url_test = "http://www.xiaohuar.com" + item['image_urls']
            print "url_test: ---->>" + url_test
            images.append(file_path)
            
            if os.path.exists(file_path):
                return
            with open(file_path, 'wb') as handle:
                '''
                cj = cookielib.CookieJar()
                opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                conn = opener.open(url_test)
                handle.write(conn.read())
                '''
                request0 = urllib2.Request(url_test)
                request0.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
                conn = urllib2.urlopen(request0)
                handle.write(conn.read())
            handle.close()
            item['images'] = images
        return item
