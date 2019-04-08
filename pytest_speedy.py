"""  """
import pytest


def pytest_addoption(parser):
    """ Print stuff to header with --speedy """
    group = parser.getgroup("speedy")
    group.addoption(
        "--speedy",
        action="store_true",
        help="pytest-speedy help \n--speedy: runs the fastest test first",
    )


def pytest_report_header():
    """  """
    msg = print("TEST\nInital Set up for Conftest to Test pytest-speedy\nTEST")

    return msg
