def tokenize(
    word: str,
    combiners=set("͜͡‿"),
    modifiers=set("̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ"),
    stresses=set("ˈˌ"),
) -> list[str] | list:
    """Takes in a word as a string and returns its tokens as a list."""

    if not word:
        return []

    tokenized = []
    start = 0

    Range = enumerate(word[1:], 1)
    for i, char in Range:
        if char in combiners:
            next(Range)
        elif char not in modifiers and not word[i-1] in stresses:
            tokenized.append(word[start:i])
            start = i
    tokenized.append(word[start:])

    return tokenized
