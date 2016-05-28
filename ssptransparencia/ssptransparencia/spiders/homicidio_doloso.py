# -*- coding: utf-8 -*-
from ssptransparencia.spiders.base import SsptransparenciaBaseSpider


class HomicidioDolosoSpider(SsptransparenciaBaseSpider):
    name = 'homicidio-doloso'
    first_lvl_link_css = '#cphBody_btnHomicicio'
