"""Setup for pytest-speedy plugin"""

from setuptools import setup

setup(
    name="pytest-speedy",
    version="0.1.0",
    description="A pytest plugin that reorders test cases from fastest to slowest.",
    url="url here",
    author="Matt Marconi, Ben Watto, Dillon Thoma, Mikey Spurr, Steve Li",
    author_email="marconim@alleghney.edu, wattob@allegheny.edu, thomad@allegheny.edu, ",
    license="Pytest-Speedy Copyright ",
    py_modules=["pytest_speedy"],
    install_requires=["pytest"],
    entry_points={"pytest11": ["speedy = pytest_speedy"]},
)
