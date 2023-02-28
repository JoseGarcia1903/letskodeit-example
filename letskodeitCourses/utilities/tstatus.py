import logging
from base.selenium_driverFunctions import SeleniumDriverFunctions
import utilities.custom_logger as cl


# En un array registra los resultados de cada test case y al final evalua si una funcion
# dentro de un test case falla, tendra como resultado final un caso fallido


class TestStatus(SeleniumDriverFunctions):

    log = cl.CustomLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, rMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("VERIFICATION SUCCESSFUL :: " + rMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("VERIFICATION FAILED :: " + rMessage)
                    self.screenShot(rMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("VERIFICATION FAILED :: " + rMessage)
                self.screenShot(rMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("EXCEPTION OCURRED :: " + rMessage)
            self.screenShot(rMessage)


    def mark(self, result, rMessage):

        self.setResult(result, rMessage)


    def finalResult(self, testName, result, rMessage):

        self.setResult(result, rMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + "TEST FAILED")
            self.resultList.clear()
            assert True == False

        else:
            self.log.info(testName + "TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
