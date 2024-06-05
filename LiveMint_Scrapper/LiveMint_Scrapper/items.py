import scrapy
class LivemintScraperItem(scrapy.Item):

    article_url = scrapy.Field()
    title = scrapy.Field()
    ArticleContent = scrapy.Field()
    author_name = scrapy.Field()
    author_url = scrapy.Field()
    published_date = scrapy.Field()
