""" Checks the tests with the fastest efficiency first """

from functools import wraps
import pytest
import sys
import time

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


def profile(f):
    """ Function for profile method """
    global this_duration
    @wraps(f)
    def profilewrapper(*arg, **kw):
        start_time = time.time()
        ret_value = f(*arg, **kw)
        elapsed = time.time() - start_time
        print("%s(...) took %s secs" % (f.__name__, elapsed))
        this_duration.append(elapsed)
        return ret_value

    return profilewrapper


def pytest_collection_modifyitems(items):
    """ reordering """
    read_file = open("tests/test_compute_tf_cookbook.py")
    for item in items:
        funcItem = item.function
        profile(funcItem)

    # Sorting list of Integers in ascending


def sort(items):
    """ Function for sort """
    global sortedList
    new_duration = sorted(this_duration)
    print(this_duration)
    print("reordering:")
    print(new_duration)
    # return sorted(sortedList.sort(ret_value))


def test(list):
    print("Test1: True")
    return list


def test2(list):
    print("test2")
    print("Success?")
    print("Success?")


def test3(list):
    print("test2")
    print("Success?")
    print("Success?")
