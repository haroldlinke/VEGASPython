using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ScriptPortal.Vegas;
using System.Windows.Forms;

namespace VegasPython
{
    public class vPythonModule : ICustomCommandModule
    {
        public const string vPythonWindowMName = "VEGASPython Interactive Window";
        private const string cVEGASPythonFolder = "\\VEGASPython";
        private CustomCommand vPythonWindowCommand = null;
        private Vegas vegas = null;
        public vPythonDockView vPythonView;
        private List<CustomCommand> vPythonWindowCommandList = new List<CustomCommand>();
 //       string test;

        public void InitializeModule(Vegas vegas)
        {
            this.vegas = vegas;
            // add vegas' event handlers here eg. this.vegas.ProjectOpening += vegas_ProjectOpening;
            this.vegas.AppInitialized += Vegas_AppInitialized;
            // this.vegas.ProjectOpened += Vegas_ProjectOpened;
        }

  //      private void Vegas_ProjectOpened(object sender, EventArgs e)
  //      {
  //          test = "";
  //      }

        private void Vegas_AppInitialized(object sender, EventArgs e)
        {
            //Check for Scriptarguments with Python script to start
            
            // check if commandline args include the call to a python script
            executeCommandLineArgs();


        }
        
        private void executeCommandLineArgs()
        {

            // look for commandline arguments
            //  /SCRIPTARGS "C:\Users\Harold\Documents\Vegas Application Extensions\VEGASPython\test.py" /SCRIPTARGS arg1 /SCRIPTARGS arg2 /SCRIPTARGS arg3
            List<string> argList;

            string[] args = System.Environment.GetCommandLineArgs(); //get all commandline arguments
            Boolean scriptargs_found = false;
            Boolean scriptarg_filename_found = false;

            argList = new List<string>();

            string pythonscriptfilename;

            pythonscriptfilename = "";

            foreach (string arg in args)
            {

                if (arg == "/SCRIPTARGS")
                {
                    scriptargs_found = true;
                }
                else
                {
                    if (scriptargs_found)
                    {
                        if (!scriptarg_filename_found)
                        {
                            // pythscript filename found
                            
                            char[] charSeparators = new char[] { '=' };
                            string[] argcomp = arg.Split(charSeparators);
                            if ((argcomp.Length == 2) && (argcomp[0] == "VPSCRIPT"))
                            {
                                pythonscriptfilename = argcomp[1];
                                argList.Add(pythonscriptfilename); // add pythonscript name to argument list
                                scriptarg_filename_found = true;
                            }
                        }
                        else
                        {
                            // arg is a new argument for the pythonscript
                            argList.Add(arg);
                        }

                        scriptargs_found = false; // search for next /SCRIPTARGS arg entry

                    }
                }
            }

            if (pythonscriptfilename.Length > 0)
            {

                if (VEGASPythonManager.mVegasPythonManager == null)
                {
                    VEGASPythonManager.mVegasPythonManager = new VEGASPythonManager(vegas, null);

                }
                VEGASPythonManager.mVegasPythonManager.InitializeVEGASPython(vegas, null);

                VEGASPythonManager.mVegasPythonManager.Execute_VPython_Script(pythonscriptfilename, argList);
            }
        }

        private void create_command_list(string pSearchPath, CustomCommand parent, bool includesubdir)
        {
            if (Directory.Exists(pSearchPath))
            {
                string[] VEGASPythonfileArray;

                if (includesubdir)
                {
                    VEGASPythonfileArray = Directory.GetDirectories(pSearchPath);

                    foreach (string pythonscriptfilepathname in VEGASPythonfileArray)
                    {
                        if (Directory.Exists(pythonscriptfilepathname)) //name is directory
                        {

                            if (!(File.Exists(pythonscriptfilepathname + "\\__init__.py"))) // check if directory is a python package
                            {
                                string pythonscriptpathname = Path.GetDirectoryName(pythonscriptfilepathname); // gets the parent directory path
                                string directoryname = pythonscriptfilepathname.Substring(pythonscriptpathname.Length + 1);

                                if (directoryname.Substring(0, 1) != "_") //ignore directories with leading _
                                {
                                    CustomCommand vPythonScriptCommand = new CustomCommand(CommandCategory.Tools, directoryname);

                                    vPythonScriptCommand.DisplayName = directoryname;
                                    vPythonScriptCommand.Invoked += vPythonScript_Invoked;

                                    if (parent == null)
                                    {
                                        vPythonWindowCommandList.Add(vPythonScriptCommand);
                                    }
                                    else
                                    {
                                        parent.AddChild(vPythonScriptCommand);
                                    }
                                    create_command_list(pythonscriptfilepathname, vPythonScriptCommand, false);
                                }
                            }
                        }
                    }
                }

                VEGASPythonfileArray = Directory.GetFiles(pSearchPath);
                foreach (string pythonscriptfilepathname in VEGASPythonfileArray)
                {
                    {
                        if (File.Exists(pythonscriptfilepathname)) // name is a file
                        {
                            string psextension = Path.GetExtension(pythonscriptfilepathname);
                            string pythonscriptname = Path.GetFileNameWithoutExtension(pythonscriptfilepathname);

                            if ((psextension == ".py") && (!(pythonscriptname == "wingdbstub")))
                            {
                                string line;
                                System.IO.StreamReader file = new System.IO.StreamReader(pythonscriptfilepathname);
                                line = file.ReadLine();


                                if (!string.IsNullOrEmpty(line))
                                {

                                    CustomCommand vPythonScriptCommand = new CustomCommand(CommandCategory.Tools, pythonscriptname);
                                    vPythonScriptCommand.MenuSelectMessage = "Execute " + pythonscriptname;
                                    vPythonScriptCommand.DisplayName = pythonscriptname;
                                    string iconFilename = pythonscriptfilepathname.Replace(".py", ".png");
                                    if (File.Exists(iconFilename))
                                    {
                                        vPythonScriptCommand.IconFile = iconFilename;
                                    }
                                    else
                                    {
                                        iconFilename = pythonscriptfilepathname.Replace(pythonscriptname + ".py", "VegasPython.png");
                                        if (File.Exists(iconFilename))
                                        {
                                            vPythonScriptCommand.IconFile = iconFilename;
                                        }
                                    }

                                    vPythonScriptCommand.Invoked += vPythonScript_Invoked;

                                    if (line.Contains("#"))
                                        vPythonScriptCommand.MenuSelectMessage = line;
                                    else
                                    {
                                        int start = line.IndexOf("\"\"\"");
                                        string commentline = line;
                                        if (start > 0)
                                        {
                                            commentline = line.Substring(start + 3);
                                            int end = commentline.IndexOf("\"\"\"");
                                            if (end > 0)
                                                commentline = commentline.Substring(0, end - 1);
                                        }
                                        vPythonScriptCommand.MenuSelectMessage = commentline;

                                    }



                                    // vPythonScriptCommand.MenuPopup += vPythonScript_MenuPopup;
                                    if (parent == null)
                                    {
                                        vPythonWindowCommandList.Add(vPythonScriptCommand);
                                    }
                                    else
                                    {
                                        parent.AddChild(vPythonScriptCommand);
                                    }
                                }
                                file.Close();
                            }
                        }
                    }
                }
            }

        }

        public System.Collections.ICollection GetCustomCommands()
        {

            VEGASPythonConfig vegasPythonConfigData;
            vegasPythonConfigData = VEGASPythonConfig.Read_config();

            vPythonWindowCommand = new CustomCommand(CommandCategory.View, vPythonWindowMName);
            vPythonWindowCommand.DisplayName = vPythonWindowMName;
            vPythonWindowCommand.Invoked += vPythonWindowCommand_Invoked;
            vPythonWindowCommand.MenuPopup += vPythonWindowCommand_MenuPopup;


            vPythonWindowCommandList.Add(vPythonWindowCommand);


            // Look for Python scripts in VEGASPython folder

            String DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);

            //vSearchPath = DLLDirectory + "\\VEGASPython_PN";

            string path1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.MyDocuments) + "\\Vegas Application Extensions" + vegasPythonConfigData.VEGASPythonFolder;
            string path2 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.LocalApplicationData) + "\\Vegas Pro\\Application Extensions" + vegasPythonConfigData.VEGASPythonFolder;
            string path3 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ApplicationData) + "\\Vegas Pro\\Application Extensions" + vegasPythonConfigData.VEGASPythonFolder;
            string path4 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.CommonApplicationData) + "\\Vegas Pro\\Application Extensions" + vegasPythonConfigData.VEGASPythonFolder;

            //vSearchPath = DLLDirectory;
            create_command_list(path1, null, true);
            create_command_list(path2, null, true);
            create_command_list(path3, null, true);
            create_command_list(path4, null, true);

            return vPythonWindowCommandList;
        }

        void vPythonWindowCommand_MenuPopup(object sender, EventArgs e)
        {
            // if the dockview is opened, vPython command is checked
            vPythonWindowCommand.Checked = vegas.FindDockView(vPythonWindowMName);
        }

        void vPythonWindowCommand_Invoked(object sender, EventArgs e)
        {
            // if not already active
            if (!vegas.ActivateDockView(vPythonWindowMName))
            {

                // let's create controls
                vPythonForm vPF = new vPythonForm(vegas);
                // create dockable view with controls
                vPythonView = new vPythonDockView(vPythonWindowMName, vPF);
                vPythonView.PersistDockWindowState = true;
                vPythonView.AutoLoadCommand = vPythonWindowCommand;
                vPythonView.MinimumSize = new System.Drawing.Size(300, 400);

                //vPythonView.vPF.setPythonView(vPythonView, vPythonWindowMName);

                vegas.LoadDockView(vPythonView);
                //               System.Diagnostics.Debug.WriteLine("vPython Window created");
            }
        }

        void vPythonScript_Invoked(object sender, EventArgs e)
        {
            // if not already active
            /*** no window will be created    
                if (!vegas.ActivateDockView(vPythonWindowMName))
                {
                    // let's create controls
                    vPythonForm vPF = new vPythonForm(vegas);
                    // create dockable view with controls
                    vPythonView = new vPythonDockView(vPythonWindowMName, vPF);
                    vPythonView.PersistDockWindowState = true;
                    vPythonView.AutoLoadCommand = vPythonWindowCommand;
                    vPythonView.MinimumSize = new System.Drawing.Size(300, 400);
                    //vPythonView.vPF.setPythonView(vPythonView, vPythonWindowMName);

                    vegas.LoadDockView(vPythonView);
                    //               System.Diagnostics.Debug.WriteLine("vPython Window created");
                }

                ****/

            CustomCommand VEGAScommand = (CustomCommand)sender;

            string pythonscriptfilename = "";

            CustomCommand v_customCommand_parent = VEGAScommand.Parent;
            string v_subpath = "";

            if (v_customCommand_parent != null) // ignore main menu item
            {
                while (v_customCommand_parent.Parent != null)
                {
                    //v_subpath = "\\" + v_customCommand_parent.MenuItemName + v_subpath;
                    v_subpath = v_customCommand_parent.MenuItemName + "." + v_subpath; // import syntax
                    v_customCommand_parent = v_customCommand_parent.Parent;
                }
            }

            // String DLLDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
            // vSearchPath = DLLDirectory + "\\VEGASPython";

            //pythonscriptfilename = vSearchPath + v_subpath + "\\" + VEGAScommand.MenuItemName + ".py";
            pythonscriptfilename = v_subpath + VEGAScommand.MenuItemName; // import syntax

            /* import syntax
            if (!File.Exists(pythonscriptfilename)) // script is not in the Standard VEGASPython directory, it must be in the VEGASPython_PN directory 
            {
                vSearchPath = DLLDirectory + "\\VEGASPython_PN";
                pythonscriptfilename = vSearchPath + v_subpath + "\\" + VEGAScommand.MenuItemName + ".py";
            }
            */

            using (UndoBlock undo = new UndoBlock("Execute Scriptfile: " + VEGAScommand.MenuItemName))
            {

                if (VEGASPythonManager.mVegasPythonManager == null)
                {
                    VEGASPythonManager.mVegasPythonManager = new VEGASPythonManager(vegas, null);

                }
                VEGASPythonManager.mVegasPythonManager.InitializeVEGASPython(vegas, null);

                VEGASPythonManager.mVegasPythonManager.Execute_VPython_Script(pythonscriptfilename,null);

            }

        }

    }
}
