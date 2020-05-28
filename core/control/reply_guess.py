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
        return screen.autoCompareResImgHash(self.handle,"onget_money_10_40_80_65.png")


    def clickOnMoney(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(50), self.getPosY(61)))#点击物品
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def onGuessEnd(self):
        print("onGuessEnd")
        # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
        # return screen.alikeHash(hashCode,"c242e76a6bcbcae0")    
        return screen.autoCompareResImgHash(self.handle,"pvp_end_10_40_80_65.png")



    def toGuess(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(50), self.getPosY(30)))#点击去竞猜
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)       

    def selecGuessRight(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(62), self.getPosY(60)))#默认选择右边
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
            print("reply_battle",wLeft, wTop, wRight, wBottom)

           
            #精彩页面hash 
            # hashCode=screen.screenRectPerHash(self.handle,5,20,90,40)
            print("toGuess")
            # if screen.alikeHash(hashCode,"8b6ca513d20fa96d"):
            if screen.autoCompareResImgHash(self.handle,"guess_5_20_90_40.png"):
               self.toGuess()
               time.sleep(5)
            else :
                
               pass

            # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
            print("selecGuess")
            
            # if screen.alikeHash(hashCode,"c966a921de295b66"):
            if screen.autoCompareResImgHash(self.handle,"guess_select_10_40_80_65.png"):
               self.selecGuessRight()
               time.sleep(5)
            else :
                
               pass
            

            if self.onGetMoney():
                self.clickOnMoney()
                time.sleep(2)
            else :
                pass
            
            if self.onGuessEnd():
                self._isRun=False
                return


            time.sleep(self.interval)

