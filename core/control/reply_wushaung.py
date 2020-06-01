import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyWuShuang(BaseControl):

  
  
    _needBuyHp=False
    _isUseHp=False
    _wsCount=0
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    



    def buyHp(self):
        pass

    def toUseHp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(60), self.getPosY(62)))#点击使用体力药
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
    def leftClickPerLong(self,x,y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)  
        time.sleep(0.3) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  

    def clickReplyBattle(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(15), self.getPosY(92)))#点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        



    
    
    def run(self):    
        self._wsCount=0
        while self._isRun and  self._wsCount<8:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
            print("reply_battle",wLeft, wTop, wRight, wBottom)

            self.leftClickPerLong(70,30)
            self.leftClickPerLong(70,10)

            #底部菜单hash 
            print("clickReplyBattle")

            if screen.autoCompareResImgHash(self.handle,"wushuang_end_0_90_80_100.png"):
               self.clickReplyBattle()
               time.sleep(5)
               self._wsCount=self._wsCount+1
            else :
                
               pass

           
            print("clickOnGoods")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
            print("toUseHp")

            if self._isUseHp and screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

       
            time.sleep(1)
