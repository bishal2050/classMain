import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is run before test")

    def test_a(self):
        print("This is first test")
        # self.assertEqual("This is test", "This is also test", "This test failed")

    def myFunction(self):
        a =1
        return a

    def test_b(self):
        print("This is second test")
        self.assertEqual("This is test", "This is test", "Test failed")

    @classmethod
    def tearDownClass(cls):
        print("this is run when testing is completed")

if __name__ == '__main__':
    unittest.main()
