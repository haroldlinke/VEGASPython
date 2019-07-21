
using ScriptPortal.MediaSoftware.Skins;

namespace VegasPython
{
    partial class vPythonForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            CheckForIllegalCrossThreadCalls = false;
            this.vPythonInputBox = new ScriptPortal.MediaSoftware.Skins.TextBox();
            this.vPythonOutputBox = new ScriptPortal.MediaSoftware.Skins.TextBox();
            this.vPythonSplitContainer = new System.Windows.Forms.SplitContainer();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openScriptToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveScriptToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.executeScriptToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.vScrollbar1 = new ScriptPortal.MediaSoftware.Skins.VScrollBar();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.executeScriptToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(421, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openScriptToolStripMenuItem,
            this.saveScriptToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // openScriptToolStripMenuItem
            // 
            this.openScriptToolStripMenuItem.Name = "openScriptToolStripMenuItem";
            this.openScriptToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.openScriptToolStripMenuItem.Text = "Open Script";
            this.openScriptToolStripMenuItem.Click += OpenFile_Click;
            // 
            // saveScriptToolStripMenuItem
            // 
            this.saveScriptToolStripMenuItem.Name = "saveScriptToolStripMenuItem";
            this.saveScriptToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.saveScriptToolStripMenuItem.Text = "Save Script";
            this.saveScriptToolStripMenuItem.Click += SaveScript_Click;
            // 
            // executeScriptToolStripMenuItem
            // 
            this.executeScriptToolStripMenuItem.Name = "executeScriptToolStripMenuItem";
            this.executeScriptToolStripMenuItem.Size = new System.Drawing.Size(92, 20);
            this.executeScriptToolStripMenuItem.Text = "Execute VEGASPython Script";
            this.executeScriptToolStripMenuItem.Click += ExecuteScript_Click;
            // 
            // vScrollbar1
            // 
            this.vScrollbar1.Dock = System.Windows.Forms.DockStyle.Right;

            // 
            // vPythonSplitContainer
            // 

            this.vPythonSplitContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            //           this.vPythonInputBox.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Bottom);
            // this.vPythonSplitContainer.Location = new System.Drawing.Point(0, 24);
            this.vPythonSplitContainer.Name = "vPythonSplitContainer";
            // this.vPythonSplitContainer.Size = new System.Drawing.Size(421, 406);
            this.vPythonSplitContainer.TabIndex = 1;
            this.vPythonSplitContainer.Panel1MinSize = 30;
            this.vPythonSplitContainer.Panel2MinSize = 30;
            //this.vPythonSplitContainer.SplitterDistance = 79;
            //this.vPythonSplitContainer.SplitterIncrement = 10;
            this.vPythonSplitContainer.SplitterWidth = 10;
            this.vPythonSplitContainer.Orientation = System.Windows.Forms.Orientation.Horizontal;
            //            this.vPythonInputBox.AutoSize = true;
            //            this.vPythonInputBox.Controls.Add(vScrollbar1);

            // 
            // vPythonInputBox
            // 

            this.vPythonInputBox.Dock = System.Windows.Forms.DockStyle.Fill;
 //           this.vPythonInputBox.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Bottom);
            this.vPythonInputBox.Location = new System.Drawing.Point(0, 24);
            this.vPythonInputBox.Multiline = true;
            this.vPythonInputBox.Name = "vPythonInputBox";
            this.vPythonInputBox.Size = new System.Drawing.Size(421, 406);
            this.vPythonInputBox.TabIndex = 1;
//            this.vPythonInputBox.AutoSize = true;
            this.vPythonInputBox.WordWrap = false;
            this.vPythonInputBox.ScrollBars = System.Windows.Forms.ScrollBars.Both;
//            this.vPythonInputBox.Controls.Add(vScrollbar1);
            // 
            // textBox2
            // 
            this.vPythonOutputBox.Dock = System.Windows.Forms.DockStyle.Fill;
//            this.vPythonOutputBox.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right | System.Windows.Forms.AnchorStyles.Left| System.Windows.Forms.AnchorStyles.Top);
            this.vPythonOutputBox.Location = new System.Drawing.Point(0, 214);
            this.vPythonOutputBox.Multiline = true;
            this.vPythonOutputBox.Name = "vPythonOutputBox";
            this.vPythonOutputBox.ReadOnly = true;
            this.vPythonOutputBox.Size = new System.Drawing.Size(421, 216);
            this.vPythonOutputBox.TabIndex = 2;
 //           this.vPythonOutputBox.AutoSize = true;
            this.vPythonOutputBox.WordWrap = false;
            this.vPythonOutputBox.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
 //           this.ClientSize = new System.Drawing.Size(421, 622);
            this.AutoSize = true;
            this.vPythonSplitContainer.Panel1.Controls.Add(this.vPythonInputBox);
            this.vPythonSplitContainer.Panel2.Controls.Add(this.vPythonOutputBox);
            this.Controls.Add(vPythonSplitContainer);
            this.Controls.Add(this.menuStrip1);
            this.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Top);
            this.Name = "VEGASPythonForm";
            this.Text = "VEGASPythonForm1";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();            // 
 
        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openScriptToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveScriptToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem executeScriptToolStripMenuItem;
        private System.Windows.Forms.SplitContainer vPythonSplitContainer;
        public ScriptPortal.MediaSoftware.Skins.TextBox vPythonInputBox;
        public ScriptPortal.MediaSoftware.Skins.TextBox vPythonOutputBox;
        private ScriptPortal.MediaSoftware.Skins.VScrollBar vScrollbar1;
    }
}

