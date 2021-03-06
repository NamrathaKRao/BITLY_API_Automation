"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custome_logger as cl
import logging
from traceback import print_stack

class Status():
    log = cl.customLogger(logging.INFO)

    def __init__(self):
        """
        Inits CheckPoint class
        """
        self.resultList = []



    def setResult(self, result, resultMessage_on_pass,resultMessage_on_failure="Expected and Actual result did not match"):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage_on_pass)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage_on_failure)

            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage_on_failure)

        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")

            print_stack()

    def mark(self, result, resultMessage_on_pass,resultMessage_on_failure="Expected and Actual result did not match"):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage_on_pass,resultMessage_on_failure)

    def mark_Partial(self,testName,result,resultMessage_on_pass,resultMessage_on_failure="Expected and Actual result did not match"):
        self.setResult(result, resultMessage_on_pass,resultMessage_on_failure)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False

        else:
            self.log.info(resultMessage_on_pass)

    def markFinal(self, testName, result, resultMessage_on_pass,resultMessage_on_failure="Expected and Actual result did not match"):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage_on_pass,resultMessage_on_failure)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
