import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class Momo(BaseControl):

  
    _count=0
    maxCount=40

 
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

 


        
   


    

    def run(self):    

        while self._isRun and self._count< self.maxCount:
            screen.setForegroundWindow(self.handle)

     
            if self.matchResImgInWindow("momo/home_0_0_30_5.png"):
                self.leftClickPer(10, 50)
                time.sleep(3)
                self.onDlgOkAndClick()
                time.sleep(3)
                self.clickMacthImg("momo/next_88_70_98_88.png")

  

            self.reTryNetErr()
            self._count=self._count+1
            time.sleep(self.interval)   
           


