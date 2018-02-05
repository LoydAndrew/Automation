import unittest

class AssertMethod(unittest.TestCase):

    def  test_assert_true_false(self):
        a = True
        b = False
        self.assertTrue(a,"a is not True")
        self.assertFalse(b,"b is not false")


    def test_assert_equal(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a,b,msg="a is not equal to b")



if __name__ == "__main__":
    unittest.main(verbosity=2)