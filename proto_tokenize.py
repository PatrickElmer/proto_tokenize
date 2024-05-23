"""Convert IPA transcribed words into sequence tokens."""


__version__ = "0.9.0"


def tokenize(
    word: str,
    combiners=set("͜͡‿"),
    modifiers=set("̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ"),
) -> tuple[str] | tuple:
    """Takes in a word as a string and returns its tokens as a tuple."""

    if not word:
        return ()

    tokenized = []
    start = 0

    Range = enumerate(word[1:], 1)
    for i, char in Range:
        if char in combiners:
            next(Range)
        elif char not in modifiers:
            tokenized.append(word[start:i])
            start = i
    tokenized.append(word[start:])

    return tuple(tokenized)
