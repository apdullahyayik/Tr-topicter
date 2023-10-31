# 🔍 TrTopicter

A simple topic detector.

[![Python Version](https://img.shields.io/pypi/pyversions/trtopicter.svg?style=for-the-badge)](https://pypi.org/project/trtopicter/)
[![PyPI Version](https://img.shields.io/pypi/v/trtopicter.svg?style=for-the-badge)](https://pypi.org/project/trtopicter/)

## Overview

**TrTopicter** is a pre-built package equipped with a machine learning model designed to detect the topics of Turkish textual content. The language of the text is first identified to avoid analyzing non-Turkish text, which could lead to inaccurate results. The deployed model has been trained on nearly 30,000 annotated Turkish sentences/paragraphs, achieving an average F-1 score of 94.37%. The execution time for analyzing text with over 300 characters is less than 1 ms, and resource usage is only 6 MB.

## Installation

You can easily install **TrTopicter** via PyPI. It has been tested on Windows 8/10, Ubuntu 18.04/20.04, and macOS Catalina 10.15.7.

```sh
pip install trtopicter
```

## Supported Topics

- **politics**
- **economy**
- **health**
- **sport**
- **technology**
- **culture**
- **religion**
- **justice**

## Pre-processing

Text preprocessing includes:

- Case-folding to lowercase
- Punctuation, numbers, and white space removal
- Stop words removal (Credits: [Zemberek-NLP](https://github.com/ahmetaa/zemberek-nlp/blob/master/experiment/src/main/resources/stop-words.tr.txt))

## Configuration

```json
{
  "LANGUAGE_IDENTIFICATION": {
    "limit": {
      "character": 500
    },
    "probability_threshold": 0.2
  },
  "DOMAIN_DETECTION": {
    "limit": {
      "character": 500
    },
    "probability_threshold": 0.5
  }
}
```

- `character`: Number of characters threshold for detection (data type: integer).
- `probability_threshold`: Probability threshold for detection (data type: float).

## Usage

You can use the **TrTopicter** package to determine the topic of Turkish text easily:

```python
from trtopicter import TrTopicter

topicter = TrTopicter()

result = topicter.get_topic("Your Turkish text goes here.")

print(result)
```

## To-do List

Our to-do list includes:

- Expanding the number of supported topics
- Adding Cython support

## Additional Resources

Explore more about natural language processing and related topics:

- [Fasttext](https://arxiv.org/abs/1607.01759)
- [Topic Classification Survey](https://arxiv.org/abs/2004.03705)
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
- [Bogazici University CMPE-561](https://www.cmpe.boun.edu.tr/tr/courses/cmpe561)
