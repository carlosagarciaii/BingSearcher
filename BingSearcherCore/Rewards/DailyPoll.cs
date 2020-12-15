using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;
using OpenQA.Selenium;

namespace BingSearcherCore.Rewards
{
    public class DailyPoll
    {


        string CurrentFileName = new StackTrace(true).GetFrame(0).GetFileName();
        Tools tools = new Tools();
        Random rand = new Random();

        string pollOptionsXpath = "//div[@class='TriviaOverlayData']//div[starts-with(@id,'btoption')][@role='radio']";

        List<IWebElement> pollOptionElements = new List<IWebElement>();


        /// <summary>
        /// <para>This checks if the criteria for the Daily Poll is met.</para>
        /// <para>driver = the IWebDriver to use</para>
        /// </summary>
        /// <returns>True if criteria is met, otherwise False.</returns>
        public bool CheckCriteria(IWebDriver driver)
        {
            bool criteriaMatch = false;
            foreach (var element in driver.FindElements(By.XPath(pollOptionsXpath)))
            {
                pollOptionElements.Add(element);
            }
            if (pollOptionElements.Count > 1)
            {
                criteriaMatch = true;
            }

            return criteriaMatch;
        }


        public bool Run(IWebDriver driver,int maxQuestions = 30)
        {

            return true;
        }


    }
}
