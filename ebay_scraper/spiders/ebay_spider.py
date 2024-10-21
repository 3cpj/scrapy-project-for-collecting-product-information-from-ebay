import scrapy

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=large+language+model&_sacat=0']

    def parse(self, response):
        self.logger.info(f"Parsing page: {response.url}")
        self.logger.info(f"Found {len(response.css('li.s-item'))} items on this page")
        for product in response.css('li.s-item'):
            yield {
                'Name': product.css('h3.s-item__title::text').get(),
                'Price': product.css('span.s-item__price::text').get(),
                'Shipping Fee': product.css('span.s-item__shipping::text').get(),
                'Location': product.css('span.s-item__location::text').get()
            }

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
