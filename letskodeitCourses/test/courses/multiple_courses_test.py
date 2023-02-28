import pytest
from utilities.tstatus import TestStatus
from pages.courses.courses_page import Courses
import unittest
import time
from ddt import ddt, data, unpack

# Este test realiza las misma pruebas que "course_test.py" con la direfencia que
# todos los parametros son tomados desde el "@data". Tener cuidado, el orden de los parametros son
# importantes


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class MultipleCourses(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = Courses(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    # Aqui se pueden especificar en otra cadena otros datos, de esta forma se puede
    # realizar las mismas pruebas con diferentes tipos de cursos
    @data(("JavaScript for beginners", "34567", "4567"))
    @unpack
    def test_verifyCourseFail(self, courseName, num, exp):
        self.courses.clickCourseLink()
        self.courses.courseEnter(courseName)
        time.sleep(3)
        self.courses.enrollCourse(courseName)
        self.courses.allActionstoEnroll(num=num, exp=exp)
        result = self.courses.cardNumIsCorrect()
        self.ts.finalResult("test_verifyCourseFail", result, "Trying to enrroll a course")
