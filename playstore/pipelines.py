# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from twisted.enterprise import adbapi
import MySQLdb.cursors

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class AppUrlPipeline(object):
    def __init__(self):
        client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        games = self.collection.find()

        if games is not None:
            raise DropItem("Duplicate found for %s" % (item['title']))
        else:
            return self.collection.insert(dict(item))
        return item


class MongoDBPipeline(object):
    def __init__(self):
        client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        matching_item = self.collection.find_one(
            {'title': item['title']}
        )

        if matching_item is not None:
            raise DropItem("Duplicate found for %s" % (item['title']))
        else:
            return self.collection.insert(dict(item))

        # valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        #     if valid:
        #         self.collection.insert(dict(item))
        #         log.msg("Game added to MongoDB database!", level=log.DEBUG, spider=spider)
        # return item


class SQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='bam', user='root', passwd='test1234',
                                            cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)
        # pass

    def process_item(self, item, spider):
        # run db query in thread pool
        print 'process item----------------------'
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        tx.execute("select name from game where name = %s", (self.safeValue(item['name']), ))
        result = tx.fetchone()
        if result:
            print 'exist --- ' + self.safeValue(item['name'])
        else:
            tx.execute( \
                "insert into game (name , author , rating, votes, image, fileSize, datePublished, contentRating, category, price, downloads, description, screenShots, version) values (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.safeValue(item['name']), self.safeValue(item['author']), self.safeValue(item['rating']),
                 self.safeValue(item['votes']), self.safeValue(item['image']), self.safeValue(item['fileSize']),
                 self.safeValue(item['datePublished']), self.safeValue(item['contentRating']),
                 self.safeValue(item['category']), self.safeValue(item['price']), self.safeValue(item['downloads']),
                 self.safeValue(item['description']), item['screenShots'].encode("utf-8"),
                 self.safeValue(item['version']))
            )
            print 'store --------'

    def safeValue(self, value):
        if value == []:
            return ''
        else:
            return value[0].encode("utf-8")

    def handle_error(self, e):
        print e
