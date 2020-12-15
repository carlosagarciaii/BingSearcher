using System;
using System.Collections.Generic;
using System.Text;
using OpenQA.Selenium.Edge;
using OpenQA.Selenium;
using System.IO;


namespace BingSearcherCore
{
    public class Login
    {
        private IWebDriver driver { get; set; }
        private Random rand = new Random();
        private Tools tools = new Tools();

        // Config
        private const string BingLoginURL = "https://login.live.com";
        private const string MSWebDriverLoc = @"C:\Users\xenor\Documents\Scripts\Bing\Selenium\Drivers\";


        public bool Start(string userName,string password)
        {
            if (userName == string.Empty)
            {
                throw new Exception("''username'' cannot be blank. Please provide a username and password.");
            }

            if (password == string.Empty)
            {
                throw new Exception("''password'' cannot be blank. Please provide a username and password.");
            }


            //System.setProperty("webdriver.edge.driver", "C:\\Users\\xenor\\Documents\\Scripts\\Bing\\Selenium\\Drivers\\msedgedriver.exe");

            if (CheckIfDriverExists()) { 


                driver = new EdgeDriver(MSWebDriverLoc);
                driver.Url = BingLoginURL;

                By locator = null; //Instantiating. Will be assigned throughout script
                IWebElement element = null; //same as above
                string locateByTxt;


                // Sleep to mimic user hesitation
                tools.RSleep();
                tools.WaitForHTMLLoad(driver); //Added as troubleshooting for page not loading.



            // Find Login Button and Populate UserName.
                locateByTxt = "loginfmt";
                locator = By.Name(locateByTxt);

                element = tools.WaitForElement(driver, locator);
                if (element != null)
                {
                    element.SendKeys(userName);
                }
                else
                {
                    throw new Exception(locateByTxt + " could not be found. \n\tCould Not Find Login Prompt.");
                }

                tools.RSleep();

            // Find Submit Button and Click It.
                locateByTxt = "//Input[@type='submit']";
                locator = By.XPath(locateByTxt);
                element = tools.WaitForElement(driver, locator);
                if (element != null)
                {
                    element.Click();
                    
                }
                else
                {
                    throw new Exception(locateByTxt + " could not be found.\n\tCould Not Find the Submit Button");
                }

                tools.RSleep();

            // Find Password Button and Populate UserName.
                locator = By.Name("passwd");

                element = tools.WaitForElement(driver, locator);
                if (element != null)
                {
                    element.SendKeys(password);
                }
                else
                {
                    throw new Exception("loginfmt could not be found. \n\tCould Not Find Password Input Field.");
                }

                tools.RSleep();

            // Find Submit Button and Click It.
                locator = By.XPath("//Input[@type='submit']");
                element = tools.WaitForElement(driver, locator);
                if (element != null)
                {
                    element.Click();
                }
                else
                {
                    throw new Exception(locateByTxt + " could not be found.\n\tCould Not Find the Submit Button");
                }

                 tools.RSleep();

            // Do you want to stay logged in?
            // AutoAnswer No. 
                locator = By.XPath("//Input[@value='No']");
                element = tools.WaitForElement(driver, locator);
                if (element != null)
                {
                    element.Click();
                    tools.RSleep();
                }






                return true;
            }
            else
            {

                Console.WriteLine("Could not locate MicrosoftWebDriver.exe ");
                return false;
            }

        }
        public bool CheckIfDriverExists()
        {
            if (File.Exists(MSWebDriverLoc + "MicrosoftWebDriver.exe"))
            {

                return true;
            }
            else if (File.Exists(MSWebDriverLoc + "msedgedriver.exe"))
            {
                File.Copy(MSWebDriverLoc + "msedgedriver.exe", MSWebDriverLoc + "MicrosoftWebDriver.exe");
                return true;
            }
            else
            {

                return false;
            }
        }

            
    }
}
