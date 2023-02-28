import pytest
from pages.login.login_page import LoginPage
from utilities.tstatus import TestStatus
import unittest


# Test que simula el ingreso incorrecto y luego Correcto de un sistema de logeo

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lg = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lg.loginSuccessfull("test2@email.com", "thisisatest")
        finalTitle = self.lg.checkTitle()
        self.ts.mark(finalTitle, "Title Correct")
        CheckElementPresent = self.lg.checkCorrectLogin()
        self.ts.finalResult("test_validLogin", CheckElementPresent, "Test Valid Login Completed")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lg.loginFail("test2@email.com", "thisisatest")
        #CheckElementPresent = self.lg.checkLoginFail()
        #assert CheckElementPresent == True

