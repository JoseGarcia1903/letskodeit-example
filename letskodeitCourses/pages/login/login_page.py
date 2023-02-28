import logging
import time
import utilities.custom_logger as cl
from base.selenium_driverFunctions import SeleniumDriverFunctions

class LoginPage(SeleniumDriverFunctions):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_L = "//div[@data-component='button']//a[@href='/login']"
    _email_f = "email"
    _password_f = "password"
    _login_b = "login"

    #def getLoginLink(self):
    #    return self.driver.find_element(By.XPATH, self._login_Link)

    #def getEmailField(self):
    #    return self.driver.find_element(By.ID, self._email_field)

    #def getPasswordField(self):
    #    return self.driver.find_element(By.ID, self._password_field)

    #def getButtonLogin(self):
    #    return self.driver.find_element(By.XPATH, self._login_button)

    # ACTIONS

    def enterLoginLink(self):
        self.ClickElement(self._login_L, typeBy="xpath")

    def email(self, email):
        self.sendData(email, self._email_f)

    def password(self, password):
        self.sendData(password, self._password_f)

    def loginButton(self):
        self.ClickElement(self._login_b)

    # TESTS

    def loginSuccessfull(self, email, password):

        self.enterLoginLink()
        self.clearField()
        time.sleep(2)
        self.email(email)
        self.password(password)
        time.sleep(2)
        #self.loginButton()

    def loginFail(self, email, password):

        self.enterLoginLink()
        self.clearField()
        time.sleep(2)
        self.email(email)
        self.password(password)
        time.sleep(2)
        self.loginButton()
        time.sleep(3)

    def checkCorrectLogin(self):

        #elementPresent = self.isElementPresent("//*[@id='navbar']//span=[text()='User Settings']",
        #                                       locatorType="xpath")
        elementPresent = self.ElementPresent("//h4[contains(text(), 'Login')]", typeBy="xpath")

        return elementPresent

    def checkLoginFail(self):
        elementPresent = self.ElementPresent("//span[contains(text(), 'Your username or password is invalid. Please try again.')]",
                                               typeBy="xpath")
        return elementPresent

    def clearField(self):
        emailField = self.gElement(locator=self._email_f)
        emailField.clear()
        passwordField = self.gElement(locator=self._password_f)
        passwordField.clear()


    def checkTitle(self):
        return self.verifyTitle("Login")
