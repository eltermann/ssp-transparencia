# -*- coding: utf-8 -*-
from ssptransparencia.spiders.base import SsptransparenciaBaseSpider


class OposicaoIntervencaoPolicialSpider(SsptransparenciaBaseSpider):
    name = 'oposicao-intervencao-policial'
    first_lvl_link_css = '#cphBody_btnMortePolicial'
