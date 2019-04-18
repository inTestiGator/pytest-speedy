#!/usr/bin/env python
"""
Compute term frequencies for an input file using a cookbook style
"""
import sys
import string

# The shared mutable data
# pylint: disable=invalid-name
data = []
words = []
word_freqs = []
#
# The Procedures
#


def read_file(path_to_file):
    """
    Takes a path to a file and assigns the entire
    contents of the file to the global variable data
    """
    # pylint: disable=global-statement
    global data
    with open(path_to_file) as data_file:
        data = data + list(data_file.read())


def filter_chars_and_normalize():
    """
    Replaces all non-alphanumeric chars in data with white space
    """
    # pylint: disable=global-statement
    global data
    # pylint: disable=consider-using-enumerate
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = " "
        else:
            data[i] = data[i].lower()


def scan():
    """
    Scans data for words, filling the global variable words
    """
    # pylint: disable=global-statement
    global data
    global words
    data_str = "".join(data)
    words = words + data_str.split()


def remove_stop_words():
    """
    Remove the stop words from the data file as we don't count them
    """
    # pylint: disable=global-statement
    global words
    with open("stopwords/stop_words.txt") as stop_file:
        stop_words = stop_file.read().split(",")
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    # pylint: disable=consider-using-enumerate
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)


def frequencies():
    """
    Creates a list of pairs associating
    words with frequencies
    """
    # pylint: disable=global-statement
    global words
    global word_freqs
    # iterate through all of the words
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])


def sort():
    """
    Sorts word_freqs by frequency
    """
    # pylint: disable=global-statement
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)


#
# The main funstion
#
if __name__ == "__main__":
    read_file(sys.argv[1])
    filter_chars_and_normalize()
    scan()
    remove_stop_words()
    frequencies()
    sort()

for tf in word_freqs[0:25]:
    print(tf[0], " - ", tf[1])
