import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl


import common.screen as screen

class ReplyPvp(BaseControl):

  
    _upPonit=False


    def setUpPonit(self,upPonit):
        self._upPonit=upPonit
  

    def setTeamNo(self,teamNo):
        print("setTeamNo",teamNo)
        self._teamNo=teamNo
  
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval





    def onPvpList(self):
        print("onPvpList")
        # return screen.autoCompareResImgHash(self.handle,"pvp\\pvp_list_76_20_96_90.png")
        return self.matchResImgInWindow("pvp\\pvp_list_76_20_96_90.png",0.7) or self.matchResImgInWindow("pvp\\on_pvp_list_5_5_90_10.png")


    def onPvpWin(self):
        print("onPvpWin")
        # return screen.autoCompareResImgHash(self.handle,"onpvpwin_10_50_80_60.png")
        return self.matchResImgInWindow("pvp\\pvp_win_0_0_100_25.png")



    def onPvpLost(self):
        print("onPvpLost")
        # return screen.autoCompareResImgHash(self.handle,"onpvplost_10_60_80_80.png")
        return self.matchResImgInWindow("pvp\\pvp_lost_0_0_100_25.png")



    def onPvpEnd(self):
        print("onPvpEnd")
        return screen.autoCompareResImgHash(self.handle,"pvp\\pvp_end_10_40_90_60.png")






    def toPvp(self):
        screen.setForegroundWindow(self.handle)
        # win32api.SetCursorPos((self.getPosX(80), self.getPosY(28)))#点击pvp
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        # win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  
        if self._upPonit :
           self.leftClickPer(80,28)  
        else:
           for i in range(3):
             self.dragPer(50,70 ,50,30)
             time.sleep(2)
           self.leftClickPer(80,82)    
            

 
    def toSelecItemOnWin(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(52), self.getPosY(60)))#默认选择中间
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

    def toPvpContinue(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(80), self.getPosY(90)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      

  

    def run(self):    

        while self._isRun:
            screen.setForegroundWindow(self.handle)
         
            
            #PVP列表hash 
           
            if self.onPvpList():
                self.toPvp()
                time.sleep(3)
            else :
                pass

            if self.onSelectTeam():
                self.toSelectTeam(self._teamNo)   
                time.sleep(20)
            else :
                pass

            if self.onPvpLost():
                self.toPvpContinue()
                time.sleep(7)
                continue
            else :
                pass

            if self.onPvpWin():#输赢难以判断
                self.toSelecItemOnWin()
                time.sleep(3)
                self.toPvpContinue() 
                time.sleep(5)#容易截图延迟
            else :
                pass  
                
        
      
            self.reTryNetErr()

            if self.onPvpEnd():
                self._isRun=False
                return

            
            time.sleep(self.interval)

