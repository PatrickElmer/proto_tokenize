from tokenize import tokenize


def test_tokenize(benchmark):
    assert benchmark(tokenize, 'at͡suːi') == ('a', 't͡s', 'uː', 'i')
