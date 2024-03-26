import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from klopot.items import RecepyItem


class RecepyLoader(ItemLoader):
    default_output_processor = TakeFirst()


class KlopotenkoComSpider(scrapy.spiders.SitemapSpider):
    name = "klopotenko_com"
    allowed_domains = ["klopotenko.com"]
    start_urls = ["https://klopotenko.com"]
    sitemap_urls = ["https://klopotenko.com/sitemap_index.xml"]
    sitemap_follow = [r"recipe-sitemap"]

    def sitemap_filter(self, entries):
        for entry in entries:
            if "/en/" in entry["loc"] or "/ru/" in entry["loc"]:
                continue
            yield entry

    def parse(self, response):
        i = RecepyLoader(item=RecepyItem(), response=response)
        i.add_value('url', response.url)
        i.add_css("name", "h1.item-title::text")
        i.add_css("cuisine", "span.recipe-cuisine a::text")
        i.add_css("total_time", ".feature-sub-title.total_time::text", re=r"total_time_text\s(.*)")
        i.add_css("ingredients", ".ingredient-list label")
        yield i.load_item()
