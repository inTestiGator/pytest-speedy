"""This is undocumented"""

import operator


Dict = {"test1": 3, "test2": 2, "test3": 1}
# print(Dict)


def frequencies(word_list):
    """
    Takes a list of words and returns a dictionary associating
    words with frequencies of occurrence
    """
    word_freqs = {}
    for i in word_list:
        if i in word_freqs:
            word_freqs[i] += 1
        else:
            word_freqs[i] = 1
    return word_freqs


# pylint: disable=redefined-outer-name
def sort(Dict):
    """
    Takes a dictionary of timings and returns a list sorted by speed,
    in order from fastest to slowest.
    """
    return sorted(Dict.items(), key=operator.itemgetter(1))


print(sort(Dict))
