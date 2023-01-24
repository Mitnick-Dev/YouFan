import sys
import components.setup as stp
from pytube import YouTube as yt
from colorama import Fore

def toContinue():
    toContinue = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" Do you want to continue [y/n]: "+Fore.RESET)
    if toContinue == "y":
        stp.setup()
    elif toContinue == "n":
        sys.exit()
    else:
        stp.resetConsole()
        toContinue = input(Fore.MAGENTA+"[?]->"+Fore.GREEN+" Do you want to continue [y/n]: "+Fore.RESET)

class youFanEvent:
    def __init__(youFanEventObject, eventType, url, downloadPath, downloadFileName):
        youFanEventObject.eventType = eventType
        youFanEventObject.url = url
        youFanEventObject.downloadPath = downloadPath
        youFanEventObject.downloadFileName = downloadFileName
    
    def ytEvent(event):
        if event.eventType == "mp4":
            stp.resetConsole()
            print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" content is searched..."+Fore.RESET)
            ytMp3Downloader = yt(f"{event.url}").streams.filter(mime_type="video/mp4",res="720p",progressive="True")
            if len(ytMp3Downloader) != 0:
                stp.resetConsole()
                print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" downloading..."+Fore.RESET)
                print(Fore.LIGHTRED_EX+"✘"+Fore.LIGHTBLUE_EX+" please do not exit before the process is finished..."+Fore.RESET)
                ytMp3Downloader.desc().first().download(output_path=event.downloadPath, filename=event.downloadFileName)
                print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" successfully downloaded"+Fore.RESET)
                toContinue()
            else:
                stp.resetConsole()
                print(Fore.LIGHTRED_EX+"✘"+Fore.LIGHTBLUE_EX+" could not download..."+Fore.RESET)
                
                
        elif event.eventType == "mp3":
            stp.resetConsole()
            print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" content is searched..."+Fore.RESET)
            ytMp3Downloader = yt(f"{event.url}").streams.filter(mime_type="audio/mp4",abr="128kbps")
            if len(ytMp3Downloader) != 0:
                stp.resetConsole()
                print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" downloading..."+Fore.RESET)
                print(Fore.LIGHTRED_EX+"✘"+Fore.LIGHTBLUE_EX+" please do not exit before the process is finished..."+Fore.RESET)
                ytMp3Downloader.desc().first().download(output_path=event.downloadPath, filename=event.downloadFileName)
                print(Fore.LIGHTGREEN_EX+"✔"+Fore.LIGHTBLUE_EX+" successfully downloaded"+Fore.RESET)
                toContinue()
            else:
                stp.resetConsole()
                print(Fore.LIGHTRED_EX+"✘"+Fore.LIGHTBLUE_EX+" could not download..."+Fore.RESET)