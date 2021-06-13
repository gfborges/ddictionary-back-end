import pytest


def assert_dict(data: dict, expected: dict):
    for (key, value) in expected.items():
        assert data.get(key) == value
