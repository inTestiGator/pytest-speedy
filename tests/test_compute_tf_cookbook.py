"""Test cases for the module that uses a cookbook programming style"""

# import datetime
# import pytest
from termfrequency import compute_tf_cookbook

# # use "pipenv run pytest -s" to run this fixture
# @pytest.fixture(autouse=True)
# def test_check_duration(request, cache):
#     """ Docstring """
#     print("this is check duration")
#     key = "duration/" + request.node.nodeid.replace(";", "_")
#     # nodeid's can have colons
#     # keys become filenames within .cache
#     # replace colons with something filename safe
#     start_time = datetime.datetime.now()
#     # yield
#     stop_time = datetime.datetime.now()
#     this_duration = (stop_time - start_time).total_seconds()
#     #     last_duration = cache.get(key, None)
#     cache.set(key, this_duration)
#     print(this_duration)


def test_read_file_populates_data():
    # test_check_duration(request, cache)
    """Checks that reading the file populates global data variable"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_filter_chars_and_normalize_data():
    # test_check_duration(request, cache)
    """Checks that the singleline comment count works"""
    compute_tf_cookbook.data = ["-", "and"]
    compute_tf_cookbook.filter_chars_and_normalize()
    assert compute_tf_cookbook.data == [" ", "and"]


def test_scan():
    """Checks that the scan function works properly"""
    # pylint: disable=len-as-condition
    compute_tf_cookbook.scan()
    assert len(compute_tf_cookbook.words) != 0


def test_sort():
    """Check that the sort function works properly"""
    compute_tf_cookbook.filter_chars_and_normalize()
    compute_tf_cookbook.frequencies()
    compute_tf_cookbook.sort()
    freqSort = compute_tf_cookbook.word_freqs
    max_freq = 100000
    for tf in freqSort:
        assert tf[1] <= max_freq
        max_freq = tf[1]


def test_frequencies():
    "Check that the frequencies function works properly"
    compute_tf_cookbook.frequencies()
    compute_tf_cookbook.sort()
    word_list = ["and", "test2", "test3"]
    freq_list = [1, 1, 1]
    for i, tf in enumerate(compute_tf_cookbook.word_freqs):
        assert tf[0] == word_list[i]
        # assert tf[1] == freq_list[i]
