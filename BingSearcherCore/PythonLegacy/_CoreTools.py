from selenium import webdriver
from random import *
import time

moduleVersion = '1.5.0.1P'

class ct:
    def __init__(self,driver):
        self.driver = driver
        print('Driver set for gtools')
        

    def exceptionText(functionName,e):
        return '\n---------------------------\nEXCEPTION\n---------------------------\nFile:\t_CoreTools\nFunction:\t' + functionName + '\n' + e

    '''
    
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingSearcher.Start',e))
            return False
        return True
    '''


    def NameV(self,name):
        driver = self.driver
        print('Attempting to locate element by name:\n\t\t' + name)
        try:
            element = driver.find_element_by_name(name)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nCould Not Find Name:\t' + name + '\n\n' + str(e) + '\n\n')
            return False
                
        return True

    def XpathV(self,xpath):
        driver = self.driver
        print('Attempting to locate Xpath:\n\t\t' + xpath)
        try:
            element = driver.find_element_by_xpath(xpath)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            
        except Exception as e:
            print('\n\nCould Not Find Xpath:\t' + xpath + '\n\n' + str(e) + '\n\n')
            return False
                
        return True

    def SafeClick(self,xpath):
        driver = self.driver
        print('SafeClicking on Xpath:\n\t\t' + xpath)
        try:
            element = driver.find_element_by_xpath(xpath)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            element.click()
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nSafeClick Failed for Xpath:\t' + xpath + '\n\n' + str(e) + '\n\n')
            return False
        
        return True

    def SafeClickL(self,element):
        driver = self.driver
        print('SafeClickL on Element:\n\t\t' + str(element))
        try:
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            element.click()
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nSafeClickL failed for Element:\t' + str(element) + '\n\n' + str(e) + '\n\n')
            return False
        
        return True

    def HasText(self,xpath,text):
        driver = self.driver

        if ct(driver).XpathV(xpath):
            
            if text.lower() in driver.find_element_by_xpath(xpath).text.lower():
                return True
            else:
                return False
        else:
            return False

    def CloseOtherTabs(self):
        driver = self.driver
        try:
            while 1==1:
                driver.switch_to.window(self.driver.window_handles[1])
                driver.close()
        
        except Exception as e:
            print('\n\nException:\n' + str(e) + '\n\n')
            driver.switch_to.window(self.driver.window_handles[0])

    


print('\n-------------------------------------\n_CoreTools Loaded:\tSUCCESS\nVersion:\t' + moduleVersion + '\n-------------------------------------\n')






