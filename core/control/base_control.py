import win32api
import win32gui
import win32con


class BaseControl:
    
    handle=0
    interval=5

 

    def __init__(self):
        pass

    def getPosX(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
        width = wRight-wLeft
        return int(wLeft+(width*srcPer))

    def getPosY(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
        height = wBottom-wTop
        return int(wTop+(height*(srcPer)))
pass