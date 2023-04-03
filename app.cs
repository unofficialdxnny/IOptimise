using System;
using System.Windows.Forms;

namespace BlankWindowApp
{
    class BlankWindow : Form
    {
        public BlankWindow()
        {
            // Set window properties
            this.Text = "Blank Window";
            this.Width = 1200;
            this.Height = 600;
            this.StartPosition = FormStartPosition.CenterScreen;
        }

        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new BlankWindow());
        }
    }
}
