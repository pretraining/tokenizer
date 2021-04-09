import re
from typing import Dict, List

from konlpy.tag import Mecab
from kss import split_sentences

WHITESPACE = re.compile(r"\s+")


class WhitespacePreTokenizer:
    def __init__(self, apply_to="cbpe", input_key="text", output_key="text") -> None:
        self._input_key = input_key
        self._output_key = output_key
        self._target = apply_to
        self._split = WHITESPACE.split

    def pretokenize(self, string: str) -> List[str]:
        list_of_tokens = []
        list_of_sentences = split_sentences(string)

        if self._target == "bbpe":
            for sentence in list_of_sentences:
                list_of_eojeols: List[str] = self._split(sentence)

                for idx, eojeol in enumerate(list_of_eojeols):
                    if idx != 0:
                        list_of_tokens.append(" " + eojeol)
                    else:
                        list_of_tokens.append(eojeol)
        else:
            for sentence in list_of_sentences:
                list_of_tokens.extend(self._split(sentence))

        if list_of_tokens:
            return list_of_tokens
        else:
            return [""]

    def process(self, example: Dict[str, List[str]]) -> Dict[str, List[str]]:
        example[self._input_key] = self.pretokenize(example[self._input_key])
        return example


class MorphemePreTokenizer:
    def __init__(self, apply_to="cbpe", input_key="text", output_key="text") -> None:
        self._input_key = input_key
        self._output_key = output_key
        self._target = apply_to
        self._split = Mecab().morphs

    def pretokenize(self, string: str) -> List[str]:
        list_of_tokens = []
        list_of_sentences = split_sentences(string)

        if self._target == "bbpe":
            for sentence in list_of_sentences:
                list_of_eojeols: List[str] = WHITESPACE.split(sentence)

                for i, eojeol in enumerate(list_of_eojeols):
                    list_of_morphems = self._split(eojeol)

                    if i == 0:
                        for j, morpheme in enumerate(list_of_morphems):
                            list_of_tokens.append(morpheme)
                    else:
                        for j, morpheme in enumerate(list_of_morphems):
                            if j == 0:
                                list_of_tokens.append(" " + morpheme)
                            else:
                                list_of_tokens.append(morpheme)
        else:
            for sentence in list_of_sentences:
                list_of_tokens.extend(self._split(sentence))

        if list_of_tokens:
            return list_of_tokens
        else:
            return [""]

    def process(self, example: Dict[str, List[str]]) -> Dict[str, List[str]]:
        example[self._input_key] = self.pretokenize(example[self._input_key])
        return example
