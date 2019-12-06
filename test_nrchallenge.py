import unittest
import os

class TestHello(unittest.TestCase):
    # makes sure matches are counted correctly
    def test_case1(self):
        input = "alpha alpha alpha alpha alpha alpha" 
        expected_output = "alpha alpha alpha - 4"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)

    # makes sure multiple matches work     
    def test_case2(self): 
        input = "alpha alpha alpha beta"
        expected_output = "alpha alpha alpha - 1\n" \
                          "alpha alpha beta - 1"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)

    # makes sure empty file works
    def test_case3(self):
        input = ""
        expected_output = ""
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)

    # makes sure case-insensitive
    def test_case4(self):
        input = "alpha alpha Alpha alpha alpha Alpha "
        expected_output = "alpha alpha alpha - 4"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)

    # makes sure Unicode characters work
    def test_case5(self):
        input = "å gjøre kål på"
        expected_output = "å gjøre kål - 1\n" \
                          "gjøre kål på - 1"
        with os.popen("echo '" + input + "' | python nrchallenge.py") as o:
            output = o.read()
        output = output.strip() # Remove leading spaces and LFs
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
