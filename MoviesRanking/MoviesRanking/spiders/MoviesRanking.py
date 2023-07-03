import scrapy

class SpiderMoviesRanking(scrapy.Spider):
    name = 'moviesranking'
    start_urls = [
        'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/'
    ]

    custom_settings = {
		'FEED_URI': 'MoviesRanking.json',
		'FEED_FORMAT': 'json',
		'CONCURRENT_REQUESTS': 24,
		'MEMUSAGE_LIMIT_MB': 2048,
		'MEMUSAGE_NOTIFY_MAIL': ['leonardo.nakaya1993@gmail.com'],
		'ROBOTSTXT_OBEY': True,
		'USER_AGENT': 'LeoNakaya',
		'FEED_EXPORT_ENCODING': 'utf8'
	}

    def parse(self, response):
       title = response.xpath('//div/h1/text()').get()
       introduction = response.xpath('//div[@class="articleContentBody"]/p/text()').get()
       tags = response.xpath('//div/p[@class="articleContentSocialNetworks articleContentTags"]/a/text()').getall()
       top_movies = response.xpath('//div/h2/a/text()').getall()

       top = getattr(self, 'top', None)
       if top:
           top = int(top)
           top_movies = top_movies[:top]
        
       yield{
           'Title' : title,
           'Introduction' : introduction,
           'Top_movies' : top_movies,
           'Tags' : tags
       }