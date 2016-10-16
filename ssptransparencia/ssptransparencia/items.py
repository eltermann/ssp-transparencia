# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class SsptransparenciaBO(scrapy.Item):
    id = scrapy.Field()
    nav_natureza = scrapy.Field()
    nav_ano = scrapy.Field()
    nav_mes = scrapy.Field()
    nav_menu_adicional = scrapy.Field()
    tabela_numero_bo = scrapy.Field()
    tabela_tipo_bo = scrapy.Field()
    tabela_cidade = scrapy.Field()
    tabela_delegacia_elaboracao = scrapy.Field()
    tabela_data_fato = scrapy.Field()
    tabela_data_registro = scrapy.Field()
    tabela_endereco_fato = scrapy.Field()
    bo_dependencia = scrapy.Field()
    bo_numero = scrapy.Field()
    bo_iniciado = scrapy.Field()
    bo_emitido = scrapy.Field()
    bo_autoria = scrapy.Field()
    bo_complementar_ao_rdo = scrapy.Field()
    bo_desdobramentos = scrapy.Field()
    bo_local_linha1 = scrapy.Field()
    bo_local_linha2 = scrapy.Field()
    bo_tipo_local = scrapy.Field()
    bo_circunscricao = scrapy.Field()
    bo_ocorrencia = scrapy.Field()
    bo_comunicacao = scrapy.Field()
    bo_elaboracao = scrapy.Field()
    bo_flagrante = scrapy.Field()
    bo_exames_requisitados = scrapy.Field()
    bo_solucao = scrapy.Field()
    bo_numero_naturezas = scrapy.Field()
    bo_numero_vitimas = scrapy.Field()


class SsptransparenciaNatureza(scrapy.Item):
    bo_id = scrapy.Field()
    count = scrapy.Field()
    especie = scrapy.Field()
    linha1 = scrapy.Field()
    linha2 = scrapy.Field()


class SsptransparenciaVitima(scrapy.Item):
    bo_id = scrapy.Field()
    count = scrapy.Field()
    nome = scrapy.Field()
    autor_vitima = scrapy.Field()
    tipo = scrapy.Field()
    rg = scrapy.Field()
    natural_de = scrapy.Field()
    nacionalidade = scrapy.Field()
    sexo = scrapy.Field()
    nascimento = scrapy.Field()
    idade = scrapy.Field()
    estado_civil = scrapy.Field()
    profissao = scrapy.Field()
    instrucao = scrapy.Field()
    cutis = scrapy.Field()
    naturezas_envolvidas = scrapy.Field()


def map_month(s):
    month = s.lower()
    month = month[:3]
    _m = dict(jan=1, fev=2, mar=3, abr=4, mai=5, jun=6,
              jul=7, ago=8, set=9, out=10, nov=11, dez=12)
    return _m[month]


class SsptransparenciaBOLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(unicode.strip)

    nav_ano_in = MapCompose(unicode.strip, int)
    nav_mes_in = MapCompose(unicode.strip, map_month)
    bo_numero_naturezas_in = MapCompose(unicode.strip, int)
    bo_numero_vitimas_in = MapCompose(unicode.strip, int)


class SsptransparenciaNaturezaLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(unicode.strip)

    count_in = MapCompose(int)


class SsptransparenciaVitimaLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(unicode.strip)

    count_in = MapCompose(int)
