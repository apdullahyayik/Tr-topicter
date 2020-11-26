#!/usr/bin/env python.
# -*- coding: utf-8 -*-

"""
Custom exceptions
"""

import inspect
import os

__all__ = ['short_descriptions', 'TrTopicterError', 'MLModelFileBrokenError', 'NonTurkishStringError',
           'MLModelNotExistError', 'get_line_info']
__version__ = '0.0.0.1'
__since__ = '25.11.2020'
__author__ = 'Apdullah Yayık <apdullahyayik@gmail.com>'

from typing import Union

short_descriptions = {
    1: "ML Model not exists, get request",
    2: "ML model file broken error, get request latest one",
    3: "Non-Turkish document is not supported"
}


class TrTopicterError(Exception):
    """
    Main project-based exception class
    """
    __slots__ = ['meta_data']

    def __init__(self, internal_detail: any = None):
        self.meta_data = get_line_info()
        self.meta_data['internal_detail'] = str(internal_detail)


class MLModelNotExistError(TrTopicterError):
    def __init__(self, internal_detail: any = None):
        super().__init__(internal_detail)
        self.meta_data['code'] = 1
        self.meta_data['short_description'] = short_descriptions[self.meta_data['code']]


class MLModelFileBrokenError(TrTopicterError):
    def __init__(self, internal_detail: any = None):
        super().__init__(internal_detail)
        self.meta_data['code'] = 2
        self.meta_data['short_description'] = short_descriptions[self.meta_data['code']]


class NonTurkishStringError(TrTopicterError):
    def __init__(self, internal_detail: any = None):
        super().__init__(internal_detail)
        self.meta_data['code'] = 3
        self.meta_data['short_description'] = short_descriptions[self.meta_data['code']]


def get_line_info(usage='exception') -> Union[str, dict]:
    frame = inspect.currentframe()
    if usage == 'logger':
        information = inspect.getframeinfo(frame.f_back)
        return ' - '.join(
            [
                os.path.basename(information.filename),
                information.function,
                str(information.lineno),
            ]
        )
    else:
        information = inspect.getframeinfo(frame.f_back.f_back.f_back.f_back)
        return {'line_number': information.lineno,
                'file_name': os.path.basename(information.filename),
                'function_name': information.function}
