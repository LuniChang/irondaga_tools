import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen

RIGHT = 0
DOWN = 1
LEFT = 2


class ReplyMap(BaseControl):

    mapTeamNo = 5
    pvpTeamNo = 4
    blueTeamNo = 2

    _needBuyHp = False
    _isUseHp = False

    _isScranMap = False
    _scranDirection = 0  # 0 → 1 ↓ 2←
    _nextScranDirection = 0

    battleEvenCode = 0  # 0 普通事件  1 黄票  2蓝票

    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def setIsUseHp(self, isUseHp):
        self._isUseHp = isUseHp

    # 点在判断窗口中点位置的哪个方向
    def xyDirection(self, x, y):
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)

        centerX = (wRight-wLeft) >> 1
        centerY = (wTop-wBottom) >> 1
        inLeft = True
        inTop = True
        if x > centerX:
            inLeft = False
        if y > centerY:
            inTop = False
        return inLeft, inTop

    def buyHp(self):
        pass

    def toUseHp(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(60), self.getPosY(62)))  # 点击使用体力药
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def clickReplyBattle(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(27), self.getPosY(93)))  # 点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



    def dragPerLeft(self):
        self.dragPer(20, 50, 80, 50)

    def dragPerRight(self):
        self.dragPer(80, 50, 20, 50)

    def dragPerUp(self):
        self.dragPer(50, 20, 50, 70)

    def dragPerDown(self):
        self.dragPer(50, 70, 50, 20)

    def resetMapPosition(self):
        if not self._isScranMap:
            winHash = ""
            while winHash != screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self.dragPer(20, 20, 70, 70)
                time.sleep(1)
                winHash = screen.winScreenRectHash(self.handle, 0, 0, 50, 50)

            self._needResetMap = False
            self._scranMapEnd = False
            self._scranDirection = 0

    def scranDragMap(self):  # 全图扫描
        winHash = screen.winScreenRectHash(self.handle, 0, 0, 50, 50)
        self._isScranMap = True
        if self._scranDirection == RIGHT:
            self.dragPerRight()
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._nextScranDirection = LEFT
                self._scranDirection = DOWN
                return
        if self._scranDirection == DOWN:
            self.dragPerDown()
            # 换方向左右
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._isScranMap = False  # 扫完全图
                return

            self._scranDirection = self._nextScranDirection
        if self._scranDirection == LEFT:
            self.dragPerLeft()
            if winHash == screen.winScreenRectHash(self.handle, 0, 0, 50, 50):
                self._nextScranDirection = RIGHT  # 左边到尽头 下去后往右
                self._scranDirection = DOWN
                return

    def inStoryLevel(self):
        return self.matchResImgInWindow("map//story_level_40_50_55_70.png")

    def onEvenSelectBattle(self):
        return self.matchResImgInWindow("map//even_select_20_58_80_62.png", 0.9) or self.matchResImgInWindow("map//even_select3_20_58_80_62.png", 0.9)

    def toEvenBattle(self):
        self.leftClickPer(70, 60)

    def onPvpSelectBattle(self):
        return self.matchResImgInWindow("map//pvp_select_20_58_80_62.png", 0.9)

    def noPvp(self):
        self.leftClickPer(22, 60)

    def onTalk(self):
        return self.matchResImgInWindow("map//talk_20_80_80_85.png")

    def skipTalk(self):
        self.leftClickPer(50, 80)

    def pressBack(self):
        self.leftClickPer(2, 2)

    def canResetMap(self):
        return self.matchResImgInWindow("map//map_can_reset_51_86_72_89.png")

    def onGoldBar(self):
        return self.matchResImgInWindow("map//on_gold_bar_0_0_30_10.png")

    def onBar(self):
        return self.matchResImgInWindow("map//on_bar_0_0_30_10.png")

    def onBlackMarket(self):
        return self.matchResImgInWindow("map//on_black_market_0_0_30_10.png")

    def onYellowPvp(self):
        return self.matchResImgInWindow("map//on_yellow_pvp_20_70_80_80.png")

    def onBusiness(self):
        return self.matchResImgInWindow("map//on_business_65_73_85_76.png")

    def toEndBusiness(self):
        self.leftClickPer(70, 74)

    def onSupportDlg(self):
        return self.matchResImgInWindow("map//on_support_20_75_80_84.png")

    def noSupport(self):
        self.leftClickPer(50, 82)

    def onMap(self):
        return self.matchResImgInWindow("map//on_map_5_86_22_89.png",0.9)

    def onDlgChallengeAndClick(self):
        win32gui.SetForegroundWindow(self.handle)
        xylist=screen.matchResImgInWindow(self.handle,"map//challenge_60_58_80_62.png",0.9)
        if len(xylist) >0:
             x, y = xylist[0]
             self.leftClick(x+2, y+2)
             self.battleEvenCode == 0

    def onDlgBuyRoadAndClick(self):
        win32gui.SetForegroundWindow(self.handle)
        xylist=screen.matchResImgInWindow(self.handle,"map//buy_road_20_58_40_62.png",0.9)
        if len(xylist) >0:
             x, y = xylist[0]
             self.leftClick(x+2, y+2)
             self.battleEvenCode == 0

             

    def run(self):

        diretionLast = 0
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)
            self.resetCursorPos()

            if self.onEvenSelectBattle():
                # self.toEvenBattle()
                self.battleEvenCode == 0
                
            self.onDlgBuyRoadAndClick()
            self.onDlgChallengeAndClick()
           
                # time.sleep(2)
            # if self.onPvpSelectBattle():
            #     self.noPvp()
            #     time.sleep(2)

            if self.inStoryLevel() or self.onGoldBar() or self.onBlackMarket():
                self.pressBack()
                time.sleep(2)

            if self.onYellowPvp():
                self.leftClick(78, 78)
                self.battleEvenCode == 1
                time.sleep(2)

            if self.onSelectTeam():
                if self.battleEvenCode == 0:
                    self.toSelectTeam(self.mapTeamNo)
                if self.battleEvenCode == 1:
                    self.toSelectTeam(self.pvpTeamNo)
                if self.battleEvenCode == 2:
                    self.toSelectTeam(self.blueTeamNo)

                time.sleep(3)

            if self.onTalk():
                self.skipTalk()
                time.sleep(2)

            # if self.onDlgOK():
            #     print("onDlgOK")
            #     self.clickDlgOK()
            #     time.sleep(2)
            
            self.onDlgOkAndClick()
      
            
            if self.onBusiness():
                self.toEndBusiness()
                time.sleep(2)

            print("clickOnGetItems")
            # 获取物品执行
            if self.onGetItems():
                self.clickOnGetItems()
                time.sleep(2)

            print("hpempty")
            if self.isHpEmpty():
                self.clickOnGetItems()
                time.sleep(2)

            # 体力不足hash
            print("toUseHp")
            if screen.autoCompareResImgHash(self.handle, "hpempty_10_40_80_65.png"):
                self.toUseHp()
                time.sleep(2)
                self.closeEmptyHp()

            if self.onSupportDlg():
                self.noSupport()
                time.sleep(2)

            if self.canResetMap():
                self.leftClickPer(65, 88)
                self._isScranMap = False

            print("findUnKnowMap")
            xylist = screen.matchResImgInWindow(
                self.handle, "map//unkown_46_46_54_50.png", threshold=0.85)
            if len(xylist) > 0:
                # for i in xylist:
                x, y = xylist[0]
                self.leftClick(x, y)
                time.sleep(2)
                self.leftClick(x, y)  # 需要连点
                # time.sleep(2)
                # self.leftClick(x,y)#需要连点
            elif self.onMap():
                

                self.resetMapPosition()
                time.sleep(2)
                self.scranDragMap()
                time.sleep(2)

            time.sleep(self.interval)
