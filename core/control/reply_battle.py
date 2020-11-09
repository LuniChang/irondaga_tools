import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyBattle(BaseControl):

  
  
    _needBuyHp=False
 
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    



    def buyHp(self):
        pass


        
   

    def clickReplyBattle(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(35), self.getPosY(93)))#点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        



    

    def run(self):    

        while self._isRun:
            screen.setForegroundWindow(self.handle)

            # print(screen.featResImgInWindow(self.handle,"map//unkown_46_46_54_50.png"))
            
           
            #底部菜单hash 
            print("clickReplyBattle")
            if self.autoCompareResImgHash("reply//end_0_90_40_95.png") or self.autoCompareResImgHash("reply//end_0_90_100_95.png"):
               self.clickReplyBattle()
               time.sleep(5)

            


           
            print("clickOnGetItems")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGetItems()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            print("toUseHp")
            if self._isUseHp and self.isHpEmpty():
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            self.reTryNetErr()
            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



