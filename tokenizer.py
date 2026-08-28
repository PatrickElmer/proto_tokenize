def tokenize(
    word: str,
    diacritics="̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ͜͡‿",
    proclitics="ˈˌ͜͡‿",
) -> list[str] | list:
    """Takes in a word as a string and returns its tokens as a list."""
    start = 0
    tokens = []

    for index, character in enumerate(word[1:], 1):
        if character not in diacritics and word[index - 1] not in proclitics:
            tokens.append(word[start:index])
            start = index
    tokens.append(word[start:])

    return tokens if word else []
