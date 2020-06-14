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
        wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
        width = wRight-wLeft
        return int(wLeft+(width*srcPer))

    def getPosY(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
        height = wBottom-wTop
        return int(wTop+(height*(srcPer)))

    def onGetItems(self):
        print("onGetItems")
        # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
        # hashCode2=screen.getResImgHash("onget_item_10_40_80_65.png")
        # return screen.alikeHash(hashCode,hashCode2) 
        # return screen.alikeHash(hashCode,"f812816e2d2e69fc")
        return screen.autoCompareResImgHash(self.handle,"onget_item_10_40_80_65.png")


    def dragPer(self,x,y,toX,toY):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)
        time.sleep(1)  
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, self.getPosX(toX), self.getPosY(toY), 0, 0)  
        time.sleep(1)
        win32api.SetCursorPos((self.getPosX(toX), self.getPosY(toY)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  

    def leftClick(self,x,y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  

    def leftClickPer(self,x,y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    

    


    def clickOnGoods(self):
        win32gui.SetForegroundWindow(self.handle)
        # win32api.SetCursorPos((self.getPosX(50), self.getPosY(65)))#点击物品
        # win32api.mouse_event(
        # win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.leftClick(self.getPosX(50), self.getPosY(65))


    def closeEmptyHp(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(80), self.getPosY(40))
        # win32api.SetCursorPos((self.getPosX(80), self.getPosY(40)))#关闭体力框
        # win32api.mouse_event(
        # win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def onSelectTeam(self):
        print("onSelectTeam")
        return screen.autoCompareResImgHash(self.handle,"select_team_8_36_82_50.png")

    #阵容小于3或者大于6不能用
    def toSelectTeam(self,teamNo):
        win32gui.SetForegroundWindow(self.handle)
        if teamNo==1 :
           win32api.SetCursorPos((self.getPosX(25), self.getPosY(52)))#点击1队
        elif teamNo==2:
           win32api.SetCursorPos((self.getPosX(50), self.getPosY(52)))#点击2队
        elif teamNo==3:    
           win32api.SetCursorPos((self.getPosX(75), self.getPosY(52)))#点击3队
        elif teamNo==4:    
           win32api.SetCursorPos((self.getPosX(25), self.getPosY(58)))#点击4队
        elif teamNo==5:    
           win32api.SetCursorPos((self.getPosX(50), self.getPosY(58)))#点击5队
        elif teamNo==6:    
           win32api.SetCursorPos((self.getPosX(75), self.getPosY(58)))#点击6队
        else :
            pass

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    



    def run(self):
        pass
pass