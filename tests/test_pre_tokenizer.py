from src.pre_tokenizer import WhitespacePreTokenizer


def test_WhitespacePreTokenizer():
    test_case01 = "안녕하세요, 제 이름은 김보섭입니다."
    test_case02 = "안녕하세요."
    test_case03 = ""

    pretokenizer_for_cbpe = WhitespacePreTokenizer(target="cbpe")
    assert pretokenizer_for_cbpe.pretokenize(test_case01) == [
        "안녕하세요,",
        "제",
        "이름은",
        "김보섭입니다.",
    ]
    assert pretokenizer_for_cbpe.pretokenize(test_case02) == ["안녕하세요."]
    assert pretokenizer_for_cbpe.pretokenize(test_case03) == [""]
    assert pretokenizer_for_cbpe.process({"text": test_case01}) == {
        "text": ["안녕하세요,", "제", "이름은", "김보섭입니다."]
    }
    assert pretokenizer_for_cbpe.process({"text": test_case02}) == {"text": ["안녕하세요."]}
    assert pretokenizer_for_cbpe.process({"text": test_case03}) == {"text": [""]}

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
