from .imported import a_function


def test_relative_import():
    assert a_function() == "result"