#                                                        PYTHON UNNITEST AND DOCTEST

   ## unittest (PyUnit):

    unittest is a testing framework inspired by Java's JUnit. It provides a test discovery mechanism and various assertion methods to check expected outcomes. Here are some key features:
*        Test Case: Test cases are organized into classes that inherit from unittest.TestCase.
*        Test Discovery: It can automatically discover and run test cases based on naming conventions or by using the discover command.
*        Test Fixture: You can set up preconditions and clean up after tests using setUp and tearDown methods.
*        Assertion Methods: unittest provides a wide range of assertion methods like assertEqual, assertRaises, assertTrue, etc., to check expected results.
*        Test Runner: The test runner executes test cases and reports the results.

    Example:

    python

```
import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

doctest:

doctest is a testing framework that extracts test cases from docstrings and runs them. It's lightweight and often used for simple, self-contained tests embedded in documentation. Key features include:

*    Test in Docstrings: Test cases are written within docstrings of functions or modules using special comments that begin with >>>.
*    Automatic Test Discovery: doctest automatically discovers and runs test cases found in docstrings.
*   Minimal Setup: It doesn't require extensive setup or additional test files.
*    Limited Assertion: doctest primarily checks if the output in the docstring matches the actual output.

Example:

python
```
    def add(a, b):
        """
        This function adds two numbers.

        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        """
        return a + b

    if __name__ == '__main__':
        import doctest
        doctest.testmod()
```

> You can run doctest by executing the script, and it will find and run the tests embedded in the docstrings.

>In summary, unittest is a more comprehensive testing framework suitable for large-scale testing with test discovery and advanced assertion methods, while doctest is a lightweight option primarily used for simple tests embedded in documentation. The choice between them depends on the complexity and requirements of your testing scenarios.

![road lights](david-watkis-LwRUp8vJJI8-unsplash.jpg)
