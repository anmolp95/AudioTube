
class Audio:
    def __init__(self,id,title,videoAttributes=None):
        """
        self.size=audio.get_filesize()
        self.type=audio.extension"""
        #ID
        self.id=id

        #Audio Related Features
        self.title=title

        if videoAttributes:
        #Video Related Features
            self.dur=videoAttributes[0]
            self.viewcount=int(videoAttributes[1])
            self.likes=int(videoAttributes[2])
            self.dislikes=int(videoAttributes[3])
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
