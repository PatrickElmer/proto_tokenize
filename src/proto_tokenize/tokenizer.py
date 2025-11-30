def tokenize(
    word: str,
    combiners=set("͜͡‿"),
    modifiers=set("̥̬̊ʰ̹̜̟̠̩̯̈̽˞̤̰̼ʷʲˠˤ̴̝̞̘̙̪̺̻̃ⁿˡ̚ːˑ̆̋˥́˦̄˧̀˨̏˩ꜜꜛ̌̂᷄᷅᷈↗↘ʱʳʴʵʶˀ̢᷆᷇᷉ʼ"),
    stresses=set("ˈˌ"),
) -> list[str] | list:
    """Takes in a word as a string and returns its tokens as a list."""
    if not word:
        return []

    bounds = [0] + [
        i for i in range(1, len(word))
        if word[i] not in combiners | modifiers
        and word[i - 1] not in combiners | stresses
    ] + [len(word)]

    return [word[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]
