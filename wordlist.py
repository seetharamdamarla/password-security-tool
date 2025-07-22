import itertools
from utils import leetspeak

def generate_wordlist(name, dob, pet, fav):
    base_words = {name, dob, pet, fav}
    patterns = set()
    special_suffixes = ["123", "@2025", "!", "@", "#"]
    years = {dob, dob[-2:], dob[:2]} if dob else set()

    for word in base_words:
        word = word.strip()
        if not word:
            continue

        leet_variants = leetspeak(word)
        all_variants = {word, word.lower(), word.upper(), word.capitalize()} | leet_variants

        for variant in all_variants:
            patterns.add(variant)
            for suffix in special_suffixes:
                patterns.add(variant + suffix)
            for prefix in special_suffixes:
                patterns.add(prefix + variant)

    # Add year-based combos
    for variant in patterns.copy():
        for year in years:
            patterns.add(variant + year)
            patterns.add(year + variant)

    # Combine patterns (2-word combos)
    combinations = set()
    for a, b in itertools.combinations(patterns, 2):
        combinations.add(a + b)
        combinations.add(b + a)

    return list(patterns.union(combinations))

def save_wordlist(wordlist, path):
    with open(path, "w") as f:
        for word in wordlist:
            f.write(word + "\n")
