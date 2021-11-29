import scrapy
from ..items import Postscheme

class Crawler(scrapy.Spider):
    name="scheme"
    start_urls = [
       'https://www.scholarshipportal.com/scholarships/india'
    ]

    def parse(self, response):

        table = Postscheme()

        all_div_schemes = response.css('.scholarship__type--list')

        for scheme in all_div_schemes:
            title = scheme.css("h3::text").extract()
            content = scheme.css("p::text").extract()
            links = scheme.css(" a").xpath("@href").extract()
            course = scheme.css(".u-m-left-20::text")[0].extract()
            amount = scheme.css(".u-m-left-20::text")[1].extract()
            deadline = scheme.css(".u-m-left-20::text")[2].extract()

            table['title'] = title
            table['content'] = content
            table['links'] = links
            table['course'] = course
            table['amount'] = amount
            table['deadline'] = deadline

            yield table

