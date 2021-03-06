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
    _canUseOil = False

    needBuyRoad=True

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
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(60), self.getPosY(62)))  # 点击使用体力药
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def clickReplyBattle(self):
        screen.setForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(27), self.getPosY(93)))  # 点击重复战斗
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def dragPerLeft(self):
        self.dragPer(5, 50, 95, 50)
        time.sleep(0.3)

    def dragPerRight(self):
        self.dragPer(95, 50, 5, 50)
        time.sleep(0.3)

    def dragPerUp(self):
        self.dragPer(50, 20, 50, 70)
        time.sleep(0.3)

    def dragPerLeftUp(self):
        self.dragPer(5, 20, 95, 70)
        time.sleep(0.3)

    def dragPerDown(self):
        self.dragPer(50, 70, 50, 20)
        time.sleep(0.3)

    def resetMapPosition(self):
        if not self._isScranMap:
            # winHash = ""
            # while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.9):
            #     winHash = screen.winScreenHash(self.handle)
            #     self.dragPerUp()

            winHash = ""
            while not screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.9):
                winHash = screen.winScreenHash(self.handle)
                # self.dragPerLeft()
                self.dragPerLeftUp()

            self._needResetMap = False
            self._scranMapEnd = False
            self._scranDirection = 0

    def scranDragMap(self):  # 全图扫描
        winHash = screen.winScreenHash(self.handle)
        self._isScranMap = True
        if self._scranDirection == RIGHT:
            self.dragPerRight()

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.9):
                self._nextScranDirection = LEFT
                self._scranDirection = DOWN
                return
        if self._scranDirection == DOWN:
            self.dragPerDown()
            # 换方向左右

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.9):
                self._isScranMap = False  # 扫完全图
                return

            self._scranDirection = self._nextScranDirection
        if self._scranDirection == LEFT:
            self.dragPerLeft()

            if screen.alikeHash(winHash, screen.winScreenHash(self.handle), 0.9):
                self._nextScranDirection = RIGHT  # 左边到尽头 下去后往右
                self._scranDirection = DOWN
                return

    def inStoryLevel(self):
        return self.matchResImgInWindow("map//story_level_40_50_55_70.png", 0.75)

    def onEvenSelectBattle(self):
        return self.matchResImgInWindow("map//even_select_20_58_80_62.png", 0.9) or self.matchResImgInWindow("map//even_select3_20_58_80_62.png", 0.9)

    def toEvenBattle(self):
        self.leftClickPer(70, 60)

    def onPvpSelectBattle(self):
        # return self.autoCompareResImgHash("map//buy_road_20_58_40_62.png", 0.9)
        return self.matchResImgInWindow("map//buy_road_20_48_80_62.png")

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

    def onArmyBar(self):
        return self.matchResImgInWindow("map//on_army_bar_50_5_72_10.png") or self.matchResImgInWindow("map//onbar2_0_0_30_10.png")

    def onBlackMarket(self):
        return self.matchResImgInWindow("map//on_black_market_0_0_30_10.png")

    def onYellowPvp(self):
        return self.matchResImgInWindow("map//on_yellow_pvp_20_70_80_80.png")

    def onBusiness(self):
        return self.matchResImgInWindow("map//on_business_65_73_85_76.png")
    

    def clickYellowOK(self):
        self.clickMacthImg("y_ok_56_60_80_65.png")

    def toEndBusiness(self):
        self.leftClickPer(70, 74)

    def skipRocket(self):
        if self.autoCompareResImgHash("rocket_ready_0_0_100_40.png", 0.8):
            self.leftClickPer(50, 50)
           
            time.sleep(10)
            self.leftClickPer(62, 58)
        self.clickMacthImg("rock_back_60_56_75_62.png",0.9)

    def onBusinessAndClose(self):
        screen.setForegroundWindow(self.handle)
        print("onBusinessAndClose")
        xylist = screen.matchResImgInWindow(
            self.handle, "map//on_business_65_73_85_76.png", 0.8)

        if len(xylist) > 0:
            # if self.canChangeRedAir():
            #      self.leftClickPer(75, 34)
            #      time.sleep(3)
            #      self.onDlgOkAndClick()
            #      self.leftClickPer(75, 46)
            #      time.sleep(3)
            #      self.onDlgOkAndClick()
            #      self.leftClickPer(75, 59)
            #      time.sleep(3)
            #      self.onDlgOkAndClick()

            x, y = xylist[0]
            self.leftClick(x, y)

    def onSupportDlg(self):
        return self.matchResImgInWindow("map//on_support_20_75_80_84.png")

    def noSupport(self):
        self.leftClickPer(50, 82)

    def onMap(self):
        print("findUnKnowMap")
        return self.matchResImgInWindow("map//on_map_5_86_22_89.png", 0.5)

    def onDlgAccept(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//accept_60_58_80_62.png", 0.9)
        if len(xylist) > 0:
            x, y = xylist[0]
            self.leftClick(x+2, y+2)
            self.battleEvenCode = 0

    def onDlgChallengeAndClick(self):
        screen.setForegroundWindow(self.handle)

        tarImgs = [
            "map//challenge_60_58_80_62.png",
            "map//challenge2_60_58_80_62.png",
             "map//touxi_60_58_80_62.png",
        ]
        for img in tarImgs:
            xylist = screen.matchResImgInWindow(
                self.handle, img, 0.9)
            if len(xylist) > 0:
                x, y = xylist[0]
                self.leftClick(x+2, y+2)
                self.battleEvenCode = 0

    def onDlgBuyRoadAndClick(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//buy_road_20_58_40_62.png", 0.9)
        if len(xylist) > 0:
            x, y = xylist[0]
            self.leftClick(x+2, y+2)
            self.battleEvenCode = 3

    def onYellowPvpAndBattle(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//yellow_pvp_60_76_80_82.png", 0.9)
        if len(xylist) > 0:
            x, y = xylist[0]
            self.leftClick(x+2, y+2)
            self.battleEvenCode = 3

    def onBlueTacketAndBattle(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//blue_tacket_15_15_40_20.png", 0.9)
        if len(xylist) > 0:
            self.leftClickPer(75, 80)
            self.battleEvenCode = 2

    def closeMapInfoMenu(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//map_infomenu_70_17_98_20.png", 0.9)
        if len(xylist) > 0:
            self.leftClickPer(98, 30)

    def closeStartDlg(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//start_dlg_25_25_75_38.png", 0.9)
        if len(xylist) > 0:
            self.leftClickPer(88, 28)

    def canChangeRedAir(self):
        screen.setForegroundWindow(self.handle)
        xylist = screen.matchResImgInWindow(
            self.handle, "map//shop_red_air_82_40_98_48.png", 0.9)
        return len(xylist) > 0

    def useOil(self):
        self.clickMacthImg("map/oil_58_8_71_15.png")
        time.sleep(5)
        self.clickMacthImg("map/use_60_56_80_62.png")




    def run(self):
        win32gui.SetForegroundWindow(self.handle)
        while self._isRun:
            #
            self.resetCursorPos()

            if self.onEvenSelectBattle():
                # self.toEvenBattle()
                self.battleEvenCode = 0

            # if self.onPvpSelectBattle():
            #     self.noPvp()
            #     time.sleep(2)
            # self.onDlgBuyRoadAndClick()
            if self.needBuyRoad:
                self.onDlgBuyRoadAndClick()
            self.onDlgChallengeAndClick()
            self.onDlgAccept()
            self.onBlueTacketAndBattle()
            self.onYellowPvpAndBattle()
            self.closeMapInfoMenu()
            self.skipRocket()
            self.closeStartDlg()
            if self.onBar():
                self.leftClickPer(10, 70)
                time.sleep(2)
                self.leftClickPer(10, 70)
                time.sleep(2)
                self.leftClickPer(10, 70)
                time.sleep(2)
                self.pressBack()
                time.sleep(3)

            if self.inStoryLevel() or self.onGoldBar() or self.onBlackMarket() or self.onArmyBar():
                self.pressBack()
                time.sleep(3)

            if self.onYellowPvp():
                self.leftClick(78, 78)
                self.battleEvenCode = 1
                time.sleep(2)

            if self.onSelectTeam():
                if self.battleEvenCode == 0:
                    self.toSelectTeam(self.mapTeamNo)
                if self.battleEvenCode == 1:
                    self.toSelectTeam(self.pvpTeamNo)
                if self.battleEvenCode == 2:
                    self.toSelectTeam(self.blueTeamNo)
                if self.battleEvenCode == 3:
                    self.toSelectTeam(self.pvpTeamNo)
                time.sleep(3)

            if self.onTalk():
                self.skipTalk()
                time.sleep(3)

            if self.onDlgOkAndClick():
                continue

            self.clickYellowOK()

            self.onBusinessAndClose()

            print("clickOnGetItems")
            # 获取物品执行
            if self.onGetItems():
                self.clickOnGetItems()
                time.sleep(2)

            # 体力不足hash
            print("toUseHp")
            if self.isHpEmpty():
                if self._isUseHp:
                    self.toUseHp()
                    time.sleep(2)
                self.closeEmptyHp()

            if self.onSupportDlg():
                self.noSupport()
                time.sleep(2)

            if self._canUseOil:
                self.useOil()
                self._canUseOil = False

            if self.canResetMap():
                self.leftClickPer(65, 88)
                time.sleep(2)
                self.onDlgOkAndClick()
                self._isScranMap = False
                self._canUseOil = True

            if self.onMap():
                print("findUnKnowMap")
                xylist = screen.matchResImgInWindow(
                    self.handle, "map//unkown_46_46_54_50.png", 0.7)

                resList = []
                minY = self.getPosY(20)
                maxY = self.getPosY(80)
                for point in xylist:
                    if point[1] >= minY and point[1] <= maxY:
                        resList.append(point)

                if len(resList) > 0:
                    # for i in xylist:

                    x, y = resList[0]
                    cx = self.getPosX(50)
                    cy = self.getPosY(50)
                    # dx=int(cx+(cx-x)/2)
                    # dy=int(cy+(cy-y)/2)
                    self.drag(x, y, cx, cy)  # 拖动不是一比一 大概是一半
                    time.sleep(0.5)
                    self.drag(x, y, cx, cy)
                    time.sleep(2)
                    self.leftClick(cx, cy)
                    time.sleep(2)
                    if self.inStoryLevel():
                        self.pressBack()
                        time.sleep(2)
                    else:
                        self.leftClick(cx, cy)  # 需要连点
                        time.sleep(3)
                    # self.leftClick(x,y)#需要连点
                elif self.onMap():

                    self.resetMapPosition()
                    time.sleep(2)
                    self.scranDragMap()
                    time.sleep(2)
                    continue

            time.sleep(self.interval)
