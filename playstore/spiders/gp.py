from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from playstore.items import PlayStoreItem  # remember we declared PlayItem in items.py


class Game (Spider):
    name = "game"  # the name of the spider
    allowed_domains = ["play.google.com"]   # he base-URLs for the allowed domains for the spider to crawl
    # a list of URLs for the spider to start crawling from. All subsequent URLs will start from the data that the spider downloads from the URLS in start_urls
    start_urls = [
        "https://play.google.com/store/apps/category/GAME/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME/collection/topgrossing"

        "https://play.google.com/store/apps/category/GAME_ARCADE/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_ARCADE/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_ARCADE/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_FAMILY/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_FAMILY/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_FAMILY/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_EDUCATIONAL/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_EDUCATIONAL/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_EDUCATIONAL/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_WORD/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_WORD/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_WORD/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_ROLE_PLAYING/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_ROLE_PLAYING/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_ROLE_PLAYING/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_BOARD/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_BOARD/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_BOARD/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_SPORTS/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_SPORTS/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_SPORTS/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_SIMULATION/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_SIMULATION/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_SIMULATION/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_ACTION/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_ACTION/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_ACTION/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_ADVENTURE/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_ADVENTURE/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_ADVENTURE/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_MUSIC/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_MUSIC/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_MUSIC/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_RACING/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_RACING/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_RACING/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_STRATEGY/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_STRATEGY/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_STRATEGY/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_CARD/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_CARD/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_CARD/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_CASINO/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_CASINO/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_CASINO/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_CASUAL/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_CASUAL/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_CASUAL/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_TRIVIA/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_TRIVIA/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_TRIVIA/collection/topgrossing",

        "https://play.google.com/store/apps/category/GAME_PUZZLE/collection/topselling_paid",
        "https://play.google.com/store/apps/category/GAME_PUZZLE/collection/topselling_free",
        "https://play.google.com/store/apps/category/GAME_PUZZLE/collection/topgrossing"
    ]

    def parse(self, response):
        links = Selector(response).xpath('//h2/a[@class="title"]/@href').extract()

        for link in links:
            item = PlayStoreItem()
            link = 'https://play.google.com' + link
            item['link'] = link
            yield Request(url=link, meta={'item': item}, callback=self.parse_game)

    def parse_game(self, response):
        game = Selector(response).xpath('//div[@class="main-content"]')
        item = response.meta['item']
        item['title'] = game.xpath('//div[@class="document-title"]/div/text()').extract()[0]
        item['coverImage'] = game.xpath('//img[@class="cover-image"]/@src').extract()[0]
        item['developer'] = game.xpath('//a[@class="document-subtitle primary"]/span[@itemprop="name"]/text()').extract()[0]
        item['category'] = game.xpath('//a[@class = "document-subtitle category"]/span[@itemprop="genre"]/text()').extract()[0]
        item['screenShots'] = game.xpath('//div[@class="thumbnails"]/img/@src').extract()
        item['description'] = game.xpath('//*[@class="id-app-orig-desc"]/text() | //*[@class="id-app-orig-desc"]/p/text()').extract()
        item['score'] = game.xpath('//div[@class="score-container"]/div[@class="score"]/text()').extract()[0]
        item['scoreCount'] = game.xpath('//div[@class="score-container"]/div[@class="reviews-stats"]/span[@class="reviews-num"]/text()').extract()[0]
        item['fiveStars'] = game.xpath('//div[@class="rating-bar-container five"]/span[@class="bar-number"]/text()').extract()[0]
        item['fourStars'] = game.xpath('//div[@class="rating-bar-container four"]/span[@class="bar-number"]/text()').extract()[0]
        item['threeStars'] = game.xpath('//div[@class="rating-bar-container three"]/span[@class="bar-number"]/text()').extract()[0]
        item['twoStars'] = game.xpath('//div[@class="rating-bar-container two"]/span[@class="bar-number"]/text()').extract()[0]
        item['oneStars'] = game.xpath('//div[@class="rating-bar-container one"]/span[@class="bar-number"]/text()').extract()[0]
        item['newFeatures'] = game.xpath('//*[@class="recent-change"]/text()').extract()
        item['updateDate'] = game.xpath('//div[@class="content" and @itemprop="datePublished"]/text()').extract()[0]
        item['size'] = game.xpath('//div[@class="content" and @itemprop="fileSize"]/text()').extract()[0]
        item['numDownloads'] = game.xpath('//div[@class="content" and @itemprop="numDownloads"]/text()').extract()[0]
        item['version'] = game.xpath('//div[@class="content" and @itemprop="softwareVersion"]/text()').extract()[0]
        item['osRequired'] = game.xpath('//div[@class="content" and @itemprop="operatingSystems"]/text()').extract()[0]
        item['contentRating'] = game.xpath('//div[@class="content" and @itemprop="contentRating"]/text()').extract()[0]

        # email = game.xpath('//*[@id="body-content"]/div[1]/div[4]/div/div[2]/div[10]/div[2]/a[2]/@href').extract()[0]
        email = game.xpath('//a[@class="dev-link" and contains(@href, "mailto")]/@href').extract()[0]
        item['email'] = str(email).replace("mailto:", "")

        try:
            item['website'] = game.xpath('//a[@class="dev-link" and contains(@href, "https")]/@href').extract()[0]
        except IndexError:
            self.log("Website not exists")

        try:
            item['promotionVideo'] = game.xpath('//span[@class="preview-overlay-container"]/@data-video-url').extract()[0]
        except IndexError:
            self.log("Promotion Video not exists")

        yield item



