import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("I run first")
    def test_a(self):
        print("I run test1")

    def test_b(self):
        print("I run test2")

    @classmethod
    def tearDownClass(cls):
        print("I run after test")


if __name__ == '__main__':
    unittest.main()
