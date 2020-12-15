using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;
using OpenQA.Selenium;

namespace BingSearcherCore.Rewards
{
    public class CommonQuiz
    {
        string CurrentFileName = new StackTrace(true).GetFrame(0).GetFileName();
        Tools tools = new Tools();
        Random rand = new Random();

        List<string> startQuizXpath = new List<string>(); 

        public CommonQuiz()
        {

            startQuizXpath.Add("//*[@id='rqStartQuiz']");
            startQuizXpath.Add("//input[@type='button'][@value='Start playing']");

        }



        /// <summary>
        /// <para>This checks if the criteria for most quizzes is met.</para>
        /// <para>driver = the IWebDriver to use</para>
        /// </summary>
        /// <returns>True if criteria is met, otherwise False.</returns>
        public bool CheckCriteria(IWebDriver driver)
        {
            bool criteriaMatch = false;
            foreach (string item in startQuizXpath)
            {
                criteriaMatch = tools.ElementsFound(driver, item);
                if (criteriaMatch)
                {
                    break;
                }


            }

            return criteriaMatch;
        }


        /// <summary>
        /// <para>This runs the standard quiz</para>
        /// <para>driver = the IWebDriver being used</para>
        /// <para>maxQuestions = the max number of cycles to run. (Default: 30 | Prevents endless loops)</para>
        /// </summary>
        /// <returns>true if success</returns>
        public bool Run(IWebDriver driver,int maxCycles = 30)
        {
            IWebElement element;
            By locator;
            string locateByText;
            List<string> answerOptions = new List<string>();
            string answerOptionPrefix = "rqAnswerOption";
            int optionSelected = 0;

            string weAreDoneText = "//div[contains(text(),'You just earned')]";


            try
            {
                driver.SwitchTo().Window(driver.WindowHandles[1]);
            }
            catch
            {
                throw new Exception($"File:\t{CurrentFileName}  \nThe target tab was not opened or does not exist. Unable to proceed.\n");
            }


            if (tools.ElementFoundOr(driver, startQuizXpath)) 
            {
                driver.FindElement(By.Id("rqStartQuiz")).Click();
            }
             else if (tools.ElementFound(driver,By.XPath("//input[@type='button'][@value='Start playing']")))
            {
                driver.FindElement(By.XPath("//input[@type='button'][@value='Start playing']")).Click();

            }
            else
            {
                return false;
            }

            tools.RSleep();

            for (int i = 0;i < maxCycles; i++)
            {
                if (tools.ElementFound(driver, By.XPath(weAreDoneText)))
                {
                    break;
                }
                answerOptions.Clear();
                answerOptions = tools.GetOptionsByID(driver, answerOptionPrefix);

                do
                {
                    optionSelected = rand.Next(0, answerOptions.Count);
                    locateByText = answerOptions[optionSelected];
                    locator = By.Id(locateByText);
                    element = tools.WaitForElement(driver,locator);
                    element.Click();
                    
                    answerOptions.RemoveAt(optionSelected);
                    tools.RSleep();

                }
                while (answerOptions.Count > 0);
            }


            return true;
        }





    }
}
