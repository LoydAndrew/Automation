import pytest

@pytest.mark.run(order=2)
def test_methodB(onetimesetUp,setUp):
    print ("Running method B")

def test_methodC(onetimesetUp,setUp):
    print ("Running method C")

def test_methodD(onetimesetUp,setUp):
    print ("Running method D")
@pytest.mark.run(order=1)
def test_methodA(onetimesetUp,setUp):
    print ("Running method A")