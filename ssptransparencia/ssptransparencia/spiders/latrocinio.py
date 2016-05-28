# -*- coding: utf-8 -*-
from ssptransparencia.spiders.base import SsptransparenciaBaseSpider


class LatrocinioSpider(SsptransparenciaBaseSpider):
    name = 'latrocinio'
    first_lvl_link_css = '#cphBody_btnLatrocinio'
