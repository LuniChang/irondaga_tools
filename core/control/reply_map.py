import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyMap(BaseControl):

  
    mapTeamNo=2
    pvpTeamNo=3
    blueTeamNo=2
    
    _needBuyHp=False
    _isUseHp=False
    _needResetMap=True
    # _startLoopSearch=False
    _scranDirection=0  #0 → 1 ↓ 2← 
    _nextScranDirection=0
    _scranMapEnd=False

    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    

    #点在判断窗口中点位置的哪个方向
    def xyDirection(self,x,y):
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        
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

    def resetMap(self):
        pass



    def dragPerLeft(self):
        self.dragPer(10,50,80,50)
    def dragPerRight(self):
        self.dragPer(80,50,10,50)
    def dragPerUp(self):
        self.dragPer(50,20,50,70)
    def dragPerDown(self):
        self.dragPer(50,70,50,20)



    def resetMapPosition(self):
        winHash=""
        while winHash != screen.winScreenRectHash(self.handle,0,0,50,50):
               self.dragPer(20,20,70,70)
               winHash = screen.winScreenRectHash(self.handle,0,0,50,50)
        self._needResetMap=False
        self._scranMapEnd=False
        self._scranDirection=0

    def scranDragMap(self):#全图扫描
        winHash = screen.winScreenRectHash(self.handle,0,0,50,50)
      
        if self._scranDirection==0:
           self.dragPerRight()
           if winHash==screen.winScreenRectHash(self.handle,0,0,50,50):
               self._nextScranDirection=2     
               self._scranDirection=1
               return
        if self._scranDirection==1:
           self.dragPerDown()
           #换方向左右
           if winHash==screen.winScreenRectHash(self.handle,0,0,50,50):
               self._needResetMap=True
               self._scranMapEnd=True#扫完全图
               return
           self._scranDirection=self._nextScranDirection   
        if self._scranDirection==2:
            self.dragPerLeft()
            if winHash==screen.winScreenRectHash(self.handle,0,0,50,50):
               self._nextScranDirection=0       #左边到尽头 下去后往右
               self._scranDirection=1
               return
        
    def inStoryLevel(self):
        return self.matchResImgInWindow("map//story_level_40_50_55_70.png")


    def onEvenSelectBattle():
        return self.matchResImgInWindow("map//even_select_20_58_80_62.png")
        
    def toEvenBattle():
        self.leftClickPer(70,60)
        


    def canResetMap(self):
        return screen.autoCompareResImgHash(self.handle,"map//map_can_reset_51_86_72_89.png")

    def run(self):    

        diretionLast=0
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
       

    
            print("findUnKnowMap")
            xylist=screen.matchResImgInWindow(self.handle,"map//unkown_52_50_58_54.png",threshold=0.9)
            if  len(xylist)>0:
                # for i in xylist:
                x,y=xylist[0]
                self.leftClick(x,y)
                time.sleep(2)
                self.leftClick(x,y)#需要连点
            else:
                if self._needResetMap == True:
                   self.resetMapPosition()
                   time.sleep(2)
                elif self._scranMapEnd != True:
                   self.scranDragMap()

               

           
     
            
            print("clickOnGetItems")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGetItems()
                time.sleep(2)

            print("hpempty")
            if self.isHpEmpty():
                self.clickOnGetItems()
                time.sleep(2)
            

            if self.inStoryLevel():
                self.leftClickPer(2,2)

            if self.onSelectTeam():
                self.toSelectTeam(blueTeamNo)   
                time.sleep(3)
         


            #体力不足hash 
            print("toUseHp")
            if screen.autoCompareResImgHash(self.handle,"hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

     
            time.sleep(self.interval)
           


