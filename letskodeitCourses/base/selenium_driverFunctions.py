import logging
import time
import os
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl

#Clases para facilitar ciertas funciones de Selenium.

class SeleniumDriverFunctions():

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def gType(self, typeBy):
        typeBy = typeBy.lower()

        if typeBy == "id":
            return By.ID
        if typeBy == "xpath":
            return By.XPATH
        if typeBy == "name":
            return By.NAME
        if typeBy == "css":
            return By.CSS_SELECTOR
        if typeBy == "linkText":
            return By.LINK_TEXT
        if typeBy == "classname":
            return By.CLASS_NAME
        else:
            self.log.error("The Element: " + typeBy + " IS NOT SUPPORTED")
            return False

    def gElement(self, locator, typeBy="id", element=None):

        try:
            typeBy = typeBy.lower()
            type = self.gType(typeBy)
            element = self.driver.find_element(type, locator)
            self.log.info("Locator found: " + locator + " Type: " +
                          typeBy)
        except:
            self.log.error("Locator NOT FOUND: " + locator
                           + " Type: " + typeBy)
            print_stack()
        return element


    def ClickElement(self, locator, typeBy="id", element=None):

        try:
            if locator:
                element = self.gElement(locator, typeBy)
            element.click()
            self.log.info("Clicked Element: " + locator
                          + " Type: " + typeBy)
        except:
            self.log.error("We Can NOT Clicked the Element: " + locator
                           + " Type: " + typeBy)
            print_stack()



    def sendData(self, data, locator, typeBy="id"):

        element = self.gElement(locator=locator, typeBy=typeBy)
        try:
            element.send_keys(data)
            self.log.info("Data sent: " + data + " To:" + locator)
        except:
            print_stack()
            self.log.error("ERROR, DATA NOT SENT")


    def waitElement(self, locator, typeBy="id",
                       timeout=10, pollFrecuency=0.5):

        element = None
        try:
            byType = self.gType(typeBy)
            self.log.info("Waiting maximum :: " + str(timeout) +
                            ":: seconds")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrecuency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("Element on the page")
        except:
            self.log.info("Element NOT on the page")
            print_stack()
        return element

    def displayedElement(self, locator="", typeBy="id", element=None):
        displayed = False
        try:
            if locator:
                element = self.gElement(locator, typeBy)
            if element is not None:
                displayed = element.is_displayed()
                self.log.info("Element Displayed using: " + locator)
            else:
                self.log.info("Element NOT Displayed using: " + locator)
            return displayed
        except:
            self.log.error("Element to Display NOT FOUND")
            return False



    def DirectionScroll(self, position="up"):

        if position == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if position == "down":
            self.driver.execute_script("window.scrollBy(0, 500);")



    def screenShot(self, message):

        fileName = message + "." + str(round(time.time() * 1000)) + ".png"
        screenShotsDirectory= "../screenshotsFailed/"

        relativeFileName = screenShotsDirectory + fileName
        currentDirectory = os.path.dirname(__file__)

        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("ScreenShot Saved: " + destinationFile)
        except:
            self.log.error("SCREENSHOT NOT SAVED")
            print_stack()


    def gElementList(self, locator, typeBy="id"):

        element = None
        try:
            typeBy = typeBy.lower()
            byType = self.gType(typeBy)
            element = self.driver.find_elements(byType, locator)
            self.log.info("List with elements found using: " + locator +
                          " Type: " + typeBy)
        except:
            self.log.error("List with elements NOT found using: " + locator +
                           " Type:" + typeBy)
        return element


    def ElementPresent(self, locator, typeBy="id"):
        try:
            element = self.gElement(locator, typeBy)
            if element is not None:
                self.log.info("Element Present")
                return True
            else:
                return False
        except:
            self.log.info("Element NOT Present")
            return False


    def switchFrame(self, id="", name="", index=None):

        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)



    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()



    def switchFrameByIndex(self, locator, typeBy="xpath"):

        result = False
        try:
            iframe_list = self.gElementList("//iframe", typeBy="xpath")
            self.log.info("iframe List: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchFrame(index=iframe_list[i])
                result = self.ElementPresent(locator, typeBy)
                if result:
                    self.log.info("Element found in iframe with index: ")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("Element NOT found in any iframe")
            return result


    def gTitle(self):
        return self.driver.title


    def verifyText(self, actualText, expectedText):

        self.log.info("Actual Text: " + actualText)
        self.log.info("Text Expected: " + expectedText)
        if expectedText.lower() in expectedText.lower():
            self.log.info("SAME TEXT")
            return True
        else:
            self.log.error("ERROR IN VERIFY TEXT CONTENT")
            return False


    def verifyTitle(self, titleToCheck):

        # Checa el titulo en la pagina actual
        try:
            actualTitle = self.gTitle()
            return self.verifyText(actualTitle, titleToCheck)
        except:
            self.log.error("ERROR IN TITLE FUNCTION")
            print_stack()
            return False



    def findHoverElement(self, locator, typeBy="", element=None):

        if locator:
            element = self.gElement(locator=locator, typeBy=typeBy)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Mouse Hovered to Element")
        except:
            self.log.error("Element to find on hover not found")



    def hoverClick(self, locator="", typeBy="", element=None):

        if locator:
            element = self.gElement(locator=locator, typeBy=typeBy)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            self.log.info("Hover element clicked")
        except:
            self.log.error("Hover element not clicked, Please, checked out")

