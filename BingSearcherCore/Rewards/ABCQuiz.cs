using OpenQA.Selenium;
using System;
using System.Collections.Generic;


namespace BingSearcherCore.Rewards
{
    public class ABCQuiz
    {

        Tools tools = new Tools();
        Random rand = new Random();
        const string nextQuestionXpath  = "//input[@type='submit'][@value='Next question']";
        const string getYourScoreXpath = "//input[@type='submit'][@value='Get your score']";
        const string doneTextXpath = "//a[text()='Check your dashboard for more ways to earn.']";
        List<string> answerOptionsXpath = new List<string>();


        public ABCQuiz()
        {
            answerOptionsXpath.Add("//span[@class='wk_Circle'][text()='A']");
            answerOptionsXpath.Add("//span[@class='wk_Circle'][text()='B']");
            answerOptionsXpath.Add("//span[@class='wk_Circle'][text()='C']");
            

        }
        /// <summary>
        /// <para>Confirms if the page viewed meets the criteria for the ABC Quiz</para>
        /// <para>driver = the IWebDriver in use</para>
        /// </summary>
        /// <returns>true if the page matches the expected ABC Quiz.</returns>
        public bool CheckCriteria(IWebDriver driver)
        {
            bool quizConfirmed;
            quizConfirmed = tools.ElementsFound(driver, answerOptionsXpath);
            return quizConfirmed;

        }


        /// <summary>
        /// <para>This should run the ABC Quiz module. </para>
        /// <para>driver = the IWebDriver in use</para>
        /// <para>maxQuestions = the max number of questions allowed. (Bing normally only serves 10)</para>
        /// </summary>
        /// <returns>true if success</returns>

        public bool Run(IWebDriver driver, int maxQuestions = 30)
        {
            IWebElement element;
            By locator;
            string locateByTxt;
            int refreshCounter;
            int selectOption;


            refreshCounter = 5;
            try
            {
                driver.SwitchTo().Window(driver.WindowHandles[1]);
            }
            catch
            {
                throw new Exception("File:\tABCQuiz.cs\nThe target tab was not opened or does not exist. Unable to proceed.\n");
            }


            tools.RSleep();

            for (int i = 0; i < maxQuestions; i++)
            {
                locateByTxt = doneTextXpath;
                locator = By.XPath(locateByTxt);

                element = tools.WaitForElement(driver, locator);
                if (element != null){ break; }
                else
                {
                    if (tools.ElementsFound(driver, answerOptionsXpath))
                    {
                        selectOption = rand.Next(0, answerOptionsXpath.Count - 1);
                        locateByTxt = answerOptionsXpath[selectOption];
                        locator = By.XPath(locateByTxt);
                        element = driver.FindElement(locator);
                        element.Click();



                    }
                    else if (tools.ElementFound(driver, By.XPath(nextQuestionXpath)))
                    {
                        locateByTxt = nextQuestionXpath;
                        locator = By.XPath(locateByTxt);
                        element = driver.FindElement(locator);

                    }
                    else if (tools.ElementFound(driver, By.XPath(getYourScoreXpath)))
                    {
                        locateByTxt = getYourScoreXpath;
                        locator = By.XPath(locateByTxt);
                        element = driver.FindElement(locator);

                    }

                    else
                    {
                        refreshCounter--;
                    }

                }
            }
            


            return true;
        }

                    



    }
}
