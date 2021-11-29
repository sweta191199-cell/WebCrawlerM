import scrapy
from ..items import Boldorg

class Crawler(scrapy.Spider):
    name="b"
    start_urls = [
       'https://bold.org/scholarships/scholarships-for-women/'
    ]

    def parse(self, response):

        tab = Boldorg()

        all_div_schemes = response.css('.ScholarshipItem-module--scholarship--2Fiy6')

        for b in all_div_schemes:
            title = b.css(".ScholarshipItem-module--name--1fuqu span::text").extract()
            content = b.css(".ScholarshipItem-module--description--3Rdny::text").extract()
            amount = b.css(".InfoItem-module--item--3MEHl:nth-child(2) div+ div::text").extract()
            deadline = b.css(".InfoItem-module--item--3MEHl:nth-child(4) div+ div::text").extract()
            links = b.css(".ScholarshipItemActions-module--view--1KmwD")[0].xpath("@href").extract()

            tab['title'] = title
            tab['content'] = content
            tab['links'] = links
            tab['amount'] = amount
            tab['deadline'] = deadline

            yield tab

