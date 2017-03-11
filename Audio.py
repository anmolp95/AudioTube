import Utils
import AppConfig
import time
class Audio:
    def __init__(self,id,title,videoAttributes=None):
        """
        self.size=audio.get_filesize()
        self.type=audio.extension"""
        #ID
        self.id=id

        #Audio Related Features
        self.title=Utils.sanitiseTitle(title)

        if videoAttributes:
        #Video Related Features
            self.dur=videoAttributes[0]
            self.viewcount=int(videoAttributes[1])
            self.likes=int(videoAttributes[2])
            self.dislikes=int(videoAttributes[3])
        self.audioStream=None
    def __hash__(self):
        return hash(self.id)

    def show(self):
        print "Title:",self.title
        print "Id:",self.id
        print "Views:",self.viewcount
        liking=self.likes*50/(self.likes+self.dislikes)
        disliking=self.dislikes*50/(self.likes+self.dislikes)
        #Low level features
        print "Duration:",self.dur
        likeStr='+'*liking
        dislikeStr='-'*disliking
        print "Likes %d , Disklikes %d " %(self.likes,self.dislikes)
        print likeStr+dislikeStr
        """sizeInMb=self.size/float(1024*1024)
        print "Size: %.3f MB" %sizeInMb
        print "Type:",self.type"""
        return

    def populateStreamInfo(self,audioStream):
        self.audioStream=audioStream
        #self.audioStream=audioStream

    def isPrepared(self):
        if self.audioStream!=None:
            return True
        else:
            return False
    def stream(self):
        if self.isPrepared():
            x1=Utils.download(self.audioStream.url,self.title)
            print "Started..."
            succ=False
            ct=0
            while 1:
                ct+=1
                ret=x1.stderr.readline()
                print ret
                if "Press [q] to stop, [?] for help" in ret:
                    succ=True
                    #break
                if ct>40:
                    break
            print "Yes"
            if succ == True:
               print "Not succ"
               # x2=Utils.stream(self.title,AppConfig.streamDelay,x1)
            else:
                raise Exception(" Coudn't Start Stream ")
        else:
            raise Exception('Audio Streams Not Prepared Yet do audioObject.prepare()')