import unittest
import logging
from html_testRunner import HTMLTestRunner

# Configure logging
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

        if result != 2:
            logging.warning(f"Subtraction test failed. Expected 2, but got {result}")

    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)

    def test_division(self):
        result = 8 / 2
        self.assertEqual(result, 4)

        if result != 4:
            logging.error(f"Division test failed. Expected 4, but got {result}")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
    report_file = "test_report.html"

    with open(report_file, "wb") as report:
        runner = HTMLTestRunner(stream=report, title="Test Report", description="Sample Test Suite")
        runner.run(test_suite)
