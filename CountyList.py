__author__ = 'junhuang'

from ZipQue import ZipQue
import csv


class CountyList(ZipQue):
    def __init__(self):
        ZipQue.__init__(self)
        self.__CountyList = []
        self.__CountyCount = 0
        self.__ZipDBFile = "110BackUp.csv"
        self.__ZipDBFileRead = open(self.__ZipDBFile,'rb')
        self.ZipDataQue = csv.DictReader(self.__ZipDBFileRead,delimiter=',')

        self.AssignZipToCounty()
        self.__ZipDBFileRead.close()
        self.NeedHeader = True
        self.currRec = 0
    def AssignZipToCounty(self):
        AssignedCounty = {}

        for row in self.ZipDataQue:
            newRec = {}
            newRec["ZIP"] = row["ZCTA"]
            newRec["CountyDistrict"] = self.STATE_DICT[int(row["STATE"])] + "-" + self.Format(row["CD110"])
            if AssignedCounty.has_key(newRec["CountyDistrict"]) is False:
                AssignedCounty[newRec["CountyDistrict"]] = True
                self.__CountyList.append(newRec)
                self.__CountyCount += 1

    def FetchNextRec(self):
        if (self.currRec < self.__CountyCount):
            self.currRec += 1
            return self.__CountyList[self.currRec-1]
        else:
            return None



"""
    def Print(self):
        print self.__CountyList
        print self.__CountyCount
myZip  = CountyList()

myZip.Print()

nextLoc =  myZip.FetchNextRec()

while(nextLoc):
    print nextLoc
    nextLoc = myZip.FetchNextRec()
"""