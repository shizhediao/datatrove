import unittest

import trafilatura

from datatrove.pipeline.extractors import ReadabilityInscriptis, Trafilatura

from ..utils import require_inscriptis, require_readability, require_trafilatura


ARTICLE_HTML = "<html><body><article><p>Hello World!</p></article></body></html>"


class TestExtractors(unittest.TestCase):
    @require_trafilatura
    def test_basic_article_trafilatura(self):
        ZERO_CONFIG = trafilatura.settings.DEFAULT_CONFIG
        ZERO_CONFIG['DEFAULT']['MIN_EXTRACTED_SIZE'] = '0'
        extractor = Trafilatura(config=ZERO_CONFIG)
        self.assertEqual(extractor.extract(ARTICLE_HTML), "Hello World!")

    @require_readability
    @require_inscriptis
    def test_basic_article_readability(self):
        extractor = ReadabilityInscriptis(min_text_length=10, min_text_score=1)
        self.assertEqual(extractor.extract(ARTICLE_HTML), "Hello World!")
