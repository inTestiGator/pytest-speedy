""" Checks the tests with the fastest efficiency first """


def pytest_addoption(parser):
    """ Print speed of tests to header with --speedy """
    group = parser.getgroup("speedy")
    group.addoption(
        "--speedy",
        action="store_true",
        help="pytest-speedy help \n--speedy: runs the fastest test first",
    )


def pytest_report_header():
    """ Display test message in the header """
    msg = print("TEST\nInital Set up for Conftest to Test pytest-speedy\nTEST")

    return msg

   
 def pytest_collect_file(path, parent):
    """ Hook to save duration of tests in a txt file """
  if path.ext == '.py':
    return PyCollector(path=path, parent=parent)
