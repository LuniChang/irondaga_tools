import win32api
import win32gui
import win32con
import time
# import sys,os
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from control.base_control import BaseControl
import threading
# import math
# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()
import common.screen as screen

class ReplyBattle(BaseControl):

  
    _isRun = False
    _needBuyHp=False
    _isUseHp=False
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    

    def start(self):
        self._isRun=True
        t=threading.Thread(target=self.run)
        t.start()


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


    def stop(self):
        self._isRun=False
      
    

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
            print("reply_battle",wLeft, wTop, wRight, wBottom)

           
            #底部菜单hash 
            hashCode=screen.screenRectPerHash(self.handle,0,90,100,95)
            print("clickReplyBattle")
            if screen.alikeHash(hashCode,"d52a2a572a2aadd5") :
               self.clickReplyBattle()
               time.sleep(5)
            else :
                
               pass

           
            print("clickOnGoods")
            #获取物品执行
            if self.onGetGoods() :
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
            print("toUseHp")
            if self._isUseHp and screen.alikeHash(hashCode,"e06aea6aeaea8aa1"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(self.interval)
            screen.grabCaptureDir(self.handle,"reply_battle")



