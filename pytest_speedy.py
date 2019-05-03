""" Checks the tests with the fastest efficiency first """

import sys
import time
import pytest

this_duration = []
tracked_functions = []
sortedList = []

# pylint: disable = redefined-outer-name


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
    # pylint: disable = global-statement
    global tracked_functions
    global sortedList
    # pylint: disable=no-member
    if pytest.config.getoption("speedy"):
        # execution()
        # join points
        # add test functions to tracked functions
        tracked_functions = [testOne, testTwo, testThree]
        # tracked_fuctions = [test for test in dir(sort) if callable(getattr(sort, test)) and not test.startswith("__")]
        # weaver
        for func in tracked_functions:
            globals()[func.__name__] = profile(func)

            # print(profile(test))
        # pylint: disable = unused-variable
        # pylint: disable = assignment-from-no-return
        sortedList = sort(testThree(testTwo(testOne(sys.argv[1]))))
        print(sortedList)
        # print(tracked_fuctions)


def profile(f):
    """ Function for profile method """
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
    """ reordering """
    read_file = open("tests/test_compute_tf_cookbook.py")
    for item in items:
        funcItem = item.function
        profile(funcItem)


# pylint: disable = unused-argument
def sort(items):
    """ Function for sort """
    new_duration = sorted(this_duration)
    print()
    print("Creating a list of the Results")
    print(this_duration)
    print()
    print("Reordering the list of the Results: ")
    print(new_duration)
    # return sorted(sortedList.sort(ret_value))


# pylint: disable = redefined-builtin
def testOne(list):
    """ Example test one. """
    print("Sample of Test 1")



def testTwo(list):
    """ Example test two. """
    print("Sample of Test 2")


def testThree(list):
    """ Example test three. """
    print("Sample of Test 3")
