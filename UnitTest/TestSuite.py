import unittest
from UnitTest.Setup_Teardown import  TestCase2
from UnitTest.TestCase1 import TestCase1

#get all tests

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

#creating a test suite

smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)