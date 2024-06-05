# # spiders/livemint_spider.py
# from scrapy.http import Request
# import scrapy
# from LiveMint_Scrapper.items import LivemintScraperItem

# class LivemintSpider(scrapy.Spider):
#     name = 'livemint'
#     allowed_domains = ['livemint.com']
#     start_urls = ['https://www.livemint.com']
    
#     def start_requests(self):
#         for url in self.start_urls:
#             yield Request(url, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
            
#     def parse(self, response):
#         article_links = response.xpath('//li//a[contains(text(), "MARKETS")]')
#         print("#################################################")
#         print("\n\n\n\n")
#         print(article_links)
#         # print(article_links.getall())
#         print("\n\n\n\n")
#         print("#################################################")
        
#         # for link in article_links:
#         #     next_page_url = link.attrib['href']
#         #     yield response.follow(next_page_url, self.parse_article)

