from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage:
    link_privacyPolicy_linktext = "Privacy Policy"
    link_termsAndCondition_linktext = "Terms & Conditions"
    link_policyDoc_linktext = "Click here"
    text_PageContent_xpath = "//body"

    def __init__(self,driver):
        self.driver = driver
    
    def clickPrivacyPolicy(self, driver):
        self.driver.find_element(By.LINK_TEXT, self.link_privacyPolicy_linktext).click()

    def clickTermsAndCondition(self, driver):
        self.driver.find_element(By.LINK_TEXT, self.link_termsAndCondition_linktext).click()
    
    def clickPolicyDoc(self,driver):
        self.driver.find_element(By.LINK_TEXT, self.link_policyDoc_linktext).click()

    def getPageContent(self, driver):
        text = self.driver.find_element(By.XPATH, self.text_PageContent_xpath).text
        return text