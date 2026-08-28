from collections.abc import Container


def tokenize(
    word: str,
    diacritics: Container[str] = "̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ͜͡‿",
    proclitics: Container[str] = "ˈˌ͜͡‿",
) -> list[str]:
    """Split a phonetic word into segments.

    A segment starts at each character that is not in `diacritics`,
    unless the character before it is in `proclitics`. The first
    character always starts a segment.

    `diacritics` never start a segment. They belong to the character on
    their left, like a length mark. `proclitics` claim the character on
    their right, like a stress mark. Tie bars go in both, because they
    bind both ways.

    The segments join back into `word`. An empty word gives an empty
    list.
    """
    segments, start, previous = [], 0, word[:1]

    for index, character in enumerate(word[1:], 1):
        if character not in diacritics and previous not in proclitics:
            segments.append(word[start:index])
            start = index
        previous = character
    segments.append(word[start:])

    return segments if word else []
