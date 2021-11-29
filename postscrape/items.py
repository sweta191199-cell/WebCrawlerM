# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()

class Postscheme(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()
    course = scrapy.Field()
    amount = scrapy.Field()
    deadline = scrapy.Field()

class BoldCrawl(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()

class Boldorg(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()
  
class women(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()

