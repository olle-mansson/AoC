import pytest

from day7.day7_solution import number_of_valid_ssl, number_of_valid_tsl


def test_number_of_valid_ips():
    test_file = open("input_test.txt")
    assert 2 == number_of_valid_tsl(test_file)


def test_number_of_valid_ssl():
    test_file = open("input_test2.txt")
    assert 3 == number_of_valid_ssl(test_file)


pytest.main()
