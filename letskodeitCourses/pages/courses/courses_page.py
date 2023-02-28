import time
from base.selenium_driverFunctions import SeleniumDriverFunctions
import utilities.custom_logger as cl
import logging


# Pages del test "" para realizar pruebas end-to-end en el sitio
# Esta prueba consiste en buscar cierto curso disponible en el sitio y simular una compra

class Courses(SeleniumDriverFunctions):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locator

    _courses_link = "//a[contains(text(), 'ALL COURSES')]"

    #_input_courses = "search"
    _input_courses = "//input[@id='search']"
    _search_course_icon = "//button[@type='submit']"
    _name_of_curse_complete = "//h4[@class='dynamic-heading' and contains(text(), '{0}')]"
    _select_courses = "//h4[@class='dynamic-heading']"


    _enroll_button = "//button[contains(text(), 'Enroll in Course')]"
    _card_num = "//input[@aria-label='Número de la tarjeta de crédito o débito']"
    #_card_num = "card-number"
    _card_exp = "//input[@aria-label='Fecha de vencimiento de la tarjeta de crédito o débito']"
    #_card_exp = "card-expiry"
    _submit_button = "//div[@class='panel payment-panel']//div[@class='col-xs-12']//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _msg_error = "//span[contains(text(), 'This field is required')]"

    _cardExtention = "//li[@class='card-no text-danger']//span[contains(text(), 'El número de tarjeta está incompleto.')]"


    #ACTIONS

    def clickCourseLink(self):
        self.ClickElement(self._courses_link, typeBy="xpath")

    def courseEnter(self, name):
        self.sendData(name, locator=self._input_courses, typeBy="xpath")
        self.ClickElement(locator=self._search_course_icon, typeBy="xpath")

    def enrollCourse(self, fullCourseName):
        # Al usar ".format()" en el localizador debe contener en texto un "{0}" para indicar que
        # recibira un parametro por "format"
        self.ClickElement(locator=self._name_of_curse_complete.format(fullCourseName), typeBy="xpath")

    def clickEnrollButton(self):
        self.ClickElement(self._enroll_button, typeBy="xpath")

    def numCard(self, num):
        time.sleep(6)
        self.switchFrameByIndex(locator=self._card_num, typeBy="xpath")
        self.sendData(data=num, locator=self._card_num, typeBy="xpath")
        self.switchToDefaultContent()

    def expCard(self, exp):
        self.switchFrameByIndex(locator=self._card_exp, typeBy="xpath")
        self.sendData(data=exp, locator=self._card_exp, typeBy="xpath")
        self.switchToDefaultContent()

    def clickSumit(self):
        self.ClickElement(self._submit_button, typeBy="xpath")

    def informationCard(self, num, exp):
        self.numCard(num)
        self.expCard(exp)

    def allActionstoEnroll(self, num, exp):
        self.clickEnrollButton()
        self.DirectionScroll(position="down")
        time.sleep(2)
        self.informationCard(num, exp)
        time.sleep(2)
        #self.clickSumit()

    #Enviara un valor al "course_test" el cual sera evaluado con ayuda de la funcion "markFinal()"
    def cardNumIsCorrect(self):
        #eMessage = self.waitElement(locator=self._cardExtention, typeBy="xpath")
        result2 = self.displayedElement(locator=self._cardExtention, typeBy="xpath")
        return result2

