# -*- coding: utf-8 -*-

from pytzdata.version import VERSION, OLSON_VERSION

EXPECTED_VERSION = "2018.7"

EXPECTED_OLSON_VERSION = "2018g"


def test_version():
    assert EXPECTED_VERSION == VERSION


def test_olson_version():
    assert EXPECTED_OLSON_VERSION == OLSON_VERSION
