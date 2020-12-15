from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,sys
from datetime import datetime
from random import *
from _CoreTools import *
moduleVersion = '1.5.0.1P'

class BingRewards:
    def __init__(self,driver):
        self.driver = driver

    def exceptionText(functionName,e):
        return '\n---------------------------\nEXCEPTION\n---------------------------\nFile:\t_BingRewards\nFunction:\t' + str(functionName) + '\n' + str(e)

    def Start(self):
        try:
            driver = self.driver
            ct(driver).CloseOtherTabs()
            driver.get('http://bing.com/rewards')
            time.sleep(randint(7,12))
            driver.switch_to.window(driver.window_handles[0])
            print('Finding Daily Links')
            #Base Assertion
            #assert BingRewards(driver).RPageLinkCycle(xpath='//div[@class="c-card-content"]/card-content/mee-rewards-daily-set-item-content/div/div/a'),'RPageLinkCycle() Failed'

            #New Assertion
            assert BingRewards(driver).RPageLinkCycle(xpath='//div[@class="c-card-content"]/card-content/mee-rewards-daily-set-item-content/div/mee-rewards-points/div/div/span[contains(@class,"mee-icon-AddMedium")]/../../../../div/a'),'RPageLinkCycle() Failed'
            
            print('Finding Past Links')
            #Base Assertion
            #assert BingRewards(driver).RPageLinkCycle(xpath='//mee-rewards-more-activities-card-item/div[@mee-rewardable=""]/div/a[@mee-call-to-action="lightweight"]'),'RPageLinkCycle() Failed'

            #New Assertion
            assert BingRewards(driver).RPageLinkCycle(xpath='//mee-rewards-more-activities-card-item/div/mee-rewards-points/div/div/span[contains(@class,"mee-icon-AddMedium")]/../../../../../div[@mee-rewardable=""]/div/a[@mee-call-to-action="lightweight"]'),'RPageLinkCycle() Failed'

        
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.Start',e))
            return False
        return True        


    def RPageLinkCycle(self,xpath):
        driver = self.driver
        
        try:
            links = driver.find_elements_by_xpath(xpath)
        
            for link in links:

                ct(driver).CloseOtherTabs()
            
                print('Clicking Link')
                    
                if(ct(driver).SafeClickL(link)):
                    time.sleep(randint(4,6))

                    print('Switching to Link Window/Tab')
                    driver.switch_to.window(driver.window_handles[1])

                    BingRewards(driver).ClosePlugInBox()



                          
                    if(ct(driver).XpathV('//h2[text()="Supersonic quiz"]')  ):
                        print(r'Running:' + '\t' + r'SupersonicQuiz()')
                        BingRewards(driver).SupersonicQuiz()

                    #This or That 1
                    elif(ct(driver).XpathV('//h2[@class="b_topTitle"][text()="This or That?"]') ):
                        print(r'Running:\t' + r'This or That')
                        BingRewards(driver).ThisOrThat()




                    #HomePage Quiz
                    elif (ct(driver).XpathV('//div[contains(text(),"Bing homepage quiz")]') or
                            (ct(driver).XpathV('//span[@class="wk_Circle"][text()="A"]') and 
                            ct(driver).XpathV('//span[@class="wk_Circle"][text()="B"]')) ):
                        print(r'Running:' + '\t' + r'BingQuiz()')
                        BingRewards(driver).BingQuizABC()
              ## Done          
                    elif(ct(driver).XpathV('//h2[text()="Lightspeed quiz"]') ):
                        print(r'Running:\t' + r'Lightspeed Quiz')
                        BingRewards(driver).LightspeedQuiz()

                    #Guess the Author
                    elif (ct(driver).XpathV('//div[@id="quizWelcomeContainer"]/div[@class="rqText"][contains(text(),"guess the author")]') ):
                        print(r'Running:' + '\t' + r'True or False')
                        BingRewards(driver).GeneralQuiz()

                    #True or False
                    elif (ct(driver).XpathV('//div[@id="quizWelcomeContainer"]/div[@class="rqText"][contains(text(),"fact from fiction")]') ):
                        print(r'Running:' + '\t' + r'True or False')
                        BingRewards(driver).GeneralQuiz()


                    #Reward Poll  
                    elif (ct(driver).XpathV('//div[text()="Today\'s Rewards poll"]')):
                        print(r'Running:' + '\t' + r'DailyPoll()')
                        BingRewards(driver).DailyPoll()


                    #Reward Poll 2
                    elif(ct(driver).XpathV('//div[@id="btoption0"]') and ct(driver).XpathV('//div[@id="btoption1"]')):
                        print(r'Running:\t' + r'Option 1 or Option 2')
                        BingRewards(driver).DailyPoll()

                    #Catch All
                    elif (ct(driver).XpathV('//*[@id="rqStartQuiz"]')):
                        BingRewards(driver).GeneralQuiz()
                        pass
                    
                    time.sleep(randint(4,8))
                ct(driver).CloseOtherTabs()
                print('\n-------------Cycle End-------------\n')
                         
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.RPageLinkCycle',e))
            return False
        return True


    def GeneralQuiz(self):
        driver = self.driver
        try:
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))
            driver.find_element_by_id('rqStartQuiz').click()

            while 1==1:
                time.sleep(randint(3,6))
                rng = randint(0,1)
                driver.find_element_by_id('rqAnswerOption' + str(rng) ).click()

                time.sleep(randint(3,6))
                if (ct(driver).HasText('//span[@id="rqAnsStatus"]','try again') and rng == 0):
                    driver.find_element_by_id('rqAnswerOption1' ).click()
                elif (ct(driver).HasText('//span[@id="rqAnsStatus"]','try again') and rng == 1):
                    driver.find_element_by_id('rqAnswerOption0' ).click()
                else:
                    pass

                
                time.sleep(randint(3,6))
                
                if  ct(driver).HasText('//div[@id="quizCompleteContainer"]/div/div[@class="headerMessage"]','you just earned') :
                    time.sleep(randint(3,6))
                    break
                    
                if not ct(driver).XpathV('//*[@id="rqAnswerOption0"]'):
                    time.sleep(randint(3,6))
                    break




        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.TrueOrFalse',e))
            return False

        finally:
            time.sleep(randint(3,6))
            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))
            

    def LightspeedQuiz(self):
        try:
            driver = self.driver
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))
            driver.find_element_by_id('rqStartQuiz').click()
            questionNum = int(driver.find_element_by_xpath('//span[@class="rqText"]/span[@class="rqPoints"]').text.replace( r'/',r'').replace(r' ',r'')) /10
            questionNum = int(questionNum)

            for h in range(0,questionNum):
                print('Supersonic Cycle:\t' + str(h))
                for i in range(0,4):
                    print('Clicking:\trqAnswerOption' + str(i))
                    ct(driver).SafeClick('//input[@id="rqAnswerOption' + str(i) + '"]')
                    time.sleep(randint(3,6))
                    if (driver.find_element_by_xpath('//span[@id="rqAnsStatus"]').text != r'Oops, try again!'):
                        break
                    time.sleep(randint(4,7))

            
            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))
        except Exception as e:
           raise ValueError(BingRewards.exceptionText('BingRewards.LightspeedQuiz',e))
           return False

  
 
    def DailyPoll(self):
        driver = self.driver
        try:
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))
            rng = randint(0,1)
            ct(driver).SafeClick('//div[@id="btoption' + str(rng) + '"]/div/div[@class="bt_PollRadio"]')
            
            time.sleep(randint(3,6))
            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))
        except Exception as e:
           raise ValueError(BingRewards.exceptionText('BingRewards.DailyPoll',e))
           return False



    def BingQuizABC(self):
        try:
            driver = self.driver
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))
            if (not ct(driver).XpathV('//a[text()="Check your dashboard for more ways to earn."]')):
                refreshCounter = 5
                while (1==1):
                    refreshCounter -= 1
                    rng=randint(1,3)
                    if (rng==1):
                        if (ct(driver).SafeClick('//span[@class="wk_Circle"][text()="A"]')):
                            refreshCounter = 5
                        time.sleep(randint(3,6))
                    elif(rng==2):
                        if(ct(driver).SafeClick('//span[@class="wk_Circle"][text()="B"]')):
                            refreshCounter = 5
                        time.sleep(randint(3,6))
                    else:
                        if(ct(driver).SafeClick('//span[@class="wk_Circle"][text()="C"]')):
                            refreshCounter = 5
                        time.sleep(randint(3,6))
                    

                    if (ct(driver).SafeClick('//input[@type="submit"][@value="Next question"]')):
                        refreshCounter = 5
                    if (ct(driver).SafeClick('//input[@type="submit"][@value="Get your score"]')):
                        break
                    time.sleep(randint(3,6))
                    if (refreshCounter == 0):
                        driver.refresh()

            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))

        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.BingQuizABC',e))
            return False


        
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.LightspeedQuiz',e))
            return False

     
    def ThisOrThat(self):
        try:
            driver = self.driver
        
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))


            driver.find_element_by_xpath('//input[@type="button"][@value="Start playing"]').click()
            for x in range(0,10):
                time.sleep(randint(5,9))
                randomGuess = randint(1,2)

                if randomGuess == 1:
                    if (not ct(driver).SafeClick('//div[@id="rqAnswerOption0"]')):
                        break
                    
                elif randomGuess == 2:
                    if (not ct(driver).SafeClick('//div[@id="rqAnswerOption1"]')):
                        break
                
            time.sleep(randint(4,7))
            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))             

        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.ThisOrThat',e))
            return False       
        return True



    def SupersonicQuiz(self):
        try:
            driver = self.driver
            runQuiz = True
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(randint(3,6))
            driver.find_element_by_xpath('//input[@type="button"][@value="Start playing"]').click()
            time.sleep(randint(3,6))
            questionNum = int(driver.find_element_by_xpath('//span[@class="rqECredits"]').text.replace(r'"',r'').replace(r' ',r''))/10
            questionNum = int(questionNum)
        
            while (runQuiz):
                for i in range(0,8):
                    if (ct(driver).XpathV('//*[contains(text(),"you just earned")]') or
                        ct(driver).XpathV('//*[contains(text(),"You just earned")]')):
                        print('\n\n------------------Quiz Completed------------------\n\n')
                        runQuiz = False
                        break
                    print('Clicking:\trqAnswerOption' + str(i))
                    ct(driver).SafeClick('//div[@id="rqAnswerOption' + str(i) + '"]')
                    time.sleep(randint(2,4))
                    #   rqAnswerOption0
   
            ct(driver).CloseOtherTabs()
            time.sleep(randint(3,6))
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.SupersonicQuiz',e))
            return False
        return True

    def ClosePlugInBox(self):
        try:
            driver = self.driver
            time.sleep(randint(3,6))
            ct(driver).SafeClick('//*[@id="bnp_hfly_cta2"]')
            time.sleep(randint(3,6))
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingRewards.ClosePlugInBox',e))
            return False
        return True


print('\n-------------------------------------\nBingRewards Load:\tSuccess\t' + moduleVersion + '\n-------------------------------------\n')

#Debug
#driverPath = '../../../Drivers/'
#driver = webdriver.Edge(executable_path= driverPath + 'msedgedriver.exe')










    

