# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class SsptransparenciaItem(scrapy.Item):
    year = scrapy.Field()
    month = scrapy.Field()
    report_number = scrapy.Field()
    report_type = scrapy.Field()
    report_datetime = scrapy.Field()
    city = scrapy.Field()
    police_station = scrapy.Field()
    occurrence_date = scrapy.Field()
    occurrence_address = scrapy.Field()


def map_month(s):
    month = s.lower()
    month = month[:3]
    _m = dict(jan=1, fev=2, mar=3, abr=4, mai=5, jun=6,
              jul=7, ago=8, set=9, out=10, nov=11, dez=12)
    return _m[month]


class SsptransparenciaItemLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()
    year_in = MapCompose(int)
    month_in = MapCompose(map_month)
    city_in = MapCompose(unicode.strip)
