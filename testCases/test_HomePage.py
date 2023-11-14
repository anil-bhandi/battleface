import pytest
from selenium import webdriver
from pageObjects.homePage import Homepage
from time import sleep
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Home:
    basURL = ReadConfig.getApplicationUrl()
    privacyPolicyURL = ReadConfig.privacyPolicyURL()
    termsAndConditionURL = ReadConfig.termsAndConditionURL()
    logger = LogGen.loggen()

    def test_TS001_TC001_privacyPolicy(self,setup):
        self.logger.info("*************** test_TS001_TC001_privacyPolicy *****************")
        self.logger.info("*************** verifying Privacy Policy Page *****************")
        self.driver = setup
        self.driver.get(self.basURL)
        self.Hp = Homepage(self.driver)
        self.Hp.clickPrivacyPolicy(self.driver)
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        currURL = self.driver.current_url
        pageContent = self.Hp.getPageContent(self.driver)
        print(currURL)
        print(pageContent)
        if pageContent =="Dummy privacy policy page" and currURL == "https://qatest.battleface.com/pages/privacy-policy.html":
            self.driver.close()
            assert True
            self.logger.info("*************** test_TS001_TC001_privacyPolicy test passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_TS001_TC001_privacyPolicy.png")
            self.driver.close()
            self.logger.error("*************** test_TS001_TC001_privacyPolicy failed *****************")
            assert False

    def test_TS001_TC002_termsAndCondition(self,setup):
        self.logger.info("*************** test_TS001_TC002_termsAndCondition *****************")
        self.logger.info("*************** verifying Terms and Condition Page *****************")
        self.driver = setup
        self.driver.get(self.basURL)
        self.Hp = Homepage(self.driver)
        self.Hp.clickTermsAndCondition(self.driver)
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        currURL = self.driver.current_url
        pageContent = self.Hp.getPageContent(self.driver)
        print(currURL)
        print(pageContent)
        if pageContent =="Dummy Terms and Condition page" and currURL == "https://qatest.battleface.com/pages/terrms-and-conditions.html":
            self.driver.close()
            assert True
            self.logger.info("*************** test_TS001_TC002_termsAndCondition test passed *****************")
        else:
            self.driver.save_screenshot("..\\Screenshots\\"+ "test_TS001_TC002_termsAndCondition.png")
            self.driver.close()
            self.logger.error("*************** test_TS001_TC002_termsAndCondition test failed *****************")
            assert False
