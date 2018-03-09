import scrapy
from items import MovieItem

class MeijuSpider(scrapy.Spider):
	name = 'meiju'
	allowed_domins = ["meijutt.com"]
	start_urls = ['htttp://www.meijutt.com/new100.html']

	def parse(self, response):
		movies = response.xpath('//ul[@class="top-list fn-clear"]/li')
		for each_movie in movies:
			itme = MovieItem()
			item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
			yield item
