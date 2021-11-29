import scrapy
from ..items import Boldorg

class Crawler(scrapy.Spider):
    name="spider"
    start_urls = [
       'https://www.scholarships.com/financial-aid/college-scholarships/scholarships-by-type/scholarships-for-women/'
    ]

    def parse(self, response):

       edu = Boldorg()
        
       all_div_schemes = response.css('.innercontent')

       for spider in all_div_schemes:
            title = spider.css(".innercontent h3 a::text").extract()
            content = spider.css(".innercontent li~ li+ li::text").extract()
            links = spider.css(".innercontent h3 a").xpath("@href").extract()
            deadline = spider.css(".innercontent li:nth-child(1)::text").extract()
            amount = spider.css(".innercontent li:nth-child(2)::text").extract()
            

            edu['title'] = title
            edu['content'] = content
            edu['links'] = links
            edu['amount'] = amount
            edu['deadline'] = deadline

            yield edu

