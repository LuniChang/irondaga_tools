import win32api
import win32gui
import win32con
import common.screen as screen
import threading
import time
class BaseControl:
    
    handle=0
    interval=5

    _isRun = False

    def __init__(self):
        pass

    def stop(self):
        self._isRun=False
      
    def start(self):
        if self._isRun:
            return
        self._isRun=True
        t=threading.Thread(target=self.run)
        t.start()

    def getPosX(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        width = wRight-wLeft
        return int(wLeft+(width*srcPer))

    def getPosY(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        height = wBottom-wTop
        return int(wTop+(height*(srcPer)))

    def onGetItems(self):
        print("onGetItems")
        return screen.autoCompareResImgHash(self.handle,"on_get_item_10_35_85_65.png")

    def resetCursorPos(self):
        win32api.SetCursorPos((0, 0))

    def dragPer(self,x,y,toX,toY):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)
        time.sleep(0.5)  
        moveToX=int(self.getPosX(toX)*(65535/win32api.GetSystemMetrics(0)))
        moveToY=int(self.getPosY(toY)*(65535/win32api.GetSystemMetrics(1)))
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, moveToX, moveToY, 0, 0)  
        time.sleep(0.3)
        win32api.SetCursorPos((moveToX, moveToY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  

        # win32gui.sendMessage(self.handle,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON, (self.getPosX(x), self.getPosY(y))   #   起始点按住
        # win32gui.sendMessage(self.handle,win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON,moveToX, moveToY)   #   移动到终点
        # win32gui.sendMessage(self.handle, win32con.WM_LBUTTONUP, 0, 0)   # 松开


    def leftClick(self,x,y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)  
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP , 0, 0, 0, 0)  
        time.sleep(0.2)
        self.resetCursorPos()
 

    def leftClickPer(self,x,y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)  
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP , 0, 0, 0, 0)  
        time.sleep(0.2)
        self.resetCursorPos()
     
    
    

    def clickOnGetItems(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(50), self.getPosY(64))


    def closeEmptyHp(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(85), self.getPosY(38))
  
    def onSelectTeam(self):
        print("onSelectTeam")
        return self.matchResImgInWindow("on_select_team_10_35_90_45.png")

    def onDlgOK(self):
        print("onDlgOK")
        return self.matchResImgInWindow("on_dlg_ok_61_62_80_65.png")
    def clickDlgOK(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(75), self.getPosY(60))

       
    def onDlgOkAndClick(self):
        win32gui.SetForegroundWindow(self.handle)
        xylist=screen.matchResImgInWindow(self.handle,"on_dlg_ok_60_62_80_66.png")
        if len(xylist) >0:
             x, y = xylist[0]
             self.leftClick(x+2, y+2)

 
        

    #阵容小于3或者大于6不能用
    def toSelectTeam(self,teamNo):
        win32gui.SetForegroundWindow(self.handle)
        if teamNo==1 :
           win32api.SetCursorPos((self.getPosX(30), self.getPosY(50)))#点击1队
        elif teamNo==2:
           win32api.SetCursorPos((self.getPosX(55), self.getPosY(50)))#点击2队
        elif teamNo==3:    
           win32api.SetCursorPos((self.getPosX(80), self.getPosY(50)))#点击3队
        elif teamNo==4:    
           win32api.SetCursorPos((self.getPosX(30), self.getPosY(55)))#点击4队
        elif teamNo==5:    
           win32api.SetCursorPos((self.getPosX(55), self.getPosY(55)))#点击5队
        elif teamNo==6:    
           win32api.SetCursorPos((self.getPosX(80), self.getPosY(55)))#点击6队
        else :
            pass

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    


    def matchResImgInWindow(self,imgName,threshold=0.8):
        xylist=screen.matchResImgInWindow(self.handle,imgName,threshold)
        if len(xylist) >0:
            return True
        else:
            return False
    
    
    
    def isHpEmpty(self):
        return screen.autoCompareResImgHash(self.handle,"hp_empty_10_40_90_62.png")

    def run(self):
        pass
pass