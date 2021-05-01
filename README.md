# Tokenizer

Easy Korean subword tokenizer training tool

## Setup

### Prerequisites

- Python 3.7.9 environment (Recommendation)

```bash
pip install -r requirements.txt
sudo apt-get install curl git # Ubuntu
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

## Train

### Configurations

#### common configs

```
- version
- corpus 
    |- dirpath: corpus data directory 
    |- extension: data file extension
    |- sampling ratio: data sampling ratio
- dataset 
    |- num_workers: number of processors to preprocess
- defaults
    |- pre_tokenizer: select pre-tokenizer options (each tokenizer names are in `conf/pre_tokenizer`)
    |- subword_tokenizer: select subword tokenizer (each tokenizer names are in `conf/subword_tokenizer`)
```

### Run
- Train `CharBPETokenizer` from tokens which are split by whitespace
  ```bash
  $ python train.py tokenizer=cbpe_whitespace
  ```

- Train `CharBPETokenizer` from tokens which are split by morpheme-analyzer (`Mecab`)
  ```bash
  $ python train.py tokenizer=cbpe_morpheme
  ```

- Train `ByteLevelBPETokenizer` from tokens which are split by whitespace
  ```bash
  $ python train.py tokenizer=bbpe_whitespace
  ```

- Train `ByteLevelBPETokenizer` from tokens which are split by morpheme-analyzer (`Mecab`)
  ```bash
  $ python train.py tokenizer=bbpe_morpheme
  ```

- Train `BertWordPieceTokenizer` from tokens which are split by whitespace
  ```bash
  $ python train.py tokenizer=wp_whitespace
  ```

- Train `BertWordPieceTokenizer` from tokens which are split by morpheme-analyzer (`Mecab`)
  ```bash
  $ python train.py tokenizer=wp_morpheme
  ```

You can see all valid arguments of `train.py` below command.

```bash
$ python train.py --help
```

```bash
== Configuration groups ==
Compose your configuration from those groups (group=option)

tokenizer: bbpe_morpheme, bbpe_whitespace, cbpe_morpheme, cbpe_whitespace, wp_morpheme, wp_whitespace

== Config ==
Override anything in the config (foo.bar=value)

version: v00
corpus:
  dirpath: null
  extension: txt
  sampling_ratio: 0.01
datasets:
  num_workers: 4
tokenizer:
  subword_tokenizer:
    init:
      _target_: tokenizers.CharBPETokenizer
      suffix: </w>
      dropout: null
      lowercase: false
      unicode_normalizer: null
      bert_normalizer: true
      split_on_whitespace_only: false
    train:
      vocab_size: 3000
      min_frequency: 2
      special_tokens:
      - <unk>
      limit_alphabet: 1000
      initial_alphabet: []
      suffix: </w>
      show_progress: true
  pre_tokenizer:
    _target_: src.pre_tokenizer.MorphemePreTokenizer
    apply_to: cbpe
    input_key: text
    output_key: text
```

## Contribution

Your contribution is always welcome. If you want to contribute something on our project, please follow these guidelines below.

### Guidelines

1. Leave your issue on github
2. Apply custom gitmessage and install pre-commit
3. Craate a branch for your issue and edit your codes
4. Do commit and push to github

### How to apply custom gitmessage

```bash
$ make set-git
```

### Commit rule
- [언어] 타입: 꼬릿말 | 파이썬 파일의 경우 [언어] 생략
- ex) .py 파일의 경우, feat: Add tokenizer utils
- ex) 그 외, [shell] feat: Add git action script

### How to use pre-commit
#### Installation
```bash
$ make all
```

#### Execution
```bash
$ make check
```
