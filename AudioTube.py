import json
import pafy
from urllib2 import urlopen
import time
import traceback
API_KEY="AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4"
BASE_URL="https://www.googleapis.com/youtube/v3/search?"
class Audio:
    def __init__(self,id):
        self.id=id
    def getID(self):
        return self.id
    def populate(self,audio,duration):
        index=min(len(audio)-1,3)
        self.title=audio[index].title
        self.duration=duration
        self.size=audio[index].get_filesize()
        self.type=audio[index].extension
    def show(self):
        print "Title:",self.title
        print "Duration:",self.duration
        print "Size:",self.size/float(1024*1024)
        print "Type:",self.type
def createAPIURL(filters):
    url=BASE_URL
    ct=0
    for filter in filters:
        if ct==0:
            url = url+ filter[0]+"="+ filter[1]
            ct=1
            continue
        url = url+"&" + filter[0]+"="+ filter[1]
    return url

def getAudio(response):
    id=response["id"]["videoId"]
    aud=Audio(id)
    return aud

typ="video"
maxResults=str(5)
query=raw_input("Enter Song's Name:")
tokens=query.split(' ')
finalQ=""
count=0
for token in tokens:
    if count==0:
        finalQ=token
        count+=1
    else:
        finalQ=finalQ+'%20'+token
part="snippet"
filter = [("type",typ),("maxResults",maxResults),("q",finalQ),("key",API_KEY),("part",part)]
req=createAPIURL(filter)
#print req
print "######Fetched Songs######"
gt=None
ct=0
link="https://www.googleapis.com/youtube/v3/search?type=video&maxResults=5&q=%22kuch%20toh%20bata%20zindagi%22&key=AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4&part=snippet"
while 1:
    try:
        #gt=requests.get(req)
        gt=urlopen(req).read()
        break
    except:
        """print traceback.print_exc()"""
        ct+=1
        print "retry after 10 seconds",ct
        time.sleep(10)
        if ct>5:
            print "Some Other time"
            exit(1)
        continue
x=json.loads(gt)
downloadFile=None
for item in x["items"]:
    audioData=getAudio(item)
    video=pafy.new(audioData.getID())
    audio=video.audiostreams
    audioData.populate(audio,video.duration)
    audioData.show()
    print "Want to download(y/n/e=exit)"
    yn=raw_input("")
    if yn=="y":
        index=min(len(audio)-1,3)
        downloadFile=audio[index]
        break
    elif  yn=="e":
        exit(1)
try:
    print "Downloading"
    downloadFile.download(".\Songs")
    print "Downloaded"
except WindowsError:
    #shutil.rmtree(".\Songs\\"+audio[-1].title+"."+audio[-1].extension+".temp")
    print "Failed"