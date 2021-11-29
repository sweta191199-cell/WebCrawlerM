import scrapy
from ..items import Boldorg

class Crawler(scrapy.Spider):
    name="b"
    start_urls = [
       'https://bold.org/scholarships/scholarships-for-women/'
    ]

    def parse(self, response):

        tab = Boldorg()

        all_div_schemes = response.css('div.Box-sc-1yzgw44-0 kchVrk')

        for b in all_div_schemes:
            title = b.css("li.Box-sc-1yzgw44-0 scholarshipGroupTemplate___StyledBox2-sc-17c4cyw-10 eaHJTb gGTmXi .ScholarshipItem-module--name--1fuqu::text").extract()
            content = b.css(".ScholarshipItem-module--description--3Rdny::text").extract()
            links = b.css(".ScholarshipItemActions-module--buttonsContainer--22njj a").xpath("@href").extract()

            tab['title'] = title
            tab['content'] = content
            tab['links'] = links

            yield tab

