using System;
using System.Threading;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Diagnostics;
using System.Windows.Forms;
using ScriptPortal.Vegas;
using Python.Runtime;
using System.Web.Script.Serialization;

namespace VegasPython
{
    

    public class VEGASPythonConfig
    {
        public string  PythonPath;
        public string VEGASPythonFolder;
        public Boolean debugmode;
        public string debugprecmd;
        public string debugpostcmd;
        public Boolean debugusereload;

        public VEGASPythonConfig()
        {
            PythonPath      = "";
            VEGASPythonFolder = "\\VEGASPYTHON";
            debugmode       = false;
            debugprecmd     = "";
            debugpostcmd    = "";
            debugusereload  = false;
        }

        public static VEGASPythonConfig Read_config()
        {
            string DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

            string vegaspythonconfigfilename = DLLDirectory + "\\VEGASPython_CONFIG.JSON";
            try
            {
                if (File.Exists(vegaspythonconfigfilename))
                {
                    System.IO.StreamReader file = new System.IO.StreamReader(vegaspythonconfigfilename);
                    string jsondata = file.ReadToEnd();
                    file.Close();

                    return new JavaScriptSerializer().Deserialize<VEGASPythonConfig>(jsondata);

                }
                else
                {
                    return new VEGASPythonConfig();
                }
            }
            catch
            {
                return new VEGASPythonConfig();
            }
        }
    }

    public class VEGASPythonManager
    {
        public static VEGASPythonManager mVegasPythonManager = null;

        private vPythonForm mvpWindowForm = null;
        private Vegas myVegas;

        
        private dynamic PythonModuleImported;
        private string PythonModuleImportedName;

        VEGASPythonConfig mVegasPythonConfigData;

        public VEGASPythonManager( Vegas       pyVegas,
                                   vPythonForm vpWindowForm)
        {
            mvpWindowForm = vpWindowForm;
            myVegas = pyVegas;
            PythonModuleImported = null;
            PythonModuleImportedName = "";
        }

        public void InitializeVEGASPython(Vegas pyVegas,
                                    vPythonForm vpWindowForm)
        {

            if (vpWindowForm != null)
            {
                mvpWindowForm = vpWindowForm;
                            }
            myVegas = pyVegas;
            
            mVegasPythonConfigData = VEGASPythonConfig.Read_config();
        }



        public void ShowError(string title, string name, Exception e)
        {
            if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
            {
                string caption = String.Format(title, name);
                string error = e.ToString();
                mvpWindowForm.vPythonOutputBox.AppendText(error + "\r\n");

                mvpWindowForm.vPythonOutputBox.AppendText("*******************************************\r\n");

                error = e.StackTrace;
                error = error.Replace("\\n", "\r\n");
                mvpWindowForm.vPythonOutputBox.AppendText(error + "\r\n");
            }


        }

        public void ShowMessage(string message)
        {
            if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
            {
                mvpWindowForm.vPythonOutputBox.AppendText("*******************************************\r\n");
                mvpWindowForm.vPythonOutputBox.AppendText(message + "\r\n");
                mvpWindowForm.vPythonOutputBox.AppendText("*******************************************\r\n");
            }

        }

        public void ShowDebugMessage(string message)
        {
            Boolean showdebug = false;
            if (showdebug && (mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
            {
                mvpWindowForm.vPythonOutputBox.AppendText("*DEBUG*************************************\r\n");
                mvpWindowForm.vPythonOutputBox.AppendText(message + "\r\n");
                mvpWindowForm.vPythonOutputBox.AppendText("*******************************************\r\n");
            }

        }

        public void ClearMessage()
        {
            
            if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
            {
                mvpWindowForm.vPythonOutputBox.Clear();
            }

        }

        public string readInputText()
        {
            if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
            {
                return mvpWindowForm.vPythonInputBox.Text;
            }
            else
            {
                return "";
            }

        }


        private void Set_Path_PN(string pFilename)
        {
            ShowDebugMessage("SetPathPN:" + pFilename);
            //string moduleDirectory;

            string moduleName;

            if (pFilename == "")
            {
                //moduleDirectory = "";
                moduleName = "";
            }
            else
            {
                //moduleDirectory = Path.GetDirectoryName(pFilename);

                //moduleName = Path.GetFileNameWithoutExtension(pFilename);
                moduleName = pFilename;
            }

            string DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

            string vegaspythonpath = Environment.GetEnvironmentVariable("PYTHONPATH");

            string path1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.MyDocuments) + "\\Vegas Application Extensions" + mVegasPythonConfigData.VEGASPythonFolder;
            string path2 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.LocalApplicationData) + "\\Vegas Pro\\Application Extensions" + mVegasPythonConfigData.VEGASPythonFolder;
            string path3 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ApplicationData) + "\\Vegas Pro\\Application Extensions" + mVegasPythonConfigData.VEGASPythonFolder;
            string path4 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.CommonApplicationData) + "\\Vegas Pro\\Application Extensions" + mVegasPythonConfigData.VEGASPythonFolder;

            if ((vegaspythonpath == null) || (vegaspythonpath == ""))
            {
                //vegaspythonpath = DLLDirectory + "\\VEGASPython_PN";
                vegaspythonpath = path1; // DLLDirectory;

            }
            else
            {
                //vegaspythonpath = vegaspythonpath + ";" + DLLDirectory + "\\VEGASPython_PN";
                vegaspythonpath = vegaspythonpath + ";" + path1; //+ DLLDirectory;
            }
            vegaspythonpath = vegaspythonpath + ";" + path2 + ";" + path3 + ";" + path4;

            string envPythonHome;
            envPythonHome = DLLDirectory + @"\Python37";

            if (mVegasPythonConfigData.PythonPath != "")
            {
                string PythonPath = mVegasPythonConfigData.PythonPath;

                if (Directory.Exists(PythonPath))
                    envPythonHome = mVegasPythonConfigData.PythonPath;
            }

            string pythonnetpath = Environment.GetEnvironmentVariable("PYTHONNET");
            if ((pythonnetpath == null) || (pythonnetpath == ""))
            {
                pythonnetpath = "";
            }


            string py_sitepackages = envPythonHome + @"\Lib\site-packages";
            string py_dlls = envPythonHome + @"\DLLs";
            string py_lib = envPythonHome + @"\Lib";

            pythonnetpath = pythonnetpath + py_lib + ";" + py_sitepackages + ";" + py_dlls;

            Environment.SetEnvironmentVariable("PATH", envPythonHome + ";" + Environment.GetEnvironmentVariable("PATH", EnvironmentVariableTarget.Machine), EnvironmentVariableTarget.Process);

            //PythonEngine.PythonPath = PythonEngine.PythonPath + ";" + vegaspythonpath + ";" + moduleDirectory + ";" + pythonnetpath;
            PythonEngine.PythonPath = PythonEngine.PythonPath + ";" + vegaspythonpath + ";" + pythonnetpath;

            ShowDebugMessage("PythonPath1: " + PythonEngine.PythonPath);

            string vegaspath = @"C:\Program Files\VEGAS\VEGAS Pro 16.0";

            string envPythonLib = envPythonHome + @"\Lib\site-packages";

            PythonEngine.PythonHome = envPythonHome;

            //string sv_pythonpath = Environment.GetEnvironmentVariable("PYTHONPATH");

            //string sv_path = Environment.GetEnvironmentVariable("PATH", EnvironmentVariableTarget.Machine);

            //PythonEngine.PythonPath = Environment.GetEnvironmentVariable("PYTHONPATH") + ";" + vegaspythonpath + ";" + moduleDirectory + ";" + pythonnetpath + ";" + vegaspath;
            PythonEngine.PythonPath = Environment.GetEnvironmentVariable("PYTHONPATH") + ";" + vegaspythonpath + ";" + pythonnetpath + ";" + vegaspath;

            ShowDebugMessage("PythonPath2: " + PythonEngine.PythonPath);

            Environment.SetEnvironmentVariable("PYTHONHOME", envPythonHome, EnvironmentVariableTarget.Process);

            Environment.SetEnvironmentVariable("PATH", envPythonHome + ";" + Environment.GetEnvironmentVariable("PATH", EnvironmentVariableTarget.Machine), EnvironmentVariableTarget.Process);

            Environment.SetEnvironmentVariable("PYTHONPATH", envPythonLib, EnvironmentVariableTarget.Process);


        }

        public void Execute_VPython_CMD()
        {

            ShowDebugMessage("Execute VPython CMD 1");
            Execute_VPython_CMD_PN();
        }


        private void Execute_VPython_CMD_PN()
        {
            try
            {
                ShowDebugMessage("CMD_PN");
                Set_Path_PN("");

                // Console.SetOut(new OutBoxWriter(mvpWindowForm.vPythonOutputBox));

                PythonEngine.Initialize();

                string code = readInputText();

                ClearMessage();

                Object pyVegas = myVegas;

                using (Py.GIL())
                {
                    using (var scope = Py.CreateScope())
                    {
                        if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
                        {
                            Console.SetOut(new OutBoxWriter(mvpWindowForm.vPythonOutputBox));
                        }

                        // Redirect stdout to text box
                        dynamic sys = PythonEngine.ImportModule("sys");

                        string codeToRedirectOutput =
                            "import sys\n" +
                            "from io import StringIO\n" +
                            "sys.stdout = mystdout = StringIO()\n" +
                            "sys.stdout.flush()\n" +
                            "sys.stderr = mystderr = StringIO()\n" +
                            "sys.stderr.flush()\n";

                        scope.Exec(codeToRedirectOutput);

                        // Console.SetOut(new OutBoxWriter(vPythonOutputBox));

                        scope.Set("pyVEGAS", pyVegas); //declare a global variable
                        scope.Set("__name__", "__main__");

                        scope.Exec(code);

                        string pyStdout = sys.stdout.getvalue(); // Get stdout
                        pyStdout = pyStdout.Replace("\n", "\r\n");

                        ShowMessage(pyStdout);

                        scope.Dispose();
                    }

                }
                // PythonEngine.Shutdown();
            }

            catch (Exception e)
            {
                string msg = "Error executing Python Script \"{0}\"";
                ShowError(msg, "VEGASPython Script", e);
            }
            //           fs.Close();


        }

        public void Execute_VPython_Script(string filename, List<string> sysargs)
        {

            //m_filename = filename; // import syntax - VEGASPython_PN.Menu_item

            Execute_VPython_File_PN(filename, sysargs);

        }

        [System.Runtime.ExceptionServices.HandleProcessCorruptedStateExceptionsAttribute]
        private void Execute_VPython_File_PN(string filename, List<string> sysargs)
        {
            ClearMessage();
            ShowDebugMessage("File_PN");
            String pythonfile = "";
            dynamic sys = null; // = PythonEngine.ImportModule("sys");
            string pyStdout = "";
            string pyStderr = "";
            try
            {
                //if (File.Exists(m_filename))
                //{
                ShowDebugMessage("Start");

                // string moduleDirectory = Path.GetDirectoryName(m_filename);

                //string moduleName = Path.GetFileNameWithoutExtension(m_filename);
                string moduleName = filename; // import syntax
                Set_Path_PN(filename);

                ShowDebugMessage("PythonPath2: " + PythonEngine.PythonPath);

                myVegas.UpdateUI();

                Object pyVegas = myVegas;

                ShowDebugMessage("Py.GIL");

                using (Py.GIL())
                {
                    ShowDebugMessage("Py.CreatScope");
                    using (var scope = Py.CreateScope("VEGAS"))
                    {
                        ShowDebugMessage("PythonEngine.Initialze");
                        PythonEngine.Initialize();


                        // Redirect stdout to text box
                        ShowDebugMessage("PythonEngine.ImportModule(sys)");
                        sys = PythonEngine.ImportModule("sys");

                        string codeToRedirectOutput =
                            "import sys\n" +
                            "from io import StringIO\n" +
                            "sys.stdout = mystdout = StringIO()\n" +
                            "sys.stdout.flush()\n" +
                            "sys.stderr = mystderr = StringIO()\n" +
                            "sys.stderr.flush()\n";

                        scope.Exec(codeToRedirectOutput);

                        if ((mvpWindowForm != null) && (myVegas.ActivateDockView(vPythonModule.vPythonWindowMName)))
                        {
                            Console.SetOut(new OutBoxWriter(mvpWindowForm.vPythonOutputBox));
                        }

                        ShowMessage("Script: " + filename);

                        if (sysargs!=null)
                        { 
                            Py.SetArgv(sysargs);
                        }

                        if ((mVegasPythonConfigData.debugmode) && (mVegasPythonConfigData.debugprecmd != ""))
                        {
                            scope.Exec(mVegasPythonConfigData.debugprecmd);
                            ShowDebugMessage("Pre-CMD Executed:" + mVegasPythonConfigData.debugprecmd);
                        }



                        if ((mVegasPythonConfigData.debugmode) && (mVegasPythonConfigData.debugusereload) && (PythonModuleImported != null))
                        {
                            if (PythonModuleImportedName == moduleName)
                            {
                                ShowDebugMessage("Reload Module" + moduleName);
                                PythonEngine.ReloadModule(PythonModuleImported);
                            }
                            else
                            {
                                ShowDebugMessage("Import Module" + moduleName);
                                //PythonModuleImported = Py.Import(moduleName);
                                PythonModuleImported = scope.Import(moduleName);
                                //PythonModuleImported = PythonEngine.ImportModule(moduleName);
                                PythonModuleImportedName = moduleName;
                            }

                        }
                        else
                        {
                            ShowDebugMessage("Import Module" + moduleName);
                            //PythonModuleImported = Py.Import(moduleName);
                            PythonModuleImported = scope.Import(moduleName);
                            //PythonModuleImported = PythonEngine.ImportModule(moduleName);
                            PythonModuleImportedName = moduleName;
                        }
                        
                        scope.Set("pyVEGAS", pyVegas); //declare pyVEGAS as global variable
                        scope.Set("__name__", "__main__");

                        ShowDebugMessage("module.FromVegas");

                        PythonModuleImported.FromVegas(pyVegas);
                        
                        if ((mVegasPythonConfigData.debugmode) && (mVegasPythonConfigData.debugpostcmd != ""))
                        {
                            scope.Exec(mVegasPythonConfigData.debugpostcmd);
                            ShowDebugMessage("Post-CMD Executed:" + mVegasPythonConfigData.debugpostcmd);
                        }

                        pyStdout = sys.stdout.getvalue(); // Get stdout
                        pyStdout = pyStdout.Replace("\n", "\r\n");
                        pyStderr = sys.stderr.getvalue(); // Get stderr
                        pyStderr = pyStderr.Replace("\n", "\r\n");
                        ShowMessage(pyStdout + "\r\n" + pyStderr);

                        scope.Dispose();



                    }
                }
                //}
                // PythonEngine.Shutdown();
            }

            catch (Exception e)
            {


                string msg = "Error executing Python file \"{0}\"";
                ShowError(msg, Path.GetFileName(pythonfile), e);
            }
            finally
            {
                // PythonEngine.Shutdown();
            }

        }

    }

    public class OutBoxWriter : TextWriter
    {
        private readonly Encoding encoding;
        private readonly TextBox textBox;

        public OutBoxWriter(TextBox textBox) : this(textBox, Encoding.UTF8)
        {
        }

        public OutBoxWriter(TextBox textBox, Encoding encoding)
        {
            this.textBox = textBox;
            this.encoding = encoding;
        }

        public override void WriteLine(string value)
        {
            this.textBox.AppendText(value);
        }

        public override void Write(char value)
        {
            this.textBox.AppendText(value.ToString());
        }

        public override void Write(string value)
        {
            this.textBox.AppendText(value);
        }

        public override void Write(char[] buffer, int index, int count)
        {
            this.textBox.AppendText(new string(buffer));
        }

        public override Encoding Encoding
        {
            get
            {
                return this.encoding;
            }
        }
    }


    public partial class vPythonForm : UserControl
    {
        //private string init_filename = "";
        //private string m_filename = "";
        private string m_editfilename = "";
        //private string m_pythonscriptfilename = "";
        //private string VEGASPythoninitmessage = "** VEGASPython V1.0 started **";
        
        public Vegas myVegas;

        
        public vPythonForm(Vegas vegas)
        {
            InitializeComponent();
            if (VEGASPythonManager.mVegasPythonManager==null)
            {
                VEGASPythonManager.mVegasPythonManager = new VEGASPythonManager(vegas, this);

            }
            VEGASPythonManager.mVegasPythonManager.InitializeVEGASPython(vegas, this);

            /*           if (vegas.ActivateDockView(vpyVEGASWindowMName))
                       {
                           vPythonOutputBox.AppendText(VEGASPythoninitmessage + "\r\n");
                       }
            */
            myVegas = vegas;

            Dictionary<string, object> options = new Dictionary<string, object>();
            options["Debug"] = true;

           }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
  //              dummy
            }
        }

        

        private void OpenFile_Click(object sender, EventArgs e)
        {
            string DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Filter = "Python Scripts (*.py)|*.py|All files (*.*)|*.*";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.AddExtension = true;
            openFileDialog1.InitialDirectory = DLLDirectory + "\\VEGASPython";
            openFileDialog1.Title = "Load a Python Script File";

            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                System.IO.StreamReader sr = new System.IO.StreamReader(openFileDialog1.FileName);
                vPythonInputBox.Clear();
                vPythonInputBox.AppendText(sr.ReadToEnd());
                sr.Close();
                m_editfilename = openFileDialog1.FileName;
            }
        }

        private void ExecuteScript_Click(object sender, EventArgs e)
        {

            VEGASPythonManager.mVegasPythonManager.ShowDebugMessage("Execute Script");
            using (UndoBlock undo = new UndoBlock("Execute Python Script"))
            {
                VEGASPythonManager.mVegasPythonManager.ShowDebugMessage("Execute Script Step 2");
                VEGASPythonManager.mVegasPythonManager.Execute_VPython_CMD();
            }
        }

        private void SaveScript_Click(object sender, EventArgs e)
        {

            string DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
        
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();

            saveFileDialog1.Filter = "Python Scripts (*.py)|*.py|All files (*.*)|*.*";
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.AddExtension = true;
            saveFileDialog1.FileName = m_editfilename;
            saveFileDialog1.InitialDirectory = DLLDirectory + "\\VEGASPython";
            saveFileDialog1.Title = "Save an Python Script File";

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if (saveFileDialog1.FileName != "")
                {
                    using (StreamWriter sw = new StreamWriter(saveFileDialog1.OpenFile()))
                    {
                        sw.Write(vPythonInputBox.Text);
                        sw.Close();
                    }
                }
            }
        }

        private void vPythonForm_Load(object sender, EventArgs e)
        {
        vPythonInputBox.Focus();
        vPythonInputBox.SelectAll();
        }
    }
}
