import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyBattle(BaseControl):

  
  
    _needBuyHp=False
    _isUseHp=False
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    



    def buyHp(self):
        pass

    def toUseHp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(62), self.getPosY(60)))#点击使用体力药
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
   

    def clickReplyBattle(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(35), self.getPosY(93)))#点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        



    

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
           
            #底部菜单hash 

            print("clickReplyBattle")
            if screen.autoCompareResImgHash(self.handle,"reply//end_0_90_100_95.png"):
               self.clickReplyBattle()
               time.sleep(5)


           
            print("clickOnGoods")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            print("toUseHp")
            if self._isUseHp and self.isHpEmpty():
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



