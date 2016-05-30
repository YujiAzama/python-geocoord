from setuptools import find_packages
from setuptools import setup

setup(
    name='geocoord',
    version='1.0.0',
    description="",
    classifiers=[
        "Programming Language :: Python",
    ],
    author="Yuji Azama",
    author_email="yuji.azama@gmail.com",
    packages = find_packages(),
    test_suite = "tests",
)
