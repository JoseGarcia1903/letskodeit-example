import unittest
from test.courses.course_test import CourseTest
from test.login.login_test import LoginTest

# Tomamos todos los test cases de las clases
testCase1 = unittest.TestLoader().loadTestsFromTestCase(CourseTest)
testCase2 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create a test suite combining all test classes
# Creamos un "test suite" combinando todos los "test cases"
smokeTest = unittest.TestSuite([testCase1, testCase2])
#smokeTest = unittest.TestSuite([testCase1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)