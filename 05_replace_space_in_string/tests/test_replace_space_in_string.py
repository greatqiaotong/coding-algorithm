import pytest
from replace_space_in_string import *


def test_replace_string_single_space():
    string = "Hello world!"
    assert replace_space(string) == "Hello%20world!"


def test_replace_string_single_space_start():
    string = " wow"
    assert replace_space(string) == "%20wow"


def test_replace_string_single_space_end():
    string = "wow "
    assert replace_space(string) == "wow%20"


def test_replace_string_multiple_spaces():
    string = "We are happy."
    assert replace_space(string) == "We%20are%20happy."


def test_replace_string_consecutive_spaces():
    string = "Hello  world!"
    assert replace_space(string) == "Hello%20%20world!"


def test_replace_string_no_space():
    string = "wow"
    assert replace_space(string) == "wow"


def test_replace_string_empty():
    string = ""
    with pytest.raises(ValueError):
        replace_space(string)


def test_replace_string_only_one_space():
    string = " "
    assert replace_space(string) == "%20"


def test_replace_string_only_spaces():
    string = "  "
    assert replace_space(string) == "%20%20"
