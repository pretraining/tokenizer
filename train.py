from pathlib import Path

import hydra
from datasets import load_dataset
from hydra.utils import instantiate, to_absolute_path
from numpy.random import choice
from omegaconf import DictConfig, OmegaConf

from src.utils import convert_to_token_generator, extract_filepath_from_dir


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    assert cfg.corpus.sampling_ratio > 0.0 and cfg.corpus.sampling_ratio <= 1.0

    list_of_filepath = extract_filepath_from_dir(
        dirpath=cfg.corpus.dirpath, ext=cfg.corpus.extension
    )

    corpus = load_dataset(
        path="json",
        data_files=list_of_filepath,
        split="train",
    )
    preprocessed_corpus = corpus

    if cfg.corpus.sampling_ratio < 1.0:
        total_size = len(preprocessed_corpus)
        sample_size = int(total_size * cfg.corpus.sampling_ratio)

        preprocessed_corpus = preprocessed_corpus.select(
            indices=choice(range(total_size), sample_size)
        )

    pre_tokenizer = instantiate(cfg.tokenizer.pre_tokenizer)

    preprocessed_corpus = preprocessed_corpus.map(
        pre_tokenizer.process, num_proc=cfg.datasets.num_workers
    )

    gen = convert_to_token_generator(
        preprocessed_corpus, cfg.tokenizer.pre_tokenizer.output_key
    )

    subword_tokenizer = instantiate(cfg.tokenizer.subword_tokenizer.init)
    subword_tokenizer.train_from_iterator(
        gen, **OmegaConf.to_container(cfg.tokenizer.subword_tokenizer.train)
    )

    vocab_dir = Path(to_absolute_path("vocab"))

    if not vocab_dir.exists():
        vocab_dir.mkdir(parents=True)

    save_dir = vocab_dir / cfg.version / cfg.tokenizer.pre_tokenizer.apply_to

    if not save_dir.exists():
        save_dir.mkdir(parents=True)
    subword_tokenizer.save_model(str(save_dir))
    OmegaConf.save(cfg.tokenizer, save_dir / "config.yaml")


if __name__ == "__main__":
    main()
