import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyWuShuang(BaseControl):

  
  
    _needBuyHp=False
    _isUseHp=False
    _battleOneMapCount=0
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    



    def buyHp(self):
        pass

    def toUseHp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(60), self.getPosY(62)))#点击使用体力药
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
    def leftClickPerLong(self,x,y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)  
        time.sleep(0.3) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  

    def clickReplyBattle(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(15), self.getPosY(92)))#点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)        



    
    _MapNo=0#章节号
    _isInBattle=False

    def run(self):    
        self._battleOneMapCount=0
        self._MapNo=0
        self._isInBattle=False
        while self._isRun and self._MapNo<=6:
            win32gui.SetForegroundWindow(self.handle)
            wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(self.handle)
      


            if  self._isInBattle==False:
                #如果在地图
                print("onmap")
                if screen.autoCompareResImgHash(self.handle,"on_ws_map_70_72_90_74.png"):
                    # self._MapNo=self._MapNo%6
                    if self._MapNo<3:
                       self.leftClickPer(15+30*self._MapNo,35)
                    elif self._MapNo<6:
                       self.leftClickPer(15+30*(self._MapNo-3),50)
                    else:
                       self._MapNo=self._MapNo%6
                       self.leftClickPer(75,73)
                        
                    time.sleep(5)
                #如果在准备页面
                if screen.autoCompareResImgHash(self.handle,"ws_ready_10_75_90_85.png"):
                    self.leftClickPer(80,80)
                    self._isInBattle=True
                    time.sleep(1)
    




            if  self._isInBattle or self._battleOneMapCount<8:
                self.leftClickPerLong(70,30)
                self.leftClickPerLong(70,10)
          

            print("clickOnGoods")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGoods()
                time.sleep(2)
            else :
                pass
        
            #底部菜单hash 
            print("clickReplyBattle")

            if screen.autoCompareResImgHash(self.handle,"wushuang_end_0_90_80_100.png"):
               self.clickReplyBattle()
               print("_battleOneMapCount",self._battleOneMapCount)
               #第五次需要弹出买次数，所以   _MapNo可能会多1
               if self._battleOneMapCount>8:#防止获取物品影响次数
                   self._MapNo=self._MapNo+1
                   self._isInBattle=False
                   self.leftClickPerLong(85,92)#回到地图，快速点击会失效
                   time.sleep(2)
                   
               self._battleOneMapCount=self._battleOneMapCount+1  
               time.sleep(5)

           
         

            #章节完毕
            print("章节完毕")
            if screen.autoCompareResImgHash(self.handle,"ws_map_end_20_40_80_65.png") :
                self._battleOneMapCount=0
                self._isInBattle=False
                self._MapNo=self._MapNo+1
                self.leftClickPer(80,40)
                self.leftClickPerLong(80,40)
                time.sleep(2)
                self.leftClickPer(8,8)
                time.sleep(2)
      

            #体力不足hash 
            # hashCode=screen.screenRectPerHash(self.handle,10,40,80,65)
            print("toUseHp")

            if self._isUseHp and screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            
    
            time.sleep(1)

        self._MapNo=0
        self._battleOneMapCount=0
        self._isInBattle=False
        self._isRun=False
