import re
import subprocess
import AppConfig
import time
def sanitiseTitle(title):
    title=re.sub("[|]","",title)
    return title
def quote(string):
    return "\""+string+"\""
def download(url, outputFilename):
    outputPathName=AppConfig.streamLocation+"\\" + outputFilename + AppConfig.extension
    P=subprocess.Popen([AppConfig.ffmpegLocation,"-i",url,"-y",outputPathName],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return P
def stream(inputFilename,delay,pDownload):
    if pDownload.returncode==None:
        print pDownload.returncode
        inputPathName=AppConfig.streamLocation+"\\"+inputFilename+AppConfig.extension
        time.sleep(delay)
        P=subprocess.Popen([AppConfig.ffplayLocation,inputPathName],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return P
    else:
        raise Exception('Not Sucess')
