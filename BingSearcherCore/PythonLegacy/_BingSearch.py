from selenium import webdriver
import time,os,sys,logging,datetime
from random import *
from _BingSearchWordList import *
from _CoreTools import *
moduleVersion = '1.5.0.1P'

class BingSearcher:
    def __init__(self,driver):
        self.driver = driver
    
    
    def exceptionText(functionName,e):
        return '\n---------------------------\nEXCEPTION\n---------------------------\nFile:\t_BingSearch\nFunction:\t' + str(functionName) + '\n' + str(e)



    def Start(self,loops =  50):
        try:
            driver = self.driver
            print('Navigating to Bing.com')
            driver.get('http://bing.com')
            time.sleep(randint(4,10))

            for i in range(0,loops):
                if (ct(driver).XpathV('//Input[@type="search"]')):
                    driver.find_element_by_xpath('//Input[@type="search"]').clear()
                    time.sleep(randint(2,4))
                    driver.find_element_by_xpath('//Input[@type="search"]').send_keys(BingSearchWL.BingStringConcat())
                    time.sleep(randint(4,6))
                if (ct(driver).XpathV('//label[@for="sb_form_go"]')):
                    driver.find_element_by_xpath('//label[@for="sb_form_go"]').click()
                elif (ct(driver).XpathV('//Input[@type="submit"]')):
                    driver.find_element_by_xpath('//Input[@type="submit"]').click()
                else:
                    print('_BingSearch Stopped due to loop error')    
                time.sleep(10)
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingSearcher.Start',e))
            return False
        return True



print('\n-------------------------------------\n_BingSearch Loaded Successfully' + moduleVersion + '\n-------------------------------------\n')



