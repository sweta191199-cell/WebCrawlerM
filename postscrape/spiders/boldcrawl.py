import scrapy
from ..items import women

class Crawler(scrapy.Spider):
    name="spider"
    start_urls = [
       'https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-type/scholarships-for-women/'
    ]

    def parse(self, response):

       edu = women()
        
       all_div_schemes = response.css('div.innercontent')

       for spider in all_div_schemes:
            title = spider.css("h3 a::text").extract()
            content = spider.css("ul li::text").extract()
            links = spider.css("h3 a").xpath("@href").extract()
            

            edu['title'] = title
            edu['content'] = content
            edu['links'] = links

            yield edu

