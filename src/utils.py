from pathlib import Path
from typing import List, Union


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
