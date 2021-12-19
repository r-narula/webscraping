import scrapy


class QuotesSpider(scrapy.Spider):
    name = "primer-scraper"

    def start_requests(self):
        urls = [
            'https://www.midsouthshooterssupply.com/dept/reloading/primers?itemsperpage=90'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # len(response.css("div.product-description a.catalog-item-name::text").getall())

        for product in response.css('div.product'):
            print(product.css('div.product-description a.catalog-item-name::text').getall())

            yield {
                'price':product.css('div.price-rating-container div.catalog-item-price span.price span::text').get(),
                'title': product.css('div.product-description a.catalog-item-name::text').get(),
                'stock':product.css('div.price-rating-container div.catalog-item-price div div span.status span.out-of-stock::text').get(),
                'maftr': product.css('div.catalog-item-brand-item-number a.catalog-item-brand::text').get(),
            }