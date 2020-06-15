import time
import win32gui, win32ui, win32con, win32api
import datetime
import common.path as path
import os
import cv2
import numpy

hashSize=8# 大于8 明汉距离会有很大差异，即使相似图片也会低于0.1
highfreq_factor=6

TOP_OFFSET=40
RIGHT_OFFSET=-37

BOTTOM_OFFSET=-1
LEFT_OFFSET=1

from PIL import ImageGrab,Image
import imagehash



def appGetWindowRect(handle):
   #有改变就加偏移量
   wLeft, wTop, wRight, wBottom = win32gui.GetWindowRect(handle)
   return wLeft+LEFT_OFFSET, wTop+TOP_OFFSET, wRight+RIGHT_OFFSET, wBottom+BOTTOM_OFFSET


def grab_capture(filename,hwnd):
  wLeft, wTop, wRight, wBottom = appGetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  img.save(filename)
  img.close()


def grabCaptureDir(hwnd,dirName):
  win32gui.SetForegroundWindow(hwnd)
  wLeft, wTop, wRight, wBottom = appGetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  phash=imgHash(img,hashSize,highfreq_factor)
  screenPath=path.getProjectPath()+"screen\\"+dirName+"\\"+phash+"_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")+".png"
  if not os.path.exists(path.getProjectPath()+"screen\\"+dirName):
        os.makedirs(path.getProjectPath()+"screen\\"+dirName)
  img.save(screenPath)
  img.close()

def grabCaptureDef(hwnd):
  win32gui.SetForegroundWindow(hwnd)
  wLeft, wTop, wRight, wBottom = appGetWindowRect(hwnd)
  img = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))
  phash=imgHash(img,hashSize,highfreq_factor).__str__()
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

  img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  phash=imgHash(img,hashSize,highfreq_factor)
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
  
   wLeft, wTop, wRight, wBottom = appGetWindowRect(handle)
   width = wRight-wLeft
   return int(wLeft+(width*srcPer))

#获取百分比Y坐标
def getPosY(handle,srcPer):
    if isinstance(srcPer,str) :
        srcPer=float(srcPer.strip())*0.01
    else:
      srcPer=srcPer*0.01
      
    
    wLeft, wTop, wRight, wBottom = appGetWindowRect(handle)
    height = wBottom-wTop
    return int(wTop+(height*(srcPer)))


def getImgHashByPath(path):
   img=Image.open(path)
   hashCode=imgHash(img,hashSize,highfreq_factor)
   img.close()
   return hashCode

def getResImgHashAndSize(fileName):
   imgPath=path.getResDirPath()+fileName
   if not os.path.exists(path.getProjectPath()):
        os.makedirs(path.getProjectPath())
   img=Image.open(imgPath)
   xSize=img.size[0]
   ySize=img.size[1]
   hashCode=imgHash(img,hashSize,highfreq_factor)
   img.close()
   return hashCode,xSize,ySize


def getResImgHash(fileName):
  imgPath=path.getResDirPath()+fileName
  if not os.path.exists(path.getProjectPath()):
        os.makedirs(path.getProjectPath())
  return imgHash(Image.open(imgPath),hashSize,highfreq_factor)






def autoCompareResImgHash(handle,fileName):
  
  return autoCompareResImgHashValue(handle,fileName)>0.3

def autoCompareResImgHashValue(handle,fileName):
  imgPath=path.getResDirPath()+fileName
  tmp=fileName.split(".")
  fSplit=tmp[0].split("_")
  fLen=len(fSplit)
  targetImgPerLeftX=int(fSplit[fLen-4])
  targetImgPerLeftY=int(fSplit[fLen-3])
  targetImgPerRightX=int(fSplit[fLen-2])
  targetImgPerRightY=int(fSplit[fLen-1])

  targetImg=Image.open(imgPath)


  targetImgWidth=targetImg.size[0]
  targetImgHeigth=targetImg.size[1]
  perSize=(targetImgPerRightX-targetImgPerLeftX)*0.01
  resWinWidth=int(targetImgWidth/perSize)
  perSize=(targetImgPerRightY-targetImgPerLeftY)*0.01
  resWinHeight=int(targetImgHeigth/perSize)



  imgScreen=getScreenRectPerImg(handle,targetImgPerLeftX,targetImgPerLeftY,targetImgPerRightX,targetImgPerRightY)

  imgScreen.resize((resWinWidth,resWinHeight),Image.ANTIALIAS)

  hashCode1=imgHash(imgScreen,hashSize,highfreq_factor)
  hashCode2=imgHash(targetImg,hashSize,highfreq_factor)

  targetImg.close()
  imgScreen.close()
  return alikeHashValue(hashCode2,hashCode1)


def screenRectPerHash(hwnd,pLeft, pTop, pRight, pBottom):
  # win32gui.SetForegroundWindow(hwnd)
  # xLeft=getPosX(hwnd,pLeft)
  # yLeft=getPosY(hwnd,pTop)
  # xRight=getPosX(hwnd,pRight)
  # yRight=getPosY(hwnd,pBottom)
  # print("screenRectPerHash" ,xLeft,yLeft , xRight,yRight )
  # img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  
  img=getScreenRectPerImg(hwnd,pLeft, pTop, pRight, pBottom)
  phash=imgHash(img,hashSize,highfreq_factor)
  img.close()
  return phash


def getScreenRectPerImg(hwnd,pLeft, pTop, pRight, pBottom):
  win32gui.SetForegroundWindow(hwnd)
  xLeft=getPosX(hwnd,pLeft)
  yLeft=getPosY(hwnd,pTop)
  xRight=getPosX(hwnd,pRight)
  yRight=getPosY(hwnd,pBottom)
  print("getScreenRectPerImg" ,xLeft,yLeft , xRight,yRight )
  img = ImageGrab.grab(bbox=(xLeft,yLeft , xRight,yRight ))
  return img


def winScreenRectHash(hwnd,pLeft, pTop, pRight, pBottom):
  win32gui.SetForegroundWindow(hwnd)
  wLeft, wTop, wRight, wBottom = appGetWindowRect(hwnd)
  print("winScreenRectHash",wLeft, wTop, wRight, wBottom)
  print("winScreenRectHash2",wLeft+pLeft,wTop+pTop , wLeft+pRight,wTop+pBottom)
  img = ImageGrab.grab(bbox=(wLeft+pLeft,wTop+pTop , wLeft+pRight,wTop+pBottom ))
  phash=imgHash(img,hashSize,highfreq_factor)
  saveTmpImg(img,phash)
  img.close()
  return phash

def alikeHash(hash1,hash2): #明汉距离 实际缩放会在2  哈希字符串 比较差异过大
    length=len(hash1)
    num = 0
    for index in range(len(hash1.encode())): 
        if hash1[index] == hash2[index]: 
            num += 1
  
    res=num/length
    print("alikeHash",length,hash1,hash2,res)
    return  True  if num/length >= 0.35 else False


def imgHash(img,hashSize,highfreq_factor):
    # return imagehash.dhash(img,hashSize).__str__()
     return imagehash.phash(img,hashSize,highfreq_factor).__str__()
    

def alikeHashValue(hash1,hash2): #明汉距离 看情况取值
    length=len(hash1)
    num = 0
    for index in range(len(hash1)): 
        if hash1[index] == hash2[index]: 
            num += 1
  
    res=num/length
    print("alikeHashValue",hash1,hash2,res)
    return  res



# def screenRectPHash(hwnd,pLeft, pTop, pRight, pBottom):
#   win32gui.SetForegroundWindow(hwnd)

#   # print("screenRectPerHash" ,xLeft,yLeft , xRight,yRight )
#   img = ImageGrab.grab(bbox=(pLeft, pTop, pRight, pBottom ))
#   phash=imgHash(img,hashSize,highfreq_factor)
#   img.close()
#   return phash

def saveTmpImg(img,hashCode=""):
  screenPath=path.getProjectPath()+"screen\\tmp\\"+hashCode+"_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") +".png"
  if not os.path.exists(path.getProjectPath()+"screen\\tmp"):
        os.makedirs(path.getProjectPath()+"screen\\tmp")
  img.save(screenPath)








def matchResImgInWindow(handle,imgName,threshold=0.8,mult=True):
  #获取目标图片
  tmp=imgName.split(".")
  fSplit=tmp[0].split("_")
  fLen=len(fSplit)
  targetImgPerLeftX=int(fSplit[fLen-4])
  targetImgPerLeftY=int(fSplit[fLen-3])
  targetImgPerRightX=int(fSplit[fLen-2])
  targetImgPerRightY=int(fSplit[fLen-1])

  imgPath=path.getResDirPath()+imgName
  if not os.path.exists(path.getProjectPath()):
    os.makedirs(path.getProjectPath())
  targetImg=Image.open(imgPath)

  targetImgWidth=targetImg.size[0]
  targetImgHeigth=targetImg.size[1]

  perSize=(targetImgPerRightX-targetImgPerLeftX)*0.01
  resWinWidth=int(targetImgWidth/perSize)
  perSize=(targetImgPerRightY-targetImgPerLeftY)*0.01
  resWinHeight=int(targetImgHeigth/perSize)


  #模板图片
  temImg=cv2.cvtColor(numpy.asarray(targetImg),cv2.COLOR_RGB2BGR)  
  targetImg.close()

  wLeft, wTop, wRight, wBottom = appGetWindowRect(handle)
  winImg = ImageGrab.grab(bbox=(wLeft, wTop, wRight, wBottom))

  #对截图缩放，适配资源图片
  toMatchWinImgSrc=cv2.cvtColor(numpy.asarray(winImg),cv2.COLOR_RGB2BGR)  

  toMatchWinImg=cv2.resize(toMatchWinImgSrc, (resWinWidth,resWinHeight),interpolation=cv2.INTER_AREA)
  winImg.close()

  res = cv2.matchTemplate(toMatchWinImg,temImg,cv2.TM_CCOEFF_NORMED)

  xyList=[]
  if mult==True :
    loc = numpy.where(res>=threshold)

    for pt in zip(*loc[::-1]):
      xyList.append((wLeft+pt[0]+(targetImgWidth>>1),wTop+pt[1]+(targetImgHeigth>>1)))

   
   
  else: #单个很不准确
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc #左上角的位置
    xyList.append((wLeft+top_left[0]+(targetImgWidth>>1),wTop+top_left[1]+(targetImgHeigth>>1)))


  print(xyList)
  return  xyList