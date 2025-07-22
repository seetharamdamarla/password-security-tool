import itertools

LEET_DICT = {'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['$', '5']}

def leetspeak(word):
    combos = [[char] + LEET_DICT.get(char.lower(), []) for char in word]
    return {''.join(x) for x in itertools.product(*combos)}
