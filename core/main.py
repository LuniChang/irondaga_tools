import win32api
import win32gui
import win32con
import time
import tkinter as tk
# import math
# import tkinter


from control.reply_battle import ReplyBattle
from control.reply_guess import ReplyGuess
from control.reply_pvp import ReplyPvp
from control.reply_map import ReplyMap
from control.reply_wushuang import ReplyWuShuang

from control.reply_aixi import ReplyAiXi

from control.momo import Momo

import common.screen as screen


# def MAKELPARAM(x,y):
#     return x+(y<<16)

# class MuMuClick:

# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
handle = screen.getLdHandle()


main = tk.Tk()

replyBattle = ReplyBattle(handle, 10)
replyGuess = ReplyGuess(handle, 10)
replyMap = ReplyMap(handle, 3)
replyWuShuang = ReplyWuShuang(handle, 10)


main.title("机动战队工具")
main.geometry("600x700")

fm1 = tk.Frame(main)
fm1.pack()


def initReplyBattle():

    userHp = tk.IntVar()

    def checkUseHp():
        if userHp.get() == 1:
            replyBattle.setIsUseHp(True)
        else:
            replyBattle.setIsUseHp(False)

    tk.Checkbutton(fm1, text="使用体力药", variable=userHp, onvalue=1,
                   offvalue=0, command=checkUseHp).grid(row=1, column=1)
    tk.Button(fm1, text="开始重复战斗", width=10, height=1,
              command=replyBattle.start).grid(row=1, column=2)
    tk.Button(fm1, text="结束重复战斗", width=10, height=1,
              command=replyBattle.stop).grid(row=1, column=3)


initReplyBattle()

tk.Label(fm1, text="用管理员运行,模拟器分辨率396x701,请勿调整模拟器窗口大小").grid(
    row=0, column=2, columnspan=4)
tk.Button(fm1, text="开始重复竞猜", width=10, height=1,
          command=replyGuess.start).grid(row=2, column=1)
tk.Button(fm1, text="结束竞猜", width=10, height=1,
          command=replyGuess.stop).grid(row=2, column=2)


replyPvp = ReplyPvp(handle, 5)

teamNo = tk.IntVar()


def startPvp():
    replyPvp.setTeamNo(int(teamNo.get()))
    replyPvp.start()


teamNo.set(4)


def initReplyPvp():

    upPoint = tk.IntVar()

    def toUpPoint():
        if upPoint.get() == 1:
            replyPvp.setUpPonit(True)
        else:
            replyPvp.setUpPonit(False)
    tk.Label(fm1, text="PVP:").grid(row=3, column=0)
    tk.Checkbutton(fm1, text="上分", variable=upPoint, onvalue=1,
                   offvalue=0, command=toUpPoint).grid(row=3, column=1)
    tk.Label(fm1, text="队伍号").grid(row=3, column=2)
    tk.Entry(fm1, textvariable=teamNo, width=10).grid(row=3, column=3)

    tk.Button(fm1, text="开始pvp", width=10, height=1,
              command=startPvp).grid(row=3, column=4)

    tk.Button(fm1, text="结束pvp", width=10, height=1,
              command=replyPvp.stop).grid(row=3, column=5)


initReplyPvp()

tk.Button(fm1, text="开始无双", width=10, height=1,
          command=replyWuShuang.start).grid(row=4, column=1)
tk.Button(fm1, text="结束无双", width=10, height=1,
          command=replyWuShuang.stop).grid(row=4, column=2)


def initReplyMap():
    mapTeamNo = tk.IntVar()
    blueTeamNo = tk.IntVar()
    pvpTeamNo = tk.IntVar()
    userHp = tk.IntVar()
    buyRoad = tk.IntVar()
    buyRoad.set(1)

    def checkUseHp():
        if userHp.get() == 1:
            replyMap.setIsUseHp(True)
        else:
            replyMap.setIsUseHp(False)

    def checkBuyRoad():
        if buyRoad.get() == 1:
            replyMap.needBuyRoad = True
        else:
            replyMap.needBuyRoad = False

    def startMap():
        replyMap.mapTeamNo = int(mapTeamNo.get())
        replyMap.blueTeamNo = int(blueTeamNo.get())
        replyMap.pvpTeamNo = int(pvpTeamNo.get())
        replyMap.start()

    mapTeamNo.set(5)
    blueTeamNo.set(1)
    pvpTeamNo.set(4)
    tk.Label(fm1, text="推图设置：").grid(row=5, column=0)
    tk.Label(fm1, text="推图队伍").grid(row=5, column=1)
    tk.Entry(fm1, textvariable=mapTeamNo, width=10).grid(row=5, column=2)
    tk.Label(fm1, text="佣兵队伍").grid(row=6, column=1)
    tk.Entry(fm1, textvariable=blueTeamNo, width=10).grid(row=6, column=2)
    tk.Label(fm1, text="pvp队伍").grid(row=7, column=1)
    tk.Entry(fm1, textvariable=pvpTeamNo, width=10).grid(row=7, column=2)
    tk.Checkbutton(fm1, text="使用体力药", variable=userHp, onvalue=1,
                   offvalue=0, command=checkUseHp).grid(row=8, column=1)
    tk.Checkbutton(fm1, text="买路", variable=buyRoad, onvalue=1,
                   offvalue=0, command=checkBuyRoad).grid(row=8, column=2)

    tk.Button(fm1, text="开始推图", width=10, height=1,
              command=startMap).grid(row=9, column=2)
    tk.Button(fm1, text="结束推图", width=10, height=1,
              command=replyMap.stop).grid(row=9, column=3)


initReplyMap()

replyAiXi = ReplyAiXi(handle, 10)


def initReplyAiXi():
    userHp = tk.IntVar()
    mapTeamNo = tk.IntVar()
    mapTeamNo.set(1)

    def checkUseHp():
        if userHp.get() == 1:
            replyAiXi.setIsUseHp(True)
        else:
            replyAiXi.setIsUseHp(False)

    def startMap():
        replyAiXi.mapTeamNo = int(mapTeamNo.get())

        replyAiXi.start()

    tk.Label(fm1, text="艾希队伍").grid(row=10, column=0)
    tk.Entry(fm1, textvariable=mapTeamNo, width=10).grid(row=10, column=1)

    tk.Checkbutton(fm1, text="使用体力药", variable=userHp, onvalue=1,
                   offvalue=0, command=checkUseHp).grid(row=10, column=2)
    tk.Button(fm1, text="开始艾希", width=10, height=1,
              command=startMap).grid(row=10, column=3)
    tk.Button(fm1, text="结束艾希", width=10, height=1,
              command=replyAiXi.stop).grid(row=10, column=4)


initReplyAiXi()


momo = Momo(handle, 0)


def initMomo():

    evenCount = tk.IntVar()
    evenCount.set(40)
    def startMomo():
        momo.maxCount = int(evenCount.get())
        momo.start()

    tk.Label(fm1, text="摸一摸：次数").grid(row=11, column=0)
    tk.Entry(fm1, textvariable=evenCount, width=10).grid(row=11, column=1)
    tk.Button(fm1, text="开始摸摸", width=10, height=1,
              command=startMomo).grid(row=11, column=2)
    tk.Button(fm1, text="结束摸摸", width=10, height=1,
              command=momo.stop).grid(row=11, column=3)

initMomo()

tk.Label(main, text="工具操作").pack()

# fmTools=tk.Frame(main).pack()
tk.Button(main, text="窗口截图", width=10, height=1,
          command=lambda: screen.grabCaptureDef(hwnd=handle, needShow=True)).pack()


tk.Label(main, text="左X百分比").pack()
xLeft = tk.Entry(main, textvariable=float)
xLeft.pack()

tk.Label(main, text="左Y百分比").pack()
yLeft = tk.Entry(main)
yLeft.pack()

tk.Label(main, text="右X百分比").pack()
xRight = tk.Entry(main)
xRight.pack()

tk.Label(main, text="右Y百分比").pack()
yRight = tk.Entry(main)
yRight.pack()
btnPerCap = tk.Button(main, text="百分比截图", width=10, height=1, command=lambda: screen.grabCaptureRectPerHash(
    hwnd=handle, tLeft=xLeft.get(), tTop=yLeft.get(), tRight=xRight.get(), tBottom=yRight.get(), needShow=True))
btnPerCap.pack()

# tk.Label(main,text="取图片哈希路径").pack()
# textPath=tk.Entry(main)
# textPath.pack()
# texthash=tk.Entry(main)
# texthash.pack()
# hashBtn=tk.Button(main,text="取图片哈希",width=10,height=1,command=lambda:texthash.insert(index=0,string=screen.getImgHashByPath(path=textPath.get())) )
# hashBtn.pack()


# 进入消息循环
main.mainloop()

main.protocol("WM_DELETE_WINDOW", exit(0))

