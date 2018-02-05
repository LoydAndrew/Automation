import unittest

class TestCase1(unittest.TestCase):

    def setUp(self):
        print ("Run once before every test")

    def test_method1(self):
        print("Running 1 method")

    def test_method2(self):
        print("Running 2 method")

    def tearDown(self):
        print ("Running after every test")

if __name__ == "__main__":
    unittest.main(verbosity=2)