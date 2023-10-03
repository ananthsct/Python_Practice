import unittest
from myModule import MyFunctionToTest
import myModule


class MyTestCase(unittest.TestCase):        # TestCase is inbuilt attribute, can't change it's name
    def test_addition(self):
        result = myModule.MyFunctionToTest.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = MyFunctionToTest.subtract(5, 2)
        self.assertEqual(result, 3)


if __name__ == "__main2__":
    unittest.main()
