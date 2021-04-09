import os
from pathlib import Path

from datasets import Dataset

from src.utils import convert_to_token_generator, extract_filepath_from_dir


def test_extract_filepath_from_dir():
    mock_dir = Path.cwd() / "mock"

    if not mock_dir.exists():
        mock_dir.mkdir(parents=True)
        mock_file = mock_dir / "mock.json"
        mock_file.touch()

    assert len(extract_filepath_from_dir(mock_dir)) == 1

    os.remove(mock_file)
    os.rmdir(mock_dir)


def test_convert_to_token_generator():
    mock_data = {"text": [["안녕하세요,", "제", "이름은", "김보섭입니다."], ["안녕하세요."]]}

    test_dataset = Dataset.from_dict(mock_data)
    test_gen = convert_to_token_generator(test_dataset, "text")

    list_of_tokens = []

    for token in test_gen:
        list_of_tokens.append(token)

    assert ["안녕하세요,", "제", "이름은", "김보섭입니다.", "안녕하세요."] == list_of_tokens
