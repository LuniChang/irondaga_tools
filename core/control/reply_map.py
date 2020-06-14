import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyMap(BaseControl):

  
  
    _needBuyHp=False
    _isUseHp=False
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    

    #点在判断窗口中点位置的哪个方向
    def xyDirection(self,x,y):
        wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
        
        centerX=(wRight-wLeft)>>1
        centerY=(wTop-wBottom)>>1
        inLeft=True
        inTop=True
        if x>centerX:
          inLeft=False
        if y>centerY:
          inTop=False
        return inLeft,inTop

        
        


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

        diretionLast=0
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
       

    
            print("findUnKnowMap")
            xylist=screen.matchResImgInWindow(self.handle,"map_unknow3_45_47_52_50.png")
           
            
            if  len(xylist)>0:
                # for i in xylist:
                x,y=xylist[0]
                self.leftClick(x,y)
                time.sleep(2)
            else:
                #这就要查看是否地图完结了，然后根据未知地点方向进一步操作...
                self.dragPer(50,50,1,50)
                time.sleep(2)

               

           
            print("getitem2")
            if screen.autoCompareResImgHash(self.handle,"getitem2_10_40_80_65.png"):
                win32gui.SetForegroundWindow(self.handle)
                self.leftClick(self.getPosX(55), self.getPosY(60))
                time.sleep(2)
            else :
                pass
            
            print("clickOnGoods")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            print("hpempty")
            if screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass

            if self.onSelectTeam():
                self.toSelectTeam(5)   
                time.sleep(3)
            else :
                pass


            #体力不足hash 
            print("toUseHp")
            if screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(self.interval)
           


