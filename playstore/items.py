# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PlayStoreItem(Item):
    # define the fields for your item here like:
    title = Field()
    developer = Field()
    category = Field()
    coverImage = Field()
    link = Field()
    updateDate = Field()
    size = Field()
    screenShots = Field()
    promotionVideo = Field()
    description = Field()
    score = Field()
    scoreCount = Field()
    fiveStars = Field()
    fourStars = Field()
    threeStars = Field()
    twoStars = Field()
    oneStars = Field()
    newFeatures = Field()
    numDownloads = Field()
    version = Field()
    osRequired = Field()
    contentRating = Field()
    website = Field()
    email = Field()
    coverImage = Field()
    pass

# class AppCategoryItem(Item):
#     name = Field()
#     url = Field()
