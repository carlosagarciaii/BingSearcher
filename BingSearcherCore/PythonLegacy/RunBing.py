from selenium import webdriver
import pandas as pd
from random import *
import time, logging, os, traceback, sys, pyautogui,math
from datetime import datetime


delayHours=0
for argument in sys.argv:
    if r'-d:' in str(argument).lower():
        strRight = len(str(argument))-3
        
        
        delayHours = float(argument[-strRight:])

print('Delaying Start:\t' + str(delayHours) + '_hrs')
time.sleep(int(delayHours * 60 * 60))


moduleVersion = '1.5.0.1P'

print('--------------------------------\nStarting:\t'  + os.path.basename(__file__) + '\nVersion:\t' + moduleVersion + '\n--------------------------------\n\n')

DEBUG_MODE = False

if DEBUG_MODE:
    print('--------------------------------\nDEBUG MODE:\tACTIVE\n--------------------------------\n\n')

#Logging

loggingDir = os.path.dirname(os.path.abspath(__file__)) + "/Logging/"

if (not os.path.exists(loggingDir)):
    os.mkdir(loggingDir)

logging.basicConfig(filename=loggingDir + os.path.basename(__file__) + '_diagnostic.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
vLoggingSegmenter = "Closing Log\n\n________________________________________________________\n________________________________________________________\n\n"

if not os.path.isdir('./Drivers'):
    os.mkdir('./Drivers')
    print('Drivers Directory Created')
else:
    print('Drivers Directory Exists')

if os.path.isfile('./Drivers/msedgedriver.exe'):
    driverPath = 'Drivers/'
    print('Found In Live:\t' + driverPath)
elif os.path.isfile('../../../Drivers/msedgedriver.exe'):
    driverPath = '../../../Drivers/'
    print('Found In Dev:\t' + driverPath)
elif os.path.isfile(r'C:/ProgramData/SeleniumDrivers/msedgedriver.exe'):
    driverPath = r'C:/ProgramData/SeleniumDrivers/msedgedriver.exe'
    print('Found In Dev:\t' + driverPath)
else:
    print('Driver Not Found')

    

def BrowserKicker(browser):
    if (browser.lower() == "chrome" or browser.lower() == "google"):
        driver = webdriver.Chrome(executable_path= driverPath + 'chromedriver.exe')
    elif browser.lower() == "edge" :
        driver = webdriver.Edge(executable_path= driverPath + 'msedgedriver.exe')
    elif (browser.lower() == "ie" or browser.lower() == "explorer" or browser.lower() == "iexplore"):
        driver = webdriver.Ie(executable_path= driverPath + 'IEDriverServer.exe')
    elif (browser.lower() == "firefox" or browser.lower() == "ff" or browser.lower() == "mozilla"):
        driver = webdriver.Firefox(executable_path= driverPath + 'geckodriver.exe')
    return driver

#Set Browser
#xxBrowser = pyautogui.confirm(text='Select a Browser to Use',title='Browser to Use',buttons=('IE','Edge','FireFox','Chrome','Quit'))



if os.path.isfile('./bingSearchConf.xlsx'):
    targetXLS = 'bingSearchConf.xlsx'
elif os.path.isfile(r'C:/ProgramData/SeleniumDrivers/bingSearchConf.xlsx'):
    targetXLS = r'C:/ProgramData/SeleniumDrivers/bingSearchConf.xlsx'


if not os.path.isfile(targetXLS):
    xldf = pd.DataFrame({'UserName':[],'Password':[],'LastSearch':[],'LastRewards':[]})
    xldf.to_excel(targetXLS,columns=['UserName','Password','LastSearch','LastRewards'])
    print('Excel File did not exist and was created.\nPlease add users to file:\n\t' + targetXLS)
    sys.exit()

#Pulling the Excel Info    
try:
    xldf = pd.read_excel(targetXLS).copy()
    
    pd.options.mode.chained_assignment = None 
    xldf.set_index('UserName')
    rowCount = len(xldf)
    if 'CurrentPoints' not in xldf.columns:
        xldf['CurrentPoints'] = r''
        
    if 'GiftCards' not in xldf.columns:
        xldf['GiftCards'] = r''
    
except Exception as e:
    
    errMsg = '-------------------------\n\tException\n-------------------------\n\nIt is possible the the Excel Sheet is Corrupt'
    print(errMsg)
    raise ValueError(errMsg + str(e))
    sys.exit()

for x in range(0,rowCount):

    MasterUser = str(xldf['UserName'][x]).replace(' ','')
    MasterPass = str(xldf['Password'][x]).replace(' ','')

    print('User' + str(x) + ':\t' + MasterUser + '\nPass:\t' + MasterPass + '\n' )


    #driver = BrowserKicker(xxBrowser)
    driver = BrowserKicker('edge')

    from _BingLogin import *
    if not DEBUG_MODE:
        BingLogin(driver).Login(MasterUser,MasterPass)

    try:
        from _BingRewards import *
        print('Starting Bing Rewards')
        if not DEBUG_MODE:
            BingRewards(driver).Start()
            pass

        logTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        xldf['LastRewards'][x] = str(logTime)
        
    except Exception as e:
        print('\n-----------------------------\nEXCEPTION\n-----------------------------\n' + str(e))
        logTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        xldf['LastRewards'][x] = 'FAIL - ' + str(logTime)
        

    
    try:
        from _BingSearch import *
        print('Starting Bing Search')
        if not DEBUG_MODE:
            BingSearcher(driver).Start()
            pass
            
        from datetime import datetime
        logTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        xldf['LastSearch'][x] = str(logTime)
        
    except Exception as e:
        print('\n-----------------------------\nEXCEPTION\n-----------------------------\n' + str(e))
        try:
            from datetime import datetime
            logTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            xldf['LastSearch'][x] = 'FAIL - ' + str(logTime)
        except:
            print('Failed to write log to sheet')

    try:
        print('Getting Current Point Total for ' + xldf['UserName'][x])

        driver.get('http://bing.com')
        time.sleep(3)
        CurrentPointTotal = driver.find_element_by_xpath('//span[@id="id_rc"]').text
        retryCount = 0
        while not CurrentPointTotal.isnumeric():
            driver.refresh()
            time.sleep(3)
            CurrentPointTotal = driver.find_element_by_xpath('//span[@id="id_rc"]').text
            retryCount +=1
            if retryCount > 5:
                break
        xldf['CurrentPoints'][x] = CurrentPointTotal
        print('User:\t' + xldf['UserName'][x] + '\nPoints:\t' + str(CurrentPointTotal))
        xldf['GiftCards'][x] = math.trunc(float(CurrentPointTotal) / 5250)
        
    except:
        print('Failed to pull points for ' + xldf['UserName'][x])

    xldf.to_excel(targetXLS,columns=['UserName','Password','CurrentPoints','GiftCards','LastSearch','LastRewards'])

    
    while 1==1:
        try:
            driver.quit()
            time.sleep(3)
            os.system('taskkill /F /T /IM conhost.exe')
            os.system('taskkill /F /IM msedgedriver.exe')
            
        except:
            break
    time.sleep(randint(350,610)) # 300 sec = 5 min

    

        




