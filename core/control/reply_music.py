import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyMusic(BaseControl):

  
  
    _needBuyHp=False
 
    def __init__(self,handle):
        self.handle=handle


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
           
           
            # screen.grabCaptureDir(self.handle,"reply_battle")



