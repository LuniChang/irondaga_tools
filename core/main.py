import win32api,win32gui,win32con
import time
import tkinter as tk
# import math
# import tkinter


from control.reply_battle import ReplyBattle
from control.reply_guess import ReplyGuess
from control.reply_pvp import ReplyPvp
import common.screen as screen



# def MAKELPARAM(x,y):
#     return x+(y<<16)

# class MuMuClick:

# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
handle =screen.getLdHandle()



main = tk.Tk()

replyBattle= ReplyBattle(handle,10)
replyGuess= ReplyGuess(handle,10)


main.title("机动战队工具")
main.geometry("480x600")


def initReplyBattle():
    tk.Button(main,text="开始重复战斗",width=10,height=1,command=replyBattle.start).pack()


    userHp = tk.IntVar()

    def checkUseHp():
        if userHp.get()==1:
            replyBattle.setIsUseHp(True)
        else:
            replyBattle.setIsUseHp(False)  


    tk.Checkbutton(main,text="使用体力药",variable=userHp,onvalue=1,offvalue=0,command=checkUseHp).pack()

    tk.Button(main,text="结束重复战斗",width=10,height=1,command=replyBattle.stop).pack()


initReplyBattle()


tk.Button(main,text="开始重复竞猜",width=10,height=1,command=replyGuess.start).pack()
tk.Button(main,text="结束竞猜",width=10,height=1,command=replyGuess.stop).pack()


replyPvp=ReplyPvp(handle,10)

teamNo=tk.IntVar()

def startPvp():
    replyPvp.setTeamNo(int(teamNo.get()))
    replyPvp.start()

teamNo.set(3)
pvpTeam=tk.Entry(main,textvariable=teamNo)


tk.Button(main,text="开始pvp",width=10,height=1,command=startPvp).pack()
tk.Label(main,text="队伍号").pack()
pvpTeam.pack()
tk.Button(main,text="结束pvp",width=10,height=1,command=replyPvp.stop).pack()

catpture=tk.Button(main,text="窗口截图",width=10,height=1,command=lambda:screen.grabCaptureDef(hwnd=handle))
catpture.pack()

tk.Label(main,text="左X百分比").pack()
xLeft=tk.Entry(main,textvariable=float)
xLeft.pack()

tk.Label(main,text="左Y百分比").pack()
yLeft=tk.Entry(main)
yLeft.pack()

tk.Label(main,text="右X百分比").pack()
xRight=tk.Entry(main)
xRight.pack()

tk.Label(main,text="右Y百分比").pack()
yRight=tk.Entry(main)
yRight.pack()
btnPerCap=tk.Button(main,text="百分比截图",width=10,height=1,command=lambda:screen.grabCaptureRectPerHash(hwnd=handle,tLeft=xLeft.get(),tTop=yLeft.get(), tRight=xRight.get(), tBottom=yRight.get()))
btnPerCap.pack()

tk.Label(main,text="取图片哈希路径").pack()
textPath=tk.Entry(main)
textPath.pack()
texthash=tk.Entry(main)
texthash.pack()
hashBtn=tk.Button(main,text="取图片哈希",width=10,height=1,command=lambda:texthash.insert(index=0,string=screen.getImgPhash(path=textPath.get())) )
hashBtn.pack()





# 进入消息循环
main.mainloop()

# while True:
#   wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(handle)

#   print(wLeft, wTop, wRight, wBottom)
#   win32api.SetCursorPos((getWidthPer(0.27),getHeightPer(0.93)))
#   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN  | win32con.MOUSEEVENTF_LEFTUP, 0,0, 0, 0)
#   time.sleep(5)
#   win32api.SetCursorPos((getWidthPer(0.50),getHeightPer(0.65)))
#   res= win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN  | win32con.MOUSEEVENTF_LEFTUP, 0,0, 0, 0)

#   time.sleep(5)


# exit()