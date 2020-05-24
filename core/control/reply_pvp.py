import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl


import common.screen as screen

class ReplyPvp(BaseControl):

  
   
    _teamNo=3

    def setTeamNo(self,teamNo):
        print("setTeamNo",teamNo)
        self._teamNo=teamNo
  
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval





    def onPvpList(self):
        print("onPvpList")
        hashCode=screen.screenRectPerHash(self.handle,70,20,90,90)
        return screen.alikeHash(hashCode,"cb7874607636762c")



    def onPvpWin(self):
        print("onPvpWin")
        hashCode=screen.screenRectPerHash(self.handle,0,15,90,25)
        return screen.alikeHash(hashCode,"ce9a356d6564f092")    

    def onPvpLost(self):
        print("onPvpLost")
        hashCode=screen.screenRectPerHash(self.handle,0,15,90,25)
        return screen.alikeHash(hashCode,"96927169616d6d96")    

    def onPvpEnd(self):
        print("onPvpEnd")
        hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
        return screen.alikeHash(hashCode,"c242e76a6bcbcae0")  

    def onSelectTeam(self):
        print("onSelectTeam")
        hashCode=screen.screenRectPerHash(self.handle,8,36,82,50)
        return screen.alikeHash(hashCode,"eaeaaa8a393c1c35")


    def toPvp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(75), self.getPosY(30)))#点击pvp
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)       

    def toSelectTeam(self): #阵容 小于3或者大于6不能用
        win32gui.SetForegroundWindow(self.handle)
        if self._teamNo==1 :
           win32api.SetCursorPos((self.getPosX(25), self.getPosY(52)))#点击1队
        elif self._teamNo==2:
           win32api.SetCursorPos((self.getPosX(50), self.getPosY(52)))#点击2队
        elif self._teamNo==3:    
           win32api.SetCursorPos((self.getPosX(75), self.getPosY(52)))#点击3队
        elif self._teamNo==4:    
           win32api.SetCursorPos((self.getPosX(25), self.getPosY(58)))#点击4队
        elif self._teamNo==5:    
           win32api.SetCursorPos((self.getPosX(50), self.getPosY(58)))#点击5队
        elif self._teamNo==6:    
           win32api.SetCursorPos((self.getPosX(75), self.getPosY(58)))#点击6队
        else :
            pass

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    


    def toSelecItemOnWin(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(47), self.getPosY(64)))#默认选择中间
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

    def toPvpContinue(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(75), self.getPosY(92)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

  

    def run(self):    

        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
            print("reply_battle",wLeft, wTop, wRight, wBottom)

           
            #PVP列表hash 
           
            if self.onPvpList():
                self.toPvp()
                time.sleep(3)
            else :
                pass

            if self.onSelectTeam():
                self.toSelectTeam()   
                time.sleep(3)
            else :
                pass

           
            if self.onPvpLost():
                self.toPvpContinue()
                time.sleep(3)
            else :
                pass


            if self.onPvpWin():
                self.toSelecItemOnWin()
                time.sleep(3)
                self.toPvpContinue()
                time.sleep(3)
            else :
                pass   

            if self.onPvpEnd():
                self._isRun=False
                return

            time.sleep(self.interval)

