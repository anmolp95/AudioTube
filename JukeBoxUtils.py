import AppConfig
from urllib2 import urlopen
import time
import json
import pafy
import pickle
rh=55
def createAPIURL(baseurl,filters):
    url=baseurl
    ct=0
    for filter in filters:
        if ct==0:
            url = url+ filter[0]+"="+ filter[1]
            ct=1
            continue
        url = url+"&" + filter[0]+"="+ filter[1]
    return url
def tokenise(query):
    tokens=query.split(' ')
    finalQ=""
    count=0
    for token in tokens:
        if count==0:
            finalQ=token
            count+=1
        else:
            finalQ=finalQ+'%20'+token
    return finalQ
def getObjectId(item):
    return item["id"]["videoId"]

def getObjectTitle(item):
    return item["snippet"]["title"]

def getVideoStats(request):
    jsonResponse=None
    tries=0
    while 1:
        try:
            jsonResponse=urlopen(request).read()
            break
        except:

            tries+=1
            print "retry after 10 seconds",tries
            time.sleep(10)
            if tries>5:
                print "Some Other time"
                raise Exception('Youtube Servers Did not respond or network error')
            continue
    youtubeResponse=json.loads(jsonResponse)
    stats=[]
    def checkSanity(ytResposne,key1,key2):
        if key2 in ytResponse[key1]:
            return ytResponse[key1][key2]
        else:
            return 1

    for ytResponse in youtubeResponse["items"]:
        videoStats=[]
        videoStats.append(checkSanity(ytResponse,"contentDetails","duration"))
        videoStats.append(checkSanity(ytResponse,"statistics","viewCount"))
        videoStats.append(checkSanity(ytResponse,"statistics","likeCount"))
        videoStats.append(checkSanity(ytResponse,"statistics","dislikeCount"))
        stats.append(videoStats)
    return stats
def getAudioList(request):
    jsonResponse=None
    tries=0
    while 1:
        try:
            jsonResponse=urlopen(request).read()
            break
        except:

            tries+=1
            print "retry after 10 seconds",tries
            time.sleep(10)
            if tries>5:
                print "Some Other time"
                raise Exception('Youtube Servers Did not respond or network error')
            continue
    youtubeResponse=json.loads(jsonResponse)
    videos=[]
    videoTitle=[]
    for item in youtubeResponse["items"]:
        videoId=getObjectId(item)
        videos.append(videoId)
        videoTitle.append(getObjectTitle(item))
    return (videoTitle,videos)

def addToGlobalSuggestions(newSuggestions):

    try:
        input= open('data.pkl', 'rb')
        globalSuggestions = pickle.load(input)
        input.close()
        output= open('data.pkl', 'wb')
        globalSuggestions=globalSuggestions +newSuggestions
        globalSuggestions.sort(key=lambda x:x.id,reverse=True)
        globalSuggestions=unique(globalSuggestions)
        globalSuggestions.sort(key=lambda x:x.viewcount,reverse=True)
        globalSuggestions=globalSuggestions[0:AppConfig.maxGlobalSuggestions]
        pickle.dump(globalSuggestions, output)
        output.close()
    except:
        output= open('data.pkl', 'wb')
        globalSuggestions=newSuggestions
        globalSuggestions.sort(key=lambda x:x.id,reverse=True)
        globalSuggestions=unique(globalSuggestions)
        globalSuggestions.sort(key=lambda x:x.viewcount,reverse=True)
        globalSuggestions=globalSuggestions[0:AppConfig.maxGlobalSuggestions]
        pickle.dump(globalSuggestions, output)
        output.close()


def getGlobalSuggestionArray():
    try:
        input= open('data.pkl', 'rb')
        globalSuggestions = pickle.load(input)
        input.close()
        return globalSuggestions
    except:
        output= open('data.pkl', 'wb')
        globalSuggestions=[]
        pickle.dump(globalSuggestions, output)
        output.close()
        return globalSuggestions
def unique(globalSuggestion):
    uniqueGlobalSuggestions=[]
    prev=None
    for elem in globalSuggestion:
        if prev==None:
            uniqueGlobalSuggestions.append(elem)
            prev=elem
        elif prev.id !=elem.id:
            #print prev.id ,"is not equal to ",elem.id
            uniqueGlobalSuggestions.append(elem)
            prev=elem
    print "here",len(uniqueGlobalSuggestions)
    return uniqueGlobalSuggestions

def getBestAudioStream(video):
    audio=video.audiostreams
    print len(audio)
    index=min(len(audio)-1,3)
    print index
    return audio[index]




