"""Test cases for the module that uses a cookbook programming style"""

import datetime
import pytest
import requests as request
from termfrequency import compute_tf_cookbook

# use "pipenv run pytest -s" to run this fixture
@pytest.fixture(autouse=True)
def test_check_duration(cache):
    """ Docstring """
    print("this is check duration")
    key = "duration/" + request.node.nodeid.replace(";", "_")
    # nodeid's can have colons
    # keys become filenames within .cache
    # replace colons with something filename safe
    start_time = datetime.datetime.now()
    # yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
#     last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    print(this_duration)


def test_read_file_populates_data(test_check_duration):
    # test_check_duration(request, cache)
    """Checks that reading the file populates global data variable"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_filter_chars_and_normalize_data(test_check_duration):
    # test_check_duration(request, cache)
    """Checks that the singleline comment count works"""
    compute_tf_cookbook.data = ["-", "and"]
    compute_tf_cookbook.filter_chars_and_normalize()
    assert compute_tf_cookbook.data == [" ", "and"]
