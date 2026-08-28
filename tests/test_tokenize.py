import pytest

from tokenizer import tokenize


def test_empty_string():
    assert tokenize("") == []


def test_single_char():
    assert tokenize("a") == ["a"]


def test_short_word():
    assert tokenize("ab") == ["a", "b"]


def test_diacritic():
    assert tokenize("aː") == ["aː"]


def test_tie_bar():
    assert tokenize("t͡s") == ["t͡s"]


def test_word_with_diacritic():
    assert tokenize("maːm") == ["m", "aː", "m"]


def test_word_with_tie_bar():
    assert tokenize("at͡sa") == ["a", "t͡s", "a"]


def test_word_with_tie_bar_and_diacritic():
    assert tokenize("at͡suːi") == ["a", "t͡s", "uː", "i"]


def test_stress():
    assert tokenize("ˈaˌb") == ["ˈa", "ˌb"]


def test_prenasalized():
    assert tokenize("aᵐ͡ba") == ["a", "ᵐ͡b", "a"]


def test_wrong_prenasalization_if_nasal_is_a_diacritic():
    assert tokenize("aⁿ͡ta") == ["aⁿ͡t", "a"]
    assert tokenize("aⁿ͡ta", diacritics="͡") == ["a", "ⁿ͡t", "a"]


def test_custom_diacritic():
    assert tokenize("ts", diacritics="s") == ["ts"]


def test_custom_tie_bar():
    assert tokenize("a-b", diacritics="-", proclitics="-") == ["a-b"]


def test_tie_bar_must_be_in_both_arguments_to_bind_both_ways():
    assert tokenize("a-b", diacritics="-") == ["a-", "b"]
    assert tokenize("a-b", proclitics="-") == ["a", "-b"]


def test_any_container_of_characters_is_accepted():
    assert tokenize("ts", diacritics="s") == ["ts"]
    assert tokenize("ts", diacritics={"s"}) == ["ts"]
    assert tokenize("ts", diacritics=["s"]) == ["ts"]
    assert tokenize("ts", diacritics=frozenset("s")) == ["ts"]


def test_missing_argument():
    with pytest.raises(TypeError):
        tokenize()


def test_trailing_tie_bar():
    assert tokenize("at͡") == ["a", "t͡"]


def test_leading_tie_bar():
    assert tokenize("͡ab") == ["͡a", "b"]


def test_leading_diacritic():
    assert tokenize("ːa") == ["ː", "a"]


def test_trailing_stress():
    assert tokenize("aˈ") == ["a", "ˈ"]


def test_lone_stress():
    assert tokenize("ˈ") == ["ˈ"]


def test_doubled_stress():
    assert tokenize("ˈˈa") == ["ˈˈa"]
