#!/usr/bin/env python.
# -*- coding: utf-8 -*-

"""
Word tokenizer
"""

__all__ = ['word_tokenize', 'compile_word_tokenizer_regex']
__since__ = '25.11.2020'
__version__ = '0.0.0.1'
__author__ = 'Apdullah Yayık <apdullahyayik@gmail.com>'

from typing import Tuple, Union, List

import re


def compile_word_tokenizer_regex():
    suffixes = r"[a-zğçşöüı]{3,}' ?[a-zğçşöüı]+"
    numbers = r"%\d{2,}[.,:/\d-]+"
    any_word = r"[a-zğçşöüı_+%\.()@&`’/\\\d-]+"
    punctuations = r"[a-zğçşöüı]*[,!?;:]"

    return re.compile(
        "|".join(
            [suffixes,
             numbers,
             any_word,
             punctuations
             ]
        ), re.I
    )


def word_tokenize(sentence: str, word_regex) -> Tuple:
    try:
        words: Union[List] = word_regex.findall(sentence)
    except (re.error, TypeError):
        return ()
    else:
        # If last word ends with dot, it should be another word
        words: Union[Tuple] = tuple(words)
        if words:
            end_dots = re.search(r'\b(\.+)$', words[-1])
            if end_dots:
                dots: str = end_dots.group(1)
                words = words[:-1] + (words[-1][:-len(dots)],) + (dots,)
        return words
