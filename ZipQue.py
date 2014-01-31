__author__ = 'junhuang'


import csv



class ZipQue:

    def __init__(self):
        self.__ZipDBFile = "110CongZipDistrictCode.csv"
        self.__ZipDBFileRead = open(self.__ZipDBFile,'rb')
        self.__CurrentLine = 1
        self.ZipDataQue = csv.DictReader(self.__ZipDBFileRead,delimiter=',')
        self.__ProcessedRec = []
        self.STATE_DICT = {1:"AL", 2:"AK", 4:"AZ", 5:"AR", 6:"CA", 8:"CO", 9:"CT", 10:"DE",
				11:"DC", 12:"FL", 13:"GA", 15:"HI", 16:"ID", 17:"IL", 18:"IN",
				19:"IA", 20:"KS", 21:"KY", 22:"LA", 23:"ME", 24:"MD", 25:"MA",
				26:"MI", 27:"MN", 28:"MS", 29:"MO", 30:"MT", 31:"NE", 32:"NV",
				33:"NH", 34:"NJ", 35:"NM", 36:"NY", 37:"NC", 38:"ND", 39:"OH",
				40:"OK", 41:"OR", 42:"PA", 72:"PR", 44:"RI", 45:"SC", 46:"SD",
				47:"TN", 48:"TX", 49:"UT", 50:"VT", 51:"VA", 53:"WA", 54:"WV", 55:"WI", 56:"WY"}
        for row in self.ZipDataQue:
            newRec = {}
            newRec["ZIP"] = row["ZCTA"]
            newRec["CountyDistrict"] = self.STATE_DICT[int(row["STATE"])] + "-" + self.Format(row["CD110"])
            self.__ProcessedRec.append(newRec)
            self.__CurrentLine += 1
        self.NeedHeader = True
        self.currRec = 0

    def FetchNextRec(self):
        if (self.currRec < self.__CurrentLine):
            self.currRec += 1
            #print self.currRec
            #print self.__CurrentLine
            return self.__ProcessedRec[self.currRec]
        else:
            return None

    def Format(self,Data):
        if int(Data) < 10:
            return "0"+Data
        else:
            return str(Data)



"""
que = ZipQue()

myRec =  que.FetchNextRec()

while (myRec):
    print myRec
    myRec = que.FetchNextRec()
"""
