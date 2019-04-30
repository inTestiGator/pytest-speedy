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


def execution():
    """ Docstring """
    testFile = open("tests/test_compute_tf_cookbook.py", "r")
