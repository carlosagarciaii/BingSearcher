using System;
using BingSearcherCore;
using BingSearcherCore._POC;
using System.Text.RegularExpressions;

namespace RunBingSearcher
{
    class Program
    {
        static void Main(string[] args)
        {
            string userName = string.Empty;
            string password = string.Empty;
            Regex userRgx = new Regex(@"(?<=/u[:])\w+",RegexOptions.IgnoreCase);
            Regex passRgx = new Regex(@"(?<=/u[:])\w+",RegexOptions.IgnoreCase);

            foreach (var arg in args)
            {
                if (userRgx.IsMatch(arg))
                {
                    userName = userRgx.Match(arg).ToString();
                }
                else if (passRgx.IsMatch(arg))
                {
                    password = passRgx.Match(arg).ToString();
                }
            }

            Login login = new Login();
            bool RunComplete;
            Console.WriteLine("Hello World!");
            RunComplete = login.Start(userName: userName, password: password);


        }
    }
}
