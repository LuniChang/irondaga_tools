import os

def getProjectPath():
    project_name = "irondaga_tools"
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")] 
    return rootPath