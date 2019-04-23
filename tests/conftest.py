""" Checks the tests with the fastest efficiency first """

import os
import sys


def pytest_addoption(parser):
    """ Print speed of tests to header with --speedy """
    group = parser.getgroup("speedy")
    group.addoption(
        "--speedy",
        action="store_true",
        help="pytest-speedy help \n--speedy: runs the fastest test first",
    )


def pytest_report_header():
    """ Reports Message to display in pytest header """
    msg = print("TEST\nInital Set up for Conftest to Test pytest-speedy\nTEST")

    return msg


def pytest_collect_file(path, parent):
    """ Hook to save duration of tests in a txt file """
    if path.ext == '.yaml':
        return YamlCollector(path=path, parent=parent)
    if path.ext == '.py':
        # here it's a regular .py file that should be handled by pytest the normal way
        return None


GO_BACK_A_DIRECTORY = "/../"
GO_INTO_SRC_DIRECTORY = "src"

# set the system path to contain the previous directory
PREVIOUS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PREVIOUS_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_SRC_DIRECTORY)
