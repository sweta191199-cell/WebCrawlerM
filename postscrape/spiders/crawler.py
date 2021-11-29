import scrapy
from ..items import PostscrapeItem

class Crawler(scrapy.Spider):
    name="schemes"
    start_urls = [
       'https://www.aicte-india.org/schemes/students-development-schemes'
    ]

    def parse(self, response):

        items = PostscrapeItem()

        all_div_schemes = response.css('div.scheme_start')

        for schemes in all_div_schemes:
            title = schemes.css("h5::text").extract()
            content = schemes.css("p::text").extract()
            links = schemes.css("ul.list-inline a").xpath("@href").extract()

            items['title'] = title
            items['content'] = content
            items['links'] = links

            yield items

