def tokenize(
    word: str,
    diacritics="̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ͜͡‿",
    proclitics="ˈˌ͜͡‿",
) -> list[str] | list:
    """Takes in a word as a string and returns its tokens as a list."""
    segments, start, previous = [], 0, word[:1]

    for index, character in enumerate(word[1:], 1):
        if character not in diacritics and previous not in proclitics:
            segments.append(word[start:index])
            start = index
        previous = character
    segments.append(word[start:])

    return segments if word else []
