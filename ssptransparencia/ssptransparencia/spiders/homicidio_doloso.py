# -*- coding: utf-8 -*-
import re
import scrapy

from ssptransparencia.items import SsptransparenciaItem
from ssptransparencia.items import SsptransparenciaItemLoader


def get_postback(a_selector):
    href = a_selector.xpath('@href').extract_first()
    m = re.match(r"javascript:__doPostBack\('(.*)','(.*)'\)", href)
    assert m
    return {'__EVENTTARGET': m.group(1), '__EVENTARGUMENT': m.group(2)}


class HomicidioDolosoSpider(scrapy.Spider):
    name = "homicidio-doloso"
    allowed_domains = ["ssp.sp.gov.br"]
    start_urls = (
        'http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx',
    )

    def parse(self, response):
        a = response.css('#cphBody_btnHomicicio')
        yield scrapy.FormRequest.from_response(response, formid='frmMain',
            formdata=get_postback(a),
            dont_click=True, callback=self.parse_years)

    def parse_years(self, response):
        for a in response.css('#cphBody_divDados ul.anoNav li a'):
            year = a.xpath('./text()').extract_first()
            yield scrapy.FormRequest.from_response(response, formid='frmMain',
                formdata=get_postback(a),
                dont_click=True, callback=self.parse_months,
                meta={'year': year})

    def parse_months(self, response):
        year = response.meta['year']
        for a in response.css('#cphBody_divDados ul.mesNav li a'):
            month = a.xpath('./text()').extract_first()
            yield scrapy.FormRequest.from_response(response, formid='frmMain',
                formdata=get_postback(a),
                dont_click=True, callback=self.parse_pages,
                meta={'year': year, 'month': month})

    def parse_pages(self, response):
        self.parse_items(response) # extract items from first page
        year = response.meta['year']
        month = response.meta['month']
        for a in response.css('tr.pager_row table td a'):
            if a.xpath('./text()').extract_first() == '...':
                callback = self.parse_pages
            else:
                callback = self.parse_items
            yield scrapy.FormRequest.from_response(response, formid='frmMain',
                formdata=get_postback(a),
                dont_click=True, callback=callback,
                meta={'year': year, 'month': month})

    def parse_items(self, response):
        for row in response.css('table#cphBody_grdListBO tr'):
            if row.xpath('@class').extract_first() in ['row1', 'row2']:
                l = SsptransparenciaItemLoader(SsptransparenciaItem(), row)
                l.add_value('year', response.meta['year'])
                l.add_value('month', response.meta['month'])
                l.add_xpath('report_number', 'td[1]/a/text()')
                l.add_xpath('report_type', 'td[2]/text()')
                l.add_xpath('city', 'td[3]/text()')
                l.add_xpath('police_station', 'td[4]/text()')
                l.add_xpath('occurrence_date', 'td[5]/text()')
                l.add_xpath('report_datetime', 'td[6]/text()')
                l.add_xpath('occurrence_address', 'td[7]/text()')
                yield l.load_item()
