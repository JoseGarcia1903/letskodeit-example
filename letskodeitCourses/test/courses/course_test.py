import pytest
from utilities.tstatus import TestStatus
from pages.courses.courses_page import Courses
from utilities.read import GetData
import unittest
import time

# Test para simular busqueda de un curso en el sitio y simular la compra de cierto curso

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = Courses(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_verifyCourseFail(self):
        self.courses.clickCourseLink()
        self.courses.courseEnter("JavaScript")
        time.sleep(2)
        self.courses.enrollCourse("JavaScript for beginners")
        self.courses.allActionstoEnroll(num="1234", exp="2105")
        result = self.courses.cardNumIsCorrect()
        # Funcion de "teststatus" para agrupar todas las funciones y verificar cuales son
        # exitosas y cuales no
        self.ts.finalResult("test_verifyCourseFail", result, "Trying to enrroll a course")
