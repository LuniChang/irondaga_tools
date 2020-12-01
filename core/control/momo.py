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
        self._count=0
        while self._isRun and self._count< self.maxCount:
            screen.setForegroundWindow(self.handle)

     
            if self.matchResImgInWindow("momo/momo_5_50_15_56.png"):
                self.leftClickPer(8, 50)
                time.sleep(3)
                self.onDlgOkAndClick()
                time.sleep(4)
                self._count=self._count+1
                time.sleep(4)
                
            # self.clickMacthImg("momo/next_88_70_98_88.png")
            self.leftClickPer(95, 80)
            time.sleep(2)

            self.reTryNetErr()
            
            time.sleep(self.interval)   
           


