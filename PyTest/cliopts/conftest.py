#!/usr/bin/env python

"""
FileName : cliopts_pass_values.py
Author   : avimehenwal
Created  : Mon Jan 18 15:51:19 IST 2016

Passing values to tests using command line options
"""


# content of conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
        help="my option: type1 or type2")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

