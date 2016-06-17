# -*- coding: utf-8 -*-
from os.path import join
from scrapy import signals
from scrapy.exporters import CsvItemExporter

from ssptransparencia.items import *


class SsptransparenciaExportPipeline(object):
    def __init__(self):
        self.files = []
        self.exporters = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        files = [
            ('bos', 'bos.csv'),
            ('vitimas', 'vitimas.csv'),
            ('naturezas', 'naturezas-envolvidas.csv'),
        ]
        for key, fname in files:
            file = open(join(spider.target_dir, fname), 'w+b')
            self.files.append(file)
            self.exporters[key] = CsvItemExporter(file)
            self.exporters[key].start_exporting()

    def spider_closed(self, spider):
        for exporter in self.exporters.values():
            exporter.finish_exporting()
        for file in self.files:
            file.close()

    def process_item(self, item, spider):
        key = None
        if isinstance(item, SsptransparenciaBO):
            key = 'bos'
        elif isinstance(item, SsptransparenciaVitima):
            key = 'vitimas'
        elif isinstance(item, SsptransparenciaNatureza):
            key = 'naturezas'
        assert key
        self.exporters[key].export_item(item)
        return item
