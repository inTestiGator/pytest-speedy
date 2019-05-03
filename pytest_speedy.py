""" Program that times the tests in a file and sorts them by fastest time first """

import sys
import time
import pytest

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
    """ The program is executed if '--speedy' is called in the terminal window """
    # pylint: disable = global-statement
    global tracked_functions
    global sortedList
    # pylint: disable=no-member
    if pytest.config.getoption("speedy"):
        # adding test functions to list called tracked_functions
        tracked_functions = [testOne, testTwo, testThree]
        # tracked_fuctions = [test for test in dir(sort)
        # if callable(getattr(sort, test)) and not test.startswith("__")]
        # weaver function
        for func in tracked_functions:
            globals()[func.__name__] = profile(func)
        # pylint: disable = assignment-from-no-return
        sortedList = sort(testThree(testTwo(testOne(sys.argv[1]))))
        print()
        # print(sortedList)


def profile(f):
    """ Function that times the test cases by using aspect oriented programming """
    # pylint: disable = global-statement
    global this_duration

    def profilewrapper(*arg, **kw):
        start_time = time.time()
        ret_value = f(*arg, **kw)
        elapsed = time.time() - start_time
        print("%s(...) took %s secs" % (f.__name__, elapsed))
        this_duration.append(elapsed)
        return ret_value

    return profilewrapper


def pytest_collection_modifyitems(items):
    """ Hook used for reordering the tests in the file """
    for item in items:
        funcItem = item.function
        profile(funcItem)


# pylint: disable = unused-argument
def sort(items):
    """ Function that sorts the list of durations calculated in the profile function """
    new_duration = sorted(this_duration)
    print()
    print("Creating a list of the Results:")
    print(this_duration)
    print()
    print("Reordering the list of the Results: ")
    print(new_duration)


# pylint: disable = redefined-builtin
def testOne(list):
    """ Example test one. """
    print()
    print("Sample of Test 1")


def testTwo(list):
    """ Example test two. """
    print()
    print("Sample of Test 2")


def testThree(list):
    """ Example test three. """
    print()
    print("Sample of Test 3")
