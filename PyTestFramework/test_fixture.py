import pytest

@pytest.yield_fixture()

def setUp():
    print ("Running method level setup")
    yield
    print("\nOnce yie")

def test_method1(setUp):
    print ("Running method 1")

def test_method2(setUp):
    print ("Running method 2")














































































