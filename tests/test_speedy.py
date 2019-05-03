""" Tests the pytest_speedy.py plugin for pytest """

import pytest_speedy


def test_profile():
    """Testing profile function within pytest_speedy """
    tracked_functions = []
    f = []
    for func in tracked_functions:
        globals()[func.__name__] = pytest_speedy.profile(f)
    assert pytest_speedy.profile(f) is not None


def test_sort():
    """Test sort function within pytest_speedy"""
    example = [1, 3, 4, 2]
    # pylint: disable=assignment-from-no-return
    sortList = pytest_speedy.sort(example)
    assert sortList is None
