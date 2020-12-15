using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;
using OpenQA.Selenium;


namespace BingSearcherCore.Rewards
{
	public class RewCycler
	{
		string CurrentFileName = new StackTrace(true).GetFrame(0).GetFileName();
		Tools tools = new Tools();
		Random rand = new Random();
		CommonQuiz cq = new CommonQuiz();
		ABCQuiz aq = new ABCQuiz();
		DailyPoll dp = new DailyPoll();

		
		public bool Run(IWebDriver driver)
		{
			IReadOnlyCollection<IWebElement> elements = new List<IWebElement>();
			string locatorText = "//span[contains(@class,'mee-icon-AddMedium')]/ancestor::mee-card//div[contains(@class,'x-hidden-vp1')]/a";
			By locator = By.XPath(locatorText);

			elements = driver.FindElements(locator);

			foreach (var element in elements)
			{
				element.Click();
				try
				{
					driver.SwitchTo().Window(driver.WindowHandles[1]);
				}
				catch
				{
					throw new Exception($"File:\t{CurrentFileName}  \nThe target tab was not opened or does not exist. Unable to proceed.\n");
				}


				if (aq.CheckCriteria(driver))
				{
					aq.Run(driver);
				}
				else if(cq.CheckCriteria(driver)){
					cq.Run(driver);
				}
				else if (dp.CheckCriteria(driver))
				{
					dp.Run(driver);
				}


			}


			return true;
		}


		/*
		 
			This was confirmed in FF as unprocessed Reward
			//span[contains(@class,"mee-icon-AddMedium")]/ancestor::mee-card//a
			
			All items should be under this heading
			//div[@class='TriviaOverlayData']//
		  
		 */

	}
}
