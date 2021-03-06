# pytest-speedy

![logo](.github/pytest-speedy_logo.png "pytest-speedy")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-speedy.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-speedy)
[![codecov](https://codecov.io/gh/inTestiGator/pytest-speedy/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/gh/inTestiGator/pytest-speedy)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-yellow.svg)](https://www.python.org/)
![license-gnu](https://img.shields.io/github/license/inTestiGator/pytest-speedy.svg)
[![code-style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Overview of pytest-speedy

A pytest plug-in that checks the tests with the fastest efficiency first.

## General Description

Pytest-Speedy is a plugin for pytest that allows users to run the fastest and
most efficient test cases first. This will allow an overall faster runtime for
programs running test cases.

## Features

In Pytest-Speedy, we want to provide optimal test case runtime for your
programs. Our main features are checking the runtime of each test case that you
have, storing that information, and then using that information to reorder the
test cases. The tests cases will run in ascending order for their runtimes so
that the smaller runtimes will run first and the larger runtimes will be run
last.

## Usage of pytest-speedy

To be able to run Pytest Speedy, the user will need the Python version 3.6.7 or
the most recent version. The user will also need the Pipenv version 2018.11.26.

* If the user does not have the correct Python version, please follow this link
  to update your Python version:

```
https://www.python.org/downloads/
```

* If the user does not have the correct Pipenv version, please use this command
  in your terminal window to update your Pipenv version:

```
pip install --user --upgrade pipenv
```

Now once the user has the correct versions for Python and Pipenv, cloning into
the repository is needed. In order to do this, the user will need to enter this
command into their terminal window:

```
git clone git@github.com:inTestiGator/pytest-speedy.git
```

After the user has cloned into the repository, the pipenv dependencies must be
installed by entering this command into the terminal window:

```
pipenv install --dev  or  $ pipenv install -d
```

After the user has installed the dependencies, the next step is the setup of
Pytest Speedy. To setup Pytest Speedy, the user will need to enter this command
into their terminal window:

```
python3 setup.py install
```

Now the user is able to run Pytest Speedy by entering this command into the
terminal window:

```
pytest --speedy
```

To test the code coverage of the program, you can look click on the badge and view
the most recent commits, or type this command in the terminal window:

```
pipenv run pytest tests/ --cov-config pytest.cov --cov-report term-missing --cov
```
