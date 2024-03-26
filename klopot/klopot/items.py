# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose, Identity


class RecepyItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    cuisine = scrapy.Field()
    ingredients = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=Identity(),
    )
    total_time = scrapy.Field()
