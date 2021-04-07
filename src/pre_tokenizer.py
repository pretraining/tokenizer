import re
from typing import Dict, List

from kss import split_sentences

WHITESPACE = re.compile(r"\s+")


class WhitespacePreTokenizer:
    def __init__(self, target="cbpe", input_key="text", output_key="text") -> None:
        self._input_key = input_key
        self._output_key = output_key
        self._target = target

    def pretokenize(self, string: str) -> List[str]:
        list_of_tokens = []
        list_of_sentences = split_sentences(string)

        for sentence in list_of_sentences:
            if self._target == "bbpe":
                list_of_footprints: List[str] = WHITESPACE.split(sentence)

                for idx, footprint in enumerate(list_of_footprints):
                    if idx != 0:
                        list_of_tokens.append(" " + footprint)
                    else:
                        list_of_tokens.append(footprint)
            else:
                list_of_tokens.extend(WHITESPACE.split(sentence))

        if list_of_tokens:
            return list_of_tokens
        else:
            return [""]

    def process(self, example: Dict[str, List[str]]) -> Dict[str, List[str]]:
        example[self._input_key] = self.pretokenize(example[self._input_key])
        return example
