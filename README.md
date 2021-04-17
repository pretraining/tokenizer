# Tokenizer

Easy Korean subword tokenizer training tool

## Setup

### Prerequisites

- Python 3.7.9 environment (Recommendation)

```
pip install -r requirements.txt
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

```
python train.py
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
