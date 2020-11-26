import os
import re
from string import punctuation
from typing import Optional, Tuple

from . import _load_model
from ..exceptions import MLModelNotExistError, MLModelFileBrokenError
from ..tokenizer import word_tokenize

__all__ = ['DomainDetector']
__version__ = '0.0.0.1'
__author__ = 'Apdullah Yayık <apdullah.yayik@gmail.com>'
__since__ = '25.11.2020'

TR_TO_ENG = {
    'siyaset': 'politics',
    'dunya': 'world',
    'ekonomi': 'economy',
    'saglik': 'health',
    'spor': 'sport',
    'teknoloji': 'technology',
    'kultur': 'culture',
    'religion': 'religion',
    'education': 'education',
}


class UnicodeTr(str):
    CHAR_MAP = {
        "to_lower": {
            u"I": u"ı",
            u"İ": u"i",
        }
    }

    def lower(self):
        for key, value in self.CHAR_MAP['to_lower'].items():
            self = self.replace(key, value)
        return self.lower()


class DomainDetector:
    __slots__ = ('stop_words', 'word_tokenizer_pre_compiled_regex', 'probability_threshold', 'model')

    def __init__(self, ml_model_path: str,
                 probability_threshold: float,
                 word_tokenizer_pre_compiled_regex,
                 stop_words=None):
        self.stop_words = stop_words
        self.word_tokenizer_pre_compiled_regex = word_tokenizer_pre_compiled_regex
        probability_threshold = min(probability_threshold, 1)
        self.probability_threshold = max(probability_threshold, 0)

        if not os.path.isfile(ml_model_path):
            raise MLModelNotExistError(ml_model_path)

        try:
            self.model = _load_model(ml_model_path)
        except Exception:
            raise MLModelFileBrokenError(ml_model_path)

    def __clean(self, line: str):

        # normalization (lower case, punctuation, numbers, white space)
        line = line.translate(str.maketrans('', '', punctuation))
        line = re.sub(r'( +)|([\d\n])', ' ', UnicodeTr(line).lower().strip())

        # stop words removal
        if self.stop_words:
            line_words = word_tokenize(line, self.word_tokenizer_pre_compiled_regex)
            line_words = [word for word in line_words if word not in self.stop_words]
            return ' '.join(line_words)
        else:
            return line

    def predict_domain(self, text: str, character_limit: int, number_of_output: Optional[int] = None) -> Optional[dict]:

        if number_of_output is None:
            number_of_output = 1
        clean_text = self.__clean(text)
        if not len(clean_text) > character_limit * 0.8:
            prediction = ([], ())
        else:
            try:
                prediction = self.model.predict(clean_text,
                                                k=number_of_output,
                                                threshold=self.probability_threshold)
            except TypeError:
                prediction = ([], ())

        return self.__format_prediction(prediction, self.probability_threshold)

    @staticmethod
    def __format_prediction(prediction: Tuple, probability_threshold: float) -> Optional[dict]:
        label, probability = prediction
        if len(label) != 1 or len(probability) != 1:
            return None
        if isinstance(probability[0], float):
            probability_value = probability[0]
            if probability_value > probability_threshold:
                if isinstance(label[0], str):
                    label_regex = re.match(pattern=r'__label__([a-z]*)', string=label[0])
                    if label_regex:
                        probability_value = min(1.00, probability_value)
                        return {'label': TR_TO_ENG[label_regex.group(1)],
                                'probability': probability_value}
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None

    def __repr__(self):
        return '<DomainDetector> object dedicated to load machine learning models and provide predictions'
