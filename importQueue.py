from queueFile import *
from Tkinter import *

class importQueue(object):

    def __init__(self):
        self.queue = []
        self.datedict = {}

    def dateList(self,fileDate):
        if fileDate not in self.datedict:
            self.datedict[fileDate] = IntVar()

    def append(self, filename):
        self.queue.append(queueFile(filename))
        self.dateList(self.queue[len(self.queue)-1].filedate)

    def getFiles(self):
        # files = []
        # for file in self.queue:
        #     files.append(file.fullname)
        # return files
        return self.queue

    def getDateCount(self):
        # Gets the count for each date
        pass

    def length(self):
        return len(self.queue)

    def getExtCount(self, filetype):
        # Gets teh count of each extension #
        counts = {}
        for file in self.queue:
            ext = file.extension.lower()
            if file.type == filetype:
                if ext not in counts:
                    counts[ext] = 1
                else:
                    counts[ext] += 1
        return counts

    def getTypeCount(self):
        # Get the count for photos vs videos #
        counts = {'Photo':0, 'Video':0}
        for file in self.queue:
            if file.type == 'Photo':
                counts['Photo'] += 1
            elif file.type == 'Video':
                counts['Video'] += 1
            else:
                pass
        return counts

    def  getDateList(self):
        return self.datedict
