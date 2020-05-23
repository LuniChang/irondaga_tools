import time
import win32gui, win32ui, win32con, win32api
import datetime
import common.path as path
import os


hashSize=16

#此方式会黑屏
def window_capture(filename,hwnd):
 # hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
 
  win32gui.SetForegroundWindow(hwnd)
  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 获取监控器信息
#   MoniterDev = win32api.EnumDisplayMonitors(None, None)
#   w = MoniterDev[0][2][2]
#   h = MoniterDev[0][2][3]
  wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(hwnd)
  w = wRight-wLeft
  h = wBottom-wTop
  print( wLeft, wTop, wRight, wBottom,w,h)
  # print w,h　　　#图片大小
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)
  # 截取从左上角（0，0）长宽为（w，h）的图片
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(saveDC, filename)

  win32gui.DeleteObject(saveBitMap.GetHandle())

  mfcDC.DeleteDC()
  saveDC.DeleteDC()
  win32gui.ReleaseDC(hwnd, hwndDC)



from PIL import ImageGrab,Image
import imagehash

def grab_capture(filename,hwnd):
  wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  img.save(filename)
  img.close()


def grabCaptureDir(hwnd,dirName):
  win32gui.SetForegroundWindow(hwnd)
  wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  phash=imagehash.phash(img,hashSize).__str__()
  screenPath=path.getProjectPath()+"screen\\"+dirName+"\\"+phash+"_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")+".png"
  if not os.path.exists(path.getProjectPath()+"screen\\"+dirName):
        os.makedirs(path.getProjectPath()+"screen\\"+dirName)
  img.save(screenPath)
  img.close()

def grabCaptureDef(hwnd):
  win32gui.SetForegroundWindow(hwnd)
  wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  phash=imagehash.phash(img,hashSize).__str__()
  screenPath=path.getProjectPath()+"screen\\"+phash+"_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")+".png"
  if not os.path.exists(path.getProjectPath()+"screen"):
        os.makedirs(path.getProjectPath()+"screen")
  img.save(screenPath)
  img.close()


def grabCaptureRect(hwnd,tLeft, tTop, tRight, tBottom):
  win32gui.SetForegroundWindow(hwnd)
  img = ImageGrab.grab(bbox=(tLeft, tTop, tRight, tBottom))
  screenPath=path.getProjectPath()+"screen\\rect\\"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")+".png"
  if not os.path.exists(path.getProjectPath()+"screen\\rect"):
        os.makedirs(path.getProjectPath()+"screen\\rect")
  img.save(screenPath)
  img.close()


def grabCaptureRectPer(hwnd,tLeft, tTop, tRight, tBottom):
  win32gui.SetForegroundWindow(hwnd)

  xLeft=getPosX(hwnd,tLeft)
  yLeft=getPosY(hwnd,tTop)
  xRight=getPosX(hwnd,tRight)
  yRight=getPosY(hwnd,tBottom)
  print(xLeft,yLeft , xRight,yRight )

  img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  screenPath=path.getProjectPath()+"screen\\rect_per\\"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")+"_"+str(xLeft)+"_"+str(yLeft) +"_"+ str(xRight)+"_"+str(yRight) +".png"
  if not os.path.exists(path.getProjectPath()+"screen\\rect_per"):
        os.makedirs(path.getProjectPath()+"screen\\rect_per")
  img.save(screenPath)
  img.close()

def grabCaptureRectPerHash(hwnd,tLeft, tTop, tRight, tBottom):
  win32gui.SetForegroundWindow(hwnd)

  xLeft=getPosX(hwnd,tLeft)
  yLeft=getPosY(hwnd,tTop)
  xRight=getPosX(hwnd,tRight)
  yRight=getPosY(hwnd,tBottom)
  print(xLeft,yLeft , xRight,yRight )

  img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  phash=imagehash.phash(img,hashSize).__str__()
  screenPath=path.getProjectPath()+"screen\\rect_per\\"+phash+"_"+str(tLeft)+"_"+str(tTop) +"_"+ str(tRight)+"_"+str(tBottom) +".png"
  if not os.path.exists(path.getProjectPath()+"screen\\rect_per"):
        os.makedirs(path.getProjectPath()+"screen\\rect_per")
  img.save(screenPath)
  img.close()



def getLdHandle():
  return win32gui.FindWindow("LDPlayerMainFrame", "雷电模拟器") 
  


#获取百分比X坐标
def getPosX(handle,srcPer):
   if isinstance(srcPer,str) :
        srcPer=float(srcPer.strip())*0.01
   else:
     srcPer=srcPer*0.01
  
   wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(handle)
   width = wRight-wLeft
   return int(wLeft+(width*srcPer))

#获取百分比Y坐标
def getPosY(handle,srcPer):
    if isinstance(srcPer,str) :
        srcPer=float(srcPer.strip())*0.01
    else:
      srcPer=srcPer*0.01
      
    
    wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(handle)
    height = wBottom-wTop
    return int(wTop+(height*(srcPer)))


def getImgPhash(path):
  return imagehash.phash(Image.open(path),hashSize)

def screenRectPerHash(hwnd,pLeft, pTop, pRight, pBottom):
  win32gui.SetForegroundWindow(hwnd)
  xLeft=getPosX(hwnd,pLeft)
  yLeft=getPosY(hwnd,pTop)
  xRight=getPosX(hwnd,pRight)
  yRight=getPosY(hwnd,pBottom)
  print("screenRectPerHash" ,xLeft,yLeft , xRight,yRight )
  img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  phash=imagehash.phash(img,hashSize).__str__()
  img.close()
  return phash

def difHash(hash1,hash2): #明汉距离 取小于0.5相似
    l=len(hash1)
    num = 0
    for index in range(len(hash1)): 
        if hash1[index] != hash2[index]: 
            num += 1
    return num/l