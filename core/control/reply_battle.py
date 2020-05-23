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
        
    def closeEmptyHp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(80), self.getPosY(40)))#关闭体力框
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def clickOnGoods(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(50), self.getPosY(65)))#点击物品
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
            print("clickReplyBattle hashCode2",hashCode)
            if screen.difHash(hashCode,"d53d2ac62ac2553d2ace555a959ad53ca839aac22ae52afb475ed525555ac438") < 0.4:
               self.clickReplyBattle()
               time.sleep(2)
            else :
                
               pass

            hashCode=screen.screenRectPerHash(self.handle,35,63,56,67)
            print("clickOnGoods hashCode1",hashCode)
            #获取物品执行
            if screen.difHash(hashCode,"9c6d9e66639b91a2cea492599b638624866dc5326596b3c9e5b26536936d6536") < 0.4:
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
            print("toUseHp hashCode1",hashCode)
            if self._isUseHp and screen.difHash(hashCode,"e0f36a7beaa56afceafeaabd807ba0b12a1d2e85aa5691b19369955124946e04") < 0.4:
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(10)
            screen.grabCaptureDir(self.handle,"reply_battle")

