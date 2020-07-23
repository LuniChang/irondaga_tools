import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl
import threading

import common.screen as screen

class ReplyGuess(BaseControl):

  
  
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval




    def onGetMoney(self):
        print("onGetMoney")
        # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
        # return screen.alikeHash(hashCode,"d81a8f8ef8e82e29")
        return screen.autoCompareResImgHash(self.handle,"get_mony_10_36_85_62.png")


    def clickOnMoney(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(55), self.getPosY(62)))#点击物品
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def onGuessEnd(self):
        print("onGuessEnd")  
        return screen.autoCompareResImgHash(self.handle,"guess//end_10_40_85_65.png")

    def getGuessLocation(self):
        return screen.matchResImgInWindow(self.handle,"guess//guess_10_22_90_30.png")


    def toGuess(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(50), self.getPosY(30)))#点击去竞猜
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)       

    def selecGuessRight(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(68), self.getPosY(58)))#默认选择右边
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
           
           
            #精彩页面hash 
            print("toGuess")
            if screen.autoCompareResImgHash(self.handle,"guess\\main_0_18_100_36.png"):
               self.toGuess()
               time.sleep(5)
    

            print("selecGuess")
            if screen.autoCompareResImgHash(self.handle,"guess\\select_10_40_85_65.png"):
               self.selecGuessRight()
               time.sleep(5)
         
            xylist= self.getGuessLocation() 
            if  len(xylist)>0:
                x,y=xylist[0]
                self.leftClick(x,y)
                
                time.sleep(10)
            

            if self.onGetMoney():
                self.clickOnMoney()
                time.sleep(2)
            else :
                pass
            
            if self.onGuessEnd():
                self._isRun=False
                return


            time.sleep(self.interval)

