""" Checks the tests with the fastest efficiency first """

import ast
import inspect
import pytest

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
    if pytest.config.getoption("speedy")
        execution()


@pytest.fixture(autouse=True)
def execution(request, cache):
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


def pytest_collection_modifyitems(items):
    """ Used to reorder the tests """
