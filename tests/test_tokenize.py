from proto_tokenize import tokenize


def test_tokenize():
    assert tokenize('at͡suːi') == ('a', 't͡s', 'uː', 'i')
