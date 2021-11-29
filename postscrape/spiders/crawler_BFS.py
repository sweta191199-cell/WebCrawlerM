import scrapy
from ..items import BoldCrawl

class Crawler(scrapy.Spider):
    name="org"
    start_urls = [
       'https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/women'
    ]

    def parse(self, response):

        bold = BoldCrawl()

        all_div_schemes = response.css('.ScholarshipItem-module--scholarship--2Fiy6')

        for org in all_div_schemes:
            links = org.css(".field-content a").xpath("@href").extract()
            title = org.css(".field-content a::text").extract()
            

            bold['links'] = links
            bold['title'] = title

            yield bold

