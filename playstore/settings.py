# -*- coding: utf-8 -*-

# Scrapy settings for playstore project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'playstore'

SPIDER_MODULES = ['playstore.spiders']
NEWSPIDER_MODULE = 'playstore.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'playstore (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'playstore.pipelines.MongoDBPipeline': 300,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "play_game"
MONGODB_COLLECTION = "games"
