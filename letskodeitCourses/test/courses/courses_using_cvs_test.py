import pytest
from utilities.tstatus import TestStatus
from pages.courses.courses_page import Courses
import unittest
import time
from ddt import ddt, data, unpack
from utilities.read import GetData


# Este test realiza las misma pruebas que "course_test.py" con la direfencia que
# todos los parametros anteriormente dados en el archivo ".test" se toman desde un archivo "cvs"

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class CoursesUsingcvsData(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.courses = Courses(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    # Direccion del archivo csv de donde tomara los parametros
    @data(*GetData("DIRECCION DEL ARCHIVO  '.CSV' (ASEGURAR QUE ESTE DENTRO DE LA CARPETA DEL PROYECTO)"))
    @unpack
    def test_verifyCourseFail(self, courseName, num, exp):
        self.courses.clickCourseLink()
        self.courses.courseEnter(courseName)
        time.sleep(3)
        self.courses.enrollCourse(courseName)
        self.courses.allActionstoEnroll(num=num, exp=exp)
        result = self.courses.cardNumIsCorrect()
        self.ts.finalResult("test_verifyCourseFail", result, "Trying to enrroll a course")
