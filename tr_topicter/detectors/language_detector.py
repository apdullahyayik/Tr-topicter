#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Language Identification Model

Don't forget to comment line below at load_model function in FastText.py to silence warning
    eprint("Warning : `load_model` does not return WordVectorModel
"""

import os
import re
from typing import Tuple, Optional

from detectors import _load_model
from exceptions import MLModelNotExistError, MLModelFileBrokenError

__all__ = ['LanguageDetector']
__version__ = '0.0.0.1'
__author__ = 'Apdullah Yayık <apdullah.yayik@gmail.com>'
__since__ = '25.11.2020'


class LanguageDetector:
    __slots__ = ['probability_threshold', 'model']

    def __init__(self, ml_model_path: str, probability_threshold: float):
        probability_threshold = min(probability_threshold, 1)
        self.probability_threshold = max(probability_threshold, 0)

        if not os.path.isfile(ml_model_path):
            raise MLModelNotExistError(ml_model_path)

        try:
            self.model = _load_model(ml_model_path)
        except Exception:
            raise MLModelFileBrokenError(ml_model_path)

    @staticmethod
    def __clean(text: str) -> str:
        # remove punctuation
        from string import punctuation
        text = text.translate(str.maketrans('', '', punctuation))

        # remove numbers
        text = re.sub(r"\d", "", text)

        # remove whitespaces and return lower-case
        text = re.sub(r'[\n\t]', ' ', text)
        return re.sub(r' +', ' ', text.lower())

    def predict_language(self, text: str, number_of_output: Optional[int] = None,
                         reduction_fold: Optional[int] = None) -> Optional[dict]:
        if number_of_output is None:
            number_of_output = 1
        if reduction_fold is None:
            reduction_fold = 1
        probability_threshold = self.probability_threshold / reduction_fold
        if not text.strip():
            prediction = ([], ())
        else:
            try:
                prediction = self.model.predict(self.__clean(text),
                                                k=number_of_output,
                                                threshold=probability_threshold)
            except TypeError:
                prediction = ([], ())
        return self.__format_prediction(prediction, probability_threshold)

    @staticmethod
    def __format_prediction(prediction: Tuple, probability_threshold: float) -> Optional[dict]:
        label, probability = prediction
        if len(label) != 1 or len(probability) != 1:
            return None
        if isinstance(probability[0], float):
            probability_value = probability[0]
            if probability_value > probability_threshold:
                if isinstance(label[0], str):
                    label_regex = re.match(pattern=r'__label__([a-z]{2,3})', string=label[0])
                    if label_regex:
                        return {'label': label_regex.group(1), 'probability': probability_value}
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None

    def __repr__(self):
        return '<LanguageDetector> object dedicated to load machine learning models and provide predictions'
