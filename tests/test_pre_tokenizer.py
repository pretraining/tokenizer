from src.pre_tokenizer import MorphemePreTokenizer, WhitespacePreTokenizer


def test_WhitespacePreTokenizer():
    test_case01 = "안녕하세요, 제 이름은 김보섭입니다."
    test_case02 = "안녕하세요."
    test_case03 = ""

    pretokenizer_not_bbpe = WhitespacePreTokenizer(target="cbpe")
    assert pretokenizer_not_bbpe.pretokenize(test_case01) == [
        "안녕하세요,",
        "제",
        "이름은",
        "김보섭입니다.",
    ]
    assert pretokenizer_not_bbpe.pretokenize(test_case02) == ["안녕하세요."]
    assert pretokenizer_not_bbpe.pretokenize(test_case03) == [""]
    assert pretokenizer_not_bbpe.process({"text": test_case01}) == {
        "text": ["안녕하세요,", "제", "이름은", "김보섭입니다."]
    }
    assert pretokenizer_not_bbpe.process({"text": test_case02}) == {"text": ["안녕하세요."]}
    assert pretokenizer_not_bbpe.process({"text": test_case03}) == {"text": [""]}

    pretokenizer_for_bbpe = WhitespacePreTokenizer(target="bbpe")
    assert pretokenizer_for_bbpe.pretokenize(test_case01) == [
        "안녕하세요,",
        "제",
        " 이름은",
        " 김보섭입니다.",
    ]
    assert pretokenizer_for_bbpe.pretokenize(test_case02) == ["안녕하세요."]
    assert pretokenizer_for_bbpe.pretokenize(test_case03) == [""]
    assert pretokenizer_for_bbpe.process({"text": test_case01}) == {
        "text": ["안녕하세요,", "제", " 이름은", " 김보섭입니다."]
    }
    assert pretokenizer_for_bbpe.process({"text": test_case02}) == {"text": ["안녕하세요."]}
    assert pretokenizer_for_bbpe.process({"text": test_case03}) == {"text": [""]}


def test_MorphemePreTokenizer():
    test_case01 = "안녕하세요, 제 이름은 김보섭입니다."
    test_case02 = "안녕하세요."
    test_case03 = ""

    pretokenizer_not_bbpe = MorphemePreTokenizer(target="cbpe")
    assert pretokenizer_not_bbpe.pretokenize(test_case01) == [
        "안녕",
        "하",
        "세요",
        ",",
        "제",
        "이름",
        "은",
        "김보섭",
        "입니다",
        ".",
    ]
    assert pretokenizer_not_bbpe.pretokenize(test_case02) == ["안녕", "하", "세요", "."]
    assert pretokenizer_not_bbpe.pretokenize(test_case03) == [""]
    assert pretokenizer_not_bbpe.process({"text": test_case01}) == {
        "text": ["안녕", "하", "세요", ",", "제", "이름", "은", "김보섭", "입니다", "."]
    }
    assert pretokenizer_not_bbpe.process({"text": test_case02}) == {
        "text": ["안녕", "하", "세요", "."]
    }
    assert pretokenizer_not_bbpe.process({"text": test_case03}) == {"text": [""]}

    pretokenizer_for_bbpe = MorphemePreTokenizer(target="bbpe")
    assert pretokenizer_for_bbpe.pretokenize(test_case01) == [
        "안녕",
        "하",
        "세요",
        ",",
        "제",
        " 이름",
        "은",
        " 김보섭",
        "입니다",
        ".",
    ]
    assert pretokenizer_for_bbpe.pretokenize(test_case02) == ["안녕", "하", "세요", "."]
    assert pretokenizer_for_bbpe.pretokenize(test_case03) == [""]
    assert pretokenizer_for_bbpe.process({"text": test_case01}) == {
        "text": ["안녕", "하", "세요", ",", "제", " 이름", "은", " 김보섭", "입니다", "."]
    }
    assert pretokenizer_for_bbpe.process({"text": test_case02}) == {
        "text": ["안녕", "하", "세요", "."]
    }
    assert pretokenizer_for_bbpe.process({"text": test_case03}) == {"text": [""]}
