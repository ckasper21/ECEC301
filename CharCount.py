### Chris Kasper ECE-C301 Lab Week 4 ###

### HW 4 Version
class CharCount(object):
    def __init__(self,txtfile,count):
        with open(txtfile) as f:
           words=[line.split() for line in f]
        wordscount=[]
        for i in range(len(words)):
            for j in range(len(words[i])):
                newword=words[i][j]
                newword=newword.strip("().?!,;:$'")
                if len(newword)==count:
                    wordscount=wordscount+[newword]
        self.words=wordscount

    def __iter__(self):
        index=0
        while index < len(self.words):
            yield self.words[index]
            index+=1

if __name__=="__main__":
    for word in CharCount('agency.txt',11):
        print "'%s'" % word




# Lab 4 Version
# Declaring class Lab 4 Version
##class CharCount(object):
##    def __init__(self,txtfile,count):
##        with open(txtfile) as f:
##           words=[line.split() for line in f]
##        wordscount=[]
##        for i in range(len(words)):
##            for j in range(len(words[i])):
##                newword=words[i][j]
##                newword=newword.strip("().?!,;:$'")
##                if len(newword)==count:
##                    wordscount=wordscount+[newword]
##        self.words=wordscount
##
##    def __iter__(self):
##        return CharCountIterator(self.words)
##
##
##class CharCountIterator(object):
##    def __init__(self,words):
##        self.words=words
##        self.index=0
##
##    def __iter__(self):
##        return self
##
##    def next(self):
##        try:
##            ret=self.words[self.index]
##        except IndexError:
##            raise StopIteration
##        self.index+=1
##        return ret
##
##
##if __name__=="__main__":
##    for word in CharCount('agency.txt',11):
##        print "'%s'" % word



      
        
