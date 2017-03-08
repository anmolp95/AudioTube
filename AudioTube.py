import json
import pafy
import shutil
from urllib2 import urlopen

API_KEY="AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4"
BASE_URL="https://www.googleapis.com/youtube/v3/search?"
class Audio:
    def __init__(self,id):
        self.id=id
    def getID(self):
        return self.id
    def populate(self,audio,duration):
        self.title=audio[3].title
        self.duration=duration
        self.size=audio[3].get_filesize()
        self.type=audio[3].extension
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
query=raw_input("")
part="snippet"
filter = [("type",typ),("maxResults",maxResults),("q",query),("key",API_KEY),("part",part)]
req=createAPIURL(filter)
print req
gt=None
ct=0
while 1:
    try:
        #gt=requests.get(req)
        gt=urlopen(req).read()
        break
    except:
        ct+=1
        print "try",ct
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
    print "Want to download(y/n)"
    yn=raw_input("")
    if yn=="y":
        downloadFile=audio[3]
        break
try:
    print "Downloading"
    downloadFile.download(".\Songs")
    print "Downloaded"
except WindowsError:
    #shutil.rmtree(".\Songs\\"+audio[-1].title+"."+audio[-1].extension+".temp")
    print "Failed"