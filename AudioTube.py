import requests
import json
import pafy
from urllib2 import urlopen

API_KEY="AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4"
BASE_URL="https://www.googleapis.com/youtube/v3/search?"
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

def getVideoID(responses):
    for response in responses:
        return response["id"]["videoId"]


typ="video"
maxResults=str(5)
query="\"cheap thrills\""
part="snippet"
filter = [("type",typ),("maxResults",maxResults),("q",query),("key",API_KEY),("part",part)]
req=createAPIURL(filter)
gt=requests.get(req)
x=json.loads(gt.text)
videoID=getVideoID(x["items"])
video=pafy.new(videoID)
audio=video.audiostreams
u = urlopen(audio[3].url)
inf=u.info()
print inf.subtype
data=u.read(1000000)
with open('./test.mp3','wb') as output:
  output.write(data)
  """
ct=0
while(data):
    print data
    ct+=1
    data=u.read(1000)"""