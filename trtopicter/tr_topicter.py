import os
import re
from json import load

from .detectors.domain_detector import DomainDetector
from .detectors.language_detector import LanguageDetector
from .exceptions import NonTurkishStringError
from .tokenizer import compile_word_tokenizer_regex

__all__ = ['TrTopicter']
__version__ = '0.0.0.1'
__author__ = 'Apdullah Yayık <apdullah.yayik@gmail.com>'
__since__ = '25.11.2020'


class TrTopicter:
    __slots__ = ('language_detection_model', 'domain_detection_model', 'text', 'parameters')

    def __init__(self):
        this_directory = os.path.abspath(os.path.dirname(__file__))
        self.parameters = self.__read_params(os.path.join(this_directory,'./configuration.json'))
        language_probability_threshold = self.parameters['LANGUAGE_IDENTIFICATION']['probability_threshold']
        self.language_detection_model = LanguageDetector(os.path.join(this_directory,'models/language/lid.176.ftz'),
                                                         language_probability_threshold)
        domain_probability_threshold = self.parameters['DOMAIN_DETECTION']['probability_threshold']
        word_tokenizer_pre_compiled_regex = compile_word_tokenizer_regex()
        stop_words = self.__read_stop_words(os.path.join(this_directory,'stop_words/tr_stop_words'))
        self.domain_detection_model = DomainDetector(os.path.join(this_directory,'models/domain_detector/tr_domain_data.lite'),
                                                     domain_probability_threshold,
                                                     word_tokenizer_pre_compiled_regex,
                                                     stop_words)

    @staticmethod
    def __read_stop_words(stop_word_file_path):
        stop_words = set()
        with open(stop_word_file_path, 'r', encoding='utf-8') as fp:
            for line in fp:
                stop_words.add(re.sub(r'\n', '', line))
        return stop_words

    @staticmethod
    def __read_params(params: str):
        with open(params, 'r', encoding='utf-8') as f:
            parameters = load(f)
        return parameters

    def get_topic(self, text):
        if not isinstance(text, str):
            raise TypeError('text should be given as string')
        language_info = self.language_detection_model.predict_language(text)

        if language_info:
            if language_info['label'] == 'tr':
                domain_info = self.domain_detection_model.predict_domain(
                    text, self.parameters['DOMAIN_DETECTION']['limit']['character'] * 0.8
                )
                if domain_info:
                    return domain_info
                else:
                    return None
        raise NonTurkishStringError

    def __repr__(self):
        return '<TrTopicter> object dedicated to load machine learning models and provide predictions'
