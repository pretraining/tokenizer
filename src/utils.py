from pathlib import Path
from typing import Generator, List, Union

import datasets


def extract_filepath_from_dir(
    dirpath: Union[Path, str], ext: str = "json"
) -> List[str]:
    if isinstance(dirpath, str):
        dirpath = Path(dirpath)

    list_of_filepath = []
    for filepath in dirpath.iterdir():
        if filepath.is_dir():
            list_of_filepath.extend((str(_) for _ in filepath.glob(f"*.{ext}")))
        elif filepath.suffix == f".{ext}":
            list_of_filepath.append(str(filepath))
    return list_of_filepath


def convert_to_token_generator(
    preprocessed_corpus: datasets.arrow_dataset.Dataset,
    key: str = "text",
) -> Generator[str, None, None]:
    preprocessed_corpus_iterator = iter(preprocessed_corpus)

    for item in preprocessed_corpus_iterator:
        list_of_tokens = item[key]
        yield from list_of_tokens
