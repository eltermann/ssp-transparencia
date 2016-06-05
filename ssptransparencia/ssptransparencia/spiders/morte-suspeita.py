# -*- coding: utf-8 -*-
import scrapy

from ssptransparencia.spiders.base import SsptransparenciaBaseSpider
from ssptransparencia.spiders.base import get_postback


class MorteSuspeitaSpider(SsptransparenciaBaseSpider):
    name = 'morte-suspeita'
    first_lvl_link_css = '#cphBody_btnMorteSuspeita'

    def parse(self, response):
        a = response.css(self.first_lvl_link_css)
        yield scrapy.FormRequest.from_response(response, formid='frmMain',
            formdata=get_postback(a),
            dont_click=True, callback=self.parse_second_menu)

    def parse_second_menu(self, response):
        for a in response.css('#cphBody_divMorteSusp a.btnItem'):
            nav_menu_adicional = a.xpath('./text()').extract_first()
            meta = {'nav_menu_adicional': nav_menu_adicional}
            yield scrapy.FormRequest.from_response(response, formid='frmMain',
                formdata=get_postback(a), dont_click=True,
                callback=self.parse_years, meta=meta)
