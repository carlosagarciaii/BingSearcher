from selenium import webdriver
import time
from random import *
from _CoreTools import *

moduleVersion = '1.5.0.1P'


class BingLogin:
    def __init__(self,driver):
        self.driver = driver
        

    def exceptionText(functionName,e):
        return '\n---------------------------\nEXCEPTION\n---------------------------\nFile:\t_BingLogin\nFunction:\t' + str(functionName) + '\n' + str(e)


    def Login(self,username,password):
        try:
            driver = self.driver
        
            print('BingLogin - Step\tNave to login.live.com')
            driver.get('https://login.live.com')
            time.sleep(randint(3,9))
            print('Current Title:\t' + driver.title)
            print('Current URL:\t' + driver.current_url)

            print('\nBingLogin - Step\tFind name("loginfmt")')    
            if (ct(driver).NameV('loginfmt')):
                driver.find_element_by_name('loginfmt').send_keys(username)
                time.sleep(randint(2,5))
            print('\nBingLogin - Step\tFind xpath(//Input[@type="submit"])')    
            if (ct(driver).XpathV('//Input[@type="submit"]')):
                driver.find_element_by_xpath('//Input[@type="submit"]').click()
                time.sleep(randint(5,10))

            print('\nBingLogin - Step\tFind name(\'passwd\')') 
            if (ct(driver).NameV('passwd')):
                driver.find_element_by_name('passwd').send_keys(password)
                time.sleep(randint(2,5))
        
            print('\nBingLogin - Step\tFind xpath(//Input[@type="submit"])') 
            if (ct(driver).XpathV('//Input[@type="submit"]')):
                driver.find_element_by_xpath('//Input[@type="submit"]').click()
                time.sleep(randint(5,10))
        
            print('\nBingLogin - Step\tFind xpath(//Input[@value="No"])') 
            ct(driver).SafeClick('//Input[@value="No"]')
            #driver.find_element_by_xpath('//Input[@value="No"]').click()
            time.sleep(randint(8,15))

        except Exception as e:
            raise ValueError(BingLogin.exceptionText('BingLogin.ThisOrThat',e))
            return False       
        return True

    
        

print('\n-------------------------------------\nBingLogin Load V:' + moduleVersion + '\t-\tSUCCESS\n-------------------------------------\n')
