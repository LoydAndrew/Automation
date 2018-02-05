import unittest

class TestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("#" * 30)
        print("Running only once before every test")
        print("#" * 30)

    def test_method1(self):
        print("\nRunning 1 method")

    def test_method2(self):
        print("Running 2 method")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print ("Running only once after every test")
        print("#" * 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)