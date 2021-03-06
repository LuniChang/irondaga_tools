import os
import sys

def getProjectPath():
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        # return os.path.dirname(sys.executable)+"\\"  #使用pyinstaller打包后的exe目录
        return ".\\"
    else :
        project_name = "irondaga_tools"
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")] 
        return rootPath
    

def getResDirPath():
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        # return sys._MEIPASS+"\\res\\"  #使用pyinstaller打包后的exe目录
         return ".\\res\\"
    else :
        project_name = "irondaga_tools"
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")] 
        return rootPath+"res\\"
    