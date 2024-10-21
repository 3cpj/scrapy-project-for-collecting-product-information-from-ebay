import scrapy
import json
import os

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=large+language+model&_sacat=0']

    def __init__(self, *args, **kwargs):
        super(EbaySpider, self).__init__(*args, **kwargs)
        self.items = []

    def parse(self, response):
        self.logger.info(f"Parsing page: {response.url}")
        items_found = response.css('li.s-item')
        self.logger.info(f"Found {len(items_found)} items on this page")

        for product in items_found:
            item = {
                'Name': product.css('div.s-item__title span::text').get(),
                'Price': product.css('span.s-item__price::text').get(),
                'Shipping Fee': product.css('span.s-item__shipping::text').get() or 'Not specified',
                'Location': product.css('span.s-item__location::text').get() or 'Not specified'
            }
            self.items.append(item)
            yield item

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            self.logger.info(f"Following next page: {next_page}")
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            self.logger.info("No more pages to follow")

    def closed(self, reason):
        os.makedirs('data', exist_ok=True)
        with open('data/output.json', 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)
        self.logger.info(f"Saved {len(self.items)} items to data/output.json")
