import unittest
import os


class TestParser(unittest.TestCase):

    # Test for proper tally of parsed phrases
    def test_input_case1(self):
        input = "alpha alpha alpha alpha alpha alpha"
        expected_output = "alpha alpha alpha - 4"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip()  # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)

    # Test multiple matches
    def test_input_case2(self):
        input = "alpha alpha alpha beta"
        expected_output = "alpha alpha alpha - 1\n" \
                          "alpha alpha beta - 1"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip()
        self.assertEqual(output, expected_output)

    # Test empty input
    def test_input_case3(self):
        input = ""
        expected_output = ""
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip()
        self.assertEqual(output, expected_output)

    # Test for case-insensitivity of resulting tally
    def test_input_case4(self):
        input = "alpha alpha Alpha alpha alpha Alpha "
        expected_output = "alpha alpha alpha - 4"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip()
        self.assertEqual(output, expected_output)

    # Test input with Unicode characters
    def test_input_case5(self):
        input = "å gjøre kål på"
        expected_output = "å gjøre kål - 1\n" \
                          "gjøre kål på - 1"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip()
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
