import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

class ReplyAiXi(BaseControl):

  
    mapTeamNo = 5
    _needBuyHp=False
    _isUseHp=False

    _mapBattleCount=0
    _mapPointLocation=[(16,28),(50,28),(84,28),(16,50),(50,50),(84,50),(50,72)]
    _mapBattlePoint=0
    _isInBattle=False
    def __init__(self,handle,interval):
        self.handle=handle
        self.interval=interval

    def setIsUseHp(self,isUseHp):
        self._isUseHp=isUseHp
    



    def buyHp(self):
        pass

    def toUseHp(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(62), self.getPosY(60)))#点击使用体力药
        win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
   

    def clickReplyBattle(self):
        self.leftClickPer(35,93)     

    def clickContinue(self):
        self.leftClickPer(85,93) 

    def onMap(self):
        print("findUnKnowMap")
        return screen.autoCompareResImgHash(self.handle, "zhangjiepingjia_40_86_60_89.png", 0.8)

    

    def run(self):    
        self._mapBattleCount=0
        self._mapBattlePoint=0
        while self._isRun:
            screen.setForegroundWindow(self.handle)

            if self.onMap():
                x,y=self._mapPointLocation[self._mapBattlePoint]
                self.leftClickPer(x,y)
                self._mapBattlePoint+=1
                if self._mapBattlePoint>8 :
                    return
                time.sleep(5)    


            if self.onSelectTeam():
               self.toSelectTeam(self.mapTeamNo)
               time.sleep(2)
            

            self.onDlgOkAndClick()
            self.findImgAndclick("aixi/mapread_40_50_60_70.png")
            #底部菜单hash 
            print("clickReplyBattle")
            if screen.autoCompareResImgHash(self.handle,"reply/end_0_90_40_95.png") or screen.autoCompareResImgHash(self.handle,"reply//end_0_90_100_95.png"):
               
                self._isInBattle=True
                self.clickReplyBattle()
                self._mapBattleCount+=1
                time.sleep(5)
                if self._mapBattleCount>6 :
                   self.clickContinue()


           
            print("clickOnGetItems")
            #获取物品执行
            if self.onGetItems() :
                self.clickOnGetItems()
                time.sleep(2)
            else :
                pass

            #体力不足hash 
            print("toUseHp")
            if self._isUseHp and self.isHpEmpty():
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            else :
                
               pass

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")



