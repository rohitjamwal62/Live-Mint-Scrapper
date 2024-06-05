from scrapy.http import Request
import scrapy
from LiveMint_Scrapper.items import LivemintScraperItem

class LivemintSpider(scrapy.Spider):
    name = 'livemint'
    allowed_domains = ['livemint.com']
    start_urls = ['https://www.livemint.com/news']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_DELAY': 2,  # Add a delay between requests
        'COOKIES_ENABLED': True,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        },
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        },
    }
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse)
            
    def parse(self, response):
        # article_links = response.xpath('//a[@class="sectionName" and contains(text(), "MARKETS")]/@href').getall()
        Headline_Links =  response.xpath("//div/h2[@class='headline']/a/@href").getall()
        for link in Headline_Links:
            if not link.startswith('http'):
                Store_link_Here = response.urljoin(link)
                yield response.follow(Store_link_Here, callback=self.parse_article)

    def parse_article(self, response):
        item = LivemintScraperItem()
        item['article_url'] = response.url
        item['title'] = response.xpath("//div/h1[@class='headline']/text()").get()
        item['ArticleContent'] = response.xpath('//p/text()').getall()
        try:
            item['published_date'] = response.xpath("//span[@class='newTimeStamp']/@data-updatedtime").getall()[0]
        except:
            item['published_date'] = ''
        item['author_name'] = str(response.xpath("//span[@class='articleInfo author ']").getall()).split('</a>')[0].split('">')[-1]
        try:
            item['author_url'] = str(response.xpath("//span[@class='articleInfo author ']").getall()).split('href=')[1].split('">')[0].replace('"','') if str(response.xpath("//span[@class='articleInfo author ']").getall()).split('href=')[1].split('">')[0] else None
        except:
            item['author_url'] = ''
        print(item)
        yield item