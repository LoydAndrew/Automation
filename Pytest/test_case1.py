import pytest

@pytest.yield_fixture()

def setUp():
    print ("Running test_case1")
    yield
    print("\nOnce yield after every method")

def test_method_case1(setUp):
    print ("Running method case1")

def test_method_case2(setUp):
    print ("Running method case2")














































































