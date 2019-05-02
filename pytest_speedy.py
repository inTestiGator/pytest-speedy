""" Checks the tests with the fastest efficiency first """

import ast
import datetime
import pytest
import sys
import re
import operator
import string
import time
import inspect
from functools import wraps

this_duration = []
tracked_functions = []
sortedList = []


def pytest_addoption(parser):
    """ Print speed of tests to header with --speedy """
    group = parser.getgroup("speedy")
    group.addoption(
        "--speedy",
        action="store_true",
        help="pytest-speedy help \n--speedy: runs the fastest test first",
    )


def pytest_report_header():
    """
    The program is executed via the execution function
    if speedy is called in the terminal window
    """
    global tracked_functions
    # pylint: disable=no-member
    if pytest.config.getoption("speedy"):
        # execution()
        # join points
        # add test functions to tracked functions
        tracked_functions = [test, test2, test3]
        # weaver
        for func in tracked_functions:
            globals()[func.__name__] = profile(func)


            # print(profile(test))
        sortedList = sort(test2(test(test3(sys.argv[1]))))
        # for i in sortedList[i]:
        #     print(i)



# pylint: disable=unused-variable
# pylint: disable=unused-argument
# @pytest.fixture(autouse=True)
def execution():
    """ Docstring """
    global this_duration
    # pylint: disable=redefined-builtin
    read_file = open("tests/test_compute_tf_cookbook.py")
    list = [
        item
        for item in ast.parse(read_file.read()).body
        if isinstance(item, ast.FunctionDef)
    ]
    for i in list:
        print("this is check duration")
        # key = "duration/" + request.node.nodeid.replace(";", "_")
        # nodeid's can have colons
        # keys become filenames within .cache
        # replace colons with something filename safe
        start_time = datetime.datetime.now()
        # yield
        stop_time = datetime.datetime.now()
        duration = (stop_time - start_time).total_seconds()
        # last_duration = cache.get(key, None)
        # cache.set(key, this_duration)
        # pylint: disable=unused-argument
        this_duration.append(duration)
        print(this_duration)


def pytest_collection_modifyitems(items):
    """ reordering """
    read_file = open("tests/test_compute_tf_cookbook.py")
    print(this_duration)
    new_duration = sorted(this_duration)
    for i in new_duration:
        print("")
        print("Reordering:")
        # key = "duration/" + request.node.nodeid.replace(";", "_")
        # nodeid's can have colons
        # keys become filenames within .cache
        # replace colons with something filename safe
        # last_duration = cache.get(key, None)
        # cache.set(key, this_duration)
        # pylint: disable=unused-argument
        print(new_duration)
        print("")
    # Sorting list of Integers in ascending
