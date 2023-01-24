import sys
import time
from platform import os
from colorama import Fore
import components.events as event 
from components.introApp import Intro


clearWin = lambda: os.system("cls")
clearLin = lambda: os.system("clear")

def resetConsole():
    if(os.name == "nt"):
        clearWin()
    else:
        clearLin()
    intro = Intro(1)
    intro.randomIntro()

def spaceDetection(x):
    if x == '':
        return False
    else: 
        return True

def downloaderAPI(url, urlCheck, youFanEvent, youFanEventType):
    downloadPath = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" please select the directory where the file will be downloaded [default path]: "+Fore.RESET)
    downloadFileName = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" please enter the name of the file [default name]: "+Fore.RESET)
    dwnldPathInptCntntCheck = filter(spaceDetection, downloadPath.split(" "))
    fileNameInptCntntCheck = filter(spaceDetection, downloadFileName.split(" "))
    
    if len(list(dwnldPathInptCntntCheck)) == 0:
        downloadPath = None
        
    if len(list(fileNameInptCntntCheck)) == 0:
        downloadFileName = None
    else:
        if youFanEventType == "mp4":
            downloadFileName += ".mp4"
        else:
            downloadFileName += ".mp3"
        
    if urlCheck[0] == "https://www.youtube.com/watch":
        downloaderEvent = youFanEvent.youFanEvent(f"{youFanEventType}",f"{url}",downloadPath, downloadFileName)
        downloaderEvent.ytEvent()

def setup():
    resetConsole()
    
    print(Fore.GREEN+"[1]"+Fore.BLUE+" youtube downloads mp4"+Fore.RESET)
    print(Fore.GREEN+"[2]"+Fore.BLUE+" youtube downloads mp3"+Fore.RESET)
    print(Fore.LIGHTRED_EX+"[3] exit app\n"+Fore.RESET)

    choose = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" please choose one of the above actions: "+Fore.RESET)
    print("")

    if(choose == "1"):
        resetConsole()
        url = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" please enter a url: "+Fore.RESET)
        urlCheck = url.split("?v=")
        resetConsole()
        downloaderAPI(url, urlCheck, event, "mp4")
    elif choose == "2":
        resetConsole()
        url = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" please enter a url: "+Fore.RESET)
        urlCheck = url.split("?v=")
        resetConsole()
        downloaderAPI(url, urlCheck, event, "mp3")
    elif choose == "3":
        sys.exit()
    else:
        print(Fore.LIGHTRED_EX+"[!]-> you entered an incorrect value\n"+Fore.RESET)
        time.sleep(1.8)
        setup()