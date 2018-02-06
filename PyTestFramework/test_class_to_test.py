import pytest
from SomeClass import SomeClass

@pytest.mark.usefixtures("onetimesetUp","setUp")
class TestClass():

    @pytest.fixture(autouse=True)
    def class_setup(self,onetimesetUp):
        self.abc=SomeClass(self.value)

    def test_methodB(self):
        result = self.abc.sum_number(1,2)
        assert result == 13
        print ("Running method B")

    def test_methodC(self):
        print ("Running method C")