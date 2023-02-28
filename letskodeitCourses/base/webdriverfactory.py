import os
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        # Inicializa WebDriverFactory clase
        self.browser = browser

    def getDriverInstance(self):

        # Toma el sitio

        # Sitio para realizar los test y pages que se llaman "daily"
        #baseUrl = "https://courses.letskodeit.com/practice"

        # Sitio para realizar los test y pages que se llaman "courses" y "login"
        baseUrl = "https://courses.letskodeit.com/"

        if self.browser == "chrome":
            chromedriver = "COLOCAR LA DIRECCION DEL DRIVER AQUI"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)

        elif self.brwoser == "firefox":
            print("Please, set the settings to Firefox browser")
        elif self.browser == "iexplorer":
            print("Please, set the settings to iExplorer browser")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
