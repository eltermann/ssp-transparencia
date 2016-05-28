# -*- coding: utf-8 -*-
from ssptransparencia.spiders.base import SsptransparenciaBaseSpider


class LesaoMorteSpider(SsptransparenciaBaseSpider):
    name = 'lesao-morte'
    first_lvl_link_css = '#cphBody_btnLesaoMorte'
