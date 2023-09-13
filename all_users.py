from data import analog_litter, matnie_words
from fuzzywuzzy import fuzz


def control_word(phrase):
    fragments = []
    phrase = phrase.lower().replace(" ", "")
    for key, value in analog_litter.items():
        for letter in value:
            for phr in phrase:
                if letter == phr:
                    phrase = phrase.replace(phr, key)

    all_fragments = []
    for word in matnie_words:
        for part in range(len(phrase)):
            fragment = phrase[part: part+len(word)]
            fragments.append(fragment)
        all_fragments.append(fragments)
        fragments = []

    counter = 0
    while counter < len(all_fragments):
        for fragment in all_fragments[counter]:
            if fuzz.ratio(matnie_words[counter], fragment) > 75:
                return 1
        counter += 1
    return 0

