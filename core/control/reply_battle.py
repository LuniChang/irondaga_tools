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
        win32api.SetCursorPos((self.getPosX(60), self.getPosY(62)))#点击使用体力药
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
   

    def clickReplyBattle(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(27), self.getPosY(93)))#点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        



    

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
            print("reply_battle",wLeft, wTop, wRight, wBottom)

           
            #底部菜单hash 
            # hashCode=screen.screenRectPerHash(self.handle,0,90,100,95)
            # hashCode2=screen.getResImgHash("battle_end_0_90_100_95.png")
            print("clickReplyBattle")
            # if screen.alikeHash(hashCode,"d52a2a572a2aadd5") :
            # if screen.alikeHash(hashCode,hashCode2) :
            if screen.autoCompareResImgHash(self.handle,"battle_end_0_90_100_95.png"):
               self.clickReplyBattle()
               time.sleep(5)
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
            # hashCode2=screen.getResImgHash("hpempty_10_40_80_65.png")
            # if self._isUseHp and screen.alikeHash(hashCode,hashCode2) :
            # if self._isUseHp and screen.alikeHash(hashCode,"e06aea6aeaea8aa1"):
            # if self._isUseHp and screen.alikeHash(hashCode,"9122d8d8948c5454"):
            if screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(self.interval)
            screen.grabCaptureDir(self.handle,"reply_battle")



