using System;
using System.Collections.Generic;
using System.Text;

namespace BingSearcherCore._POC
{
    public class poc
    {
        List<string> testList = new List<string>();

        public poc()
        {
            testList.Add("value 1");
            testList.Add("value 2");
            testList.Add("value 3");
            testList.Add("value 4");
        }

        public void Go()
        {
            foreach (var item in testList)
            {
                Console.WriteLine(item);
            }
        }

    }
}
