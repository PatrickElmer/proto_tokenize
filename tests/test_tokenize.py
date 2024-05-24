from proto_tokenize import tokenize
import pytest


def test_empty_string():
    assert tokenize("") == []

def test_single_char():
    assert tokenize("a") == ["a"]

def test_short_word():
    assert tokenize("ab") == ["a", "b"]

def test_modifier():
    assert tokenize("aː") == ["aː"]

def test_combiner():
    assert tokenize("t͡s") == ["t͡s"]

def test_word_with_modifier():
    assert tokenize("maːm") == ["m", "aː", "m"]

def test_word_with_combiner():
    assert tokenize("at͡sa") == ["a", "t͡s", "a"]

def test_word_with_combiner_and_modifier():
    assert tokenize("at͡suːi") == ["a", "t͡s", "uː", "i"]

def test_missing_argument():
    with pytest.raises(TypeError):
        tokenize()
