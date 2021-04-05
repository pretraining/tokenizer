import os
from pathlib import Path

from src.utils import extract_filepath_from_dir


def test_extract_filepath_from_dir():
    mock_dir = Path.cwd() / "mock"

    if not mock_dir.exists():
        mock_dir.mkdir(parents=True)
        mock_file = mock_dir / "mock.json"
        mock_file.touch()

    assert len(extract_filepath_from_dir(mock_dir)) == 1

    os.remove(mock_file)
    os.rmdir(mock_dir)
