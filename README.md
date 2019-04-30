# pytest-speedy

![logo](.github/pytest-speedy_logo.png "pytest-speedy")

[![Build Status](https://api.travis-ci.com/inTestiGator/pytest-speedy.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-speedy)
[![codecov.io](http://codecov.io/github/inTestiGator/pytest-speedy/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-speedy?branch=master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-purple.svg)](https://www.python.org/)

## Overview of pytest-speedy

A pytest plug-in that checks the tests with the fastest efficiency first.

## General Description

This pytest plugin will run by reordering the test cases so that the test case
with the fastest running time will be tested first. The plugin will go through
all of the test cases, record the run time from the fastest to slowest and then
test them in that order.

## Features

(Add in features about pytest-speedy)


## Usage of pytest-speedy

(Add in details about what version of Python the plug-in is configured too as
  well as how to update or install Python)
To be able to run Pytest Speedy, the user will need the Python version 3.6.7 or the most recent version. The user will also need the Pipenv version 2018.11.26.

* If the user does not have the correct Python version, please follow this link to update your Python version:

  * https://www.python.org/downloads/

* If the user does not have the correct Pipenv version, please use this command in your terminal window to update your Pipenv version:

  * $ pip install --user --upgrade pipenv

Now once the user has the correct versions for Python and Pipenv, cloning into the repository is needed. In order to do this, the user will need to enter this command into their terminal window:

  * $ git clone git@github.com:inTestiGator/pytest-speedy.git

After the user has cloned into the repository, the pipenv dependencies must be installed by entering this command into the terminal window:

  * $ pipenv install --dev  or  $ pipenv install -d

After the user has installed the dependencies, the next step is the setup of Pytest Speedy. To setup Pytest Speedy, the user will need to enter this command into their terminal window:

  * $ python3 setup.py install

Now the user is able to run Pytest Speedy by entering this command into the terminal window:

  * $ pytest -s
