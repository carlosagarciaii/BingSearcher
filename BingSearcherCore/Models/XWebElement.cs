using System;
using System.Collections.Generic;
using System.Text;

namespace BingSearcherCore.Models
{
    public class XWebElement
    {

        private string identifier;
        public string Identifier { get { return identifier; } set { identifier = value; } }

        private string type;
        public string Type { get { return type; } set { type = value; } }

        private string action;
        public string Action { get { return action; } set { action = value; } }

        private bool required;
        public bool Required { get { return required; } set { required = value; } }



        /// <summary>
        /// <para>Identifier = the ID, Xpath, CSS, etc required to identify the element</para>
        /// <para>Type = the type (IE: ID, CSS, Name, XPath)</para>
        /// <para>Action = What action to take</para>
        /// <para>Required = Is this a prerequisite for the next step</para>
        /// </summary>
        public XWebElement(string identifier,string type,string action, bool required = false)
        {
            identifier = this.identifier;
            type = this.type;
            action = this.action;
            required = this.required;

        }

    }
}
