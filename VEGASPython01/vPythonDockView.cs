using System;
using System.Collections.Generic;
using System.Text;
using ScriptPortal.Vegas;
using System.Windows.Forms;

namespace VegasPython
{
    [System.ComponentModel.DesignerCategory("Code")]
    public class vPythonDockView : DockableControl
    {
        public vPythonForm vPF;

        public vPythonDockView(string name, vPythonForm vPF)
            : base(name)
        {
            this.vPF = vPF;
            this.SetStyle(ControlStyles.ContainerControl, true);
 //           this.AutoScroll = true;
            this.PersistDockWindowState = true;
            Controls.Add(this.vPF);
            DefaultFloatingSize = new System.Drawing.Size(vPF.Width, vPF.Height);
        }
    }
}
