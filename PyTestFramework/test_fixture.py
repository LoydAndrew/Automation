import pytest

@pytest.yield_fixture()

def setUp():
    print ("Once before every method")
    yield
    print("\nOnce yield after every method")

def test_method1(setUp):
    print ("Running method 1")

def test_method2(setUp):
    print ("Running method 2")














































































