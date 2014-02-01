__author__ = 'junhuang'


import csv
from PriceGrabber import PriceGrabber
from CountyList import CountyList
import time


class KBBDataCollector:
    def __init__(self):
        self.outPutFile = None
        self.__outPutFile = "./Result/testOutput.csv"
        self.__PriceGrabber = PriceGrabber()
        self.__ZipCodeStoreObject = CountyList()

        self.__slPriceTagType = [
                                     "privatepartyexcellent",
                                     "privatepartyfair",
                                     "privatepartygood",
                                     "privatepartyverygood",
                                     "tradeinfair",
                                     "tradeingood",
                                     "tradeinverygood",
                                ]
        self.__slPriceType = [
                                "priceMin",
                                "price",
                                "priceMax",
                             ]
        self.__lOutputData = [[
                                "Zip",
                                "CD110",
                                "privatepartyexcellent",
                                 "privatepartyfair",
                                 "privatepartygood",
                                 "privatepartyverygood",
                                 "min-tradeinfair",
                                 "tradeinfair",
                                 "max-tradeinfair",
                                 "min-tradeingood",
                                 "tradeingood",
                                 "max-tradeingood",
                                 "min-tradeinverygood",
                                 "tradeinverygood",
                                 "max-tradeinverygood",
                             ]]

    def SetOutPutPath(self,Path):
        self.__outPutFile = Path

    def StorePriceData(self):
        if self.__ZipCodeStoreObject.NeedHeader is False:
            return
        with open(self.__outPutFile, "wb",1) as outputFile:
            writer = csv.writer(outputFile)
            writer.writerows(self.__lOutputData)
        outputFile.close()

    def AppendDataTofile(self,Result):
        self.OutputResult = []
        self.OutputResult.append(Result)

        if self.outPutFile.closed:
            self.outPutFile =  open(self.__outPutFile, "a" , 1)
        writer = csv.writer(self.outPutFile)
        writer.writerows(self.OutputResult)




    def CollectDataByAllZipcode(self,sURL,query_arg = None):

        query_arg = query_arg or {}
        T_StartTime = time.time()
        #if (carModelData is not None):
            #place holder for now
        #    return
        self.__ZipCodeStoreObject.currRec= 0
        NextLocation = self.__ZipCodeStoreObject.FetchNextRec()

        #Write out header of the csv file.
        self.StorePriceData()
        self.outPutFile = open(self.__outPutFile, 'a', 1)
        #Append data to the file
        while(NextLocation):
            startTime = time.time()

            query_arg["zipCode"] = NextLocation["ZIP"]

            print NextLocation["ZIP"]
            Counter = 0
            bFound = False
            while(Counter<15 and bFound is False ):
                try:
                    ResultPriceDataDict , bFound = self.__PriceGrabber.FetchPriceFromUrl(sURL,query_arg)
                except Exception as e:
                    bFound = False
                Counter+=1

            if bFound is True:
                Result = self.FormatDataIntoCSV(ResultPriceDataDict,NextLocation)
                self.AppendDataTofile(Result)
            NextLocation = self.__ZipCodeStoreObject.FetchNextRec()
            elapsedTime = time.time() - startTime

            print elapsedTime
        if self.outPutFile is not None:
            self.outPutFile.close()
        #self.AppendDataTofile([],True)
        T_ElapsedTime = time.time()- T_StartTime

        print "The total elapsed time is " + str(T_ElapsedTime) + " seconds"

        return

    def FormatDataIntoCSV(self,ResultDataDict,LocData):

        if (ResultDataDict is None) or (LocData is None):
            print "No data was fetched from the following zip code: " + LocData
            return

        if ResultDataDict.has_key('values') is False:
            return

        DataDict = ResultDataDict['values']


        Result = [
            LocData["ZIP"],
            LocData["CountyDistrict"],
            DataDict[self.__slPriceTagType[0]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[1]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[2]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[3]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[4]][self.__slPriceType[0]],
            DataDict[self.__slPriceTagType[4]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[4]][self.__slPriceType[2]],
            DataDict[self.__slPriceTagType[5]][self.__slPriceType[0]],
            DataDict[self.__slPriceTagType[5]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[5]][self.__slPriceType[2]],
            DataDict[self.__slPriceTagType[6]][self.__slPriceType[0]],
            DataDict[self.__slPriceTagType[6]][self.__slPriceType[1]],
            DataDict[self.__slPriceTagType[6]][self.__slPriceType[2]]
        ]

        return Result


#sURL = ("http://www.kbb.com/toyota/corolla/2009-toyota-corolla/ce-sedan-4d/?condition=excellent"+
#                           "&intent=trade-in-sell&mileage=60000&val=b&pricetype=private-party")
KBB = KBBDataCollector()

years = [2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003]
milePerY = 15000
counter = 1
for year in years:
    if year is 2013 or year is 2012 or year is 2010 or year is 2011:
        counter += 1
        continue
    sURL = ("http://www.kbb.com/toyota/camry/"+str(year)+"-toyota-camry/le-sedan-4d/?"
        +"&intent=trade-in-sell&mileage="+str(milePerY*counter)+"&pricetype=private-party&condition=excellent"
        +"&val=b&ref=http%3A%2F%2Fwww.kbb.com%2Ftoyota%2Fcamry%2F2010-toyota-camry%"
        +"2Fle-sedan-4d%2Foptions%2F")

    KBB.SetOutPutPath("./Result/Toyota-Camry-"+str(year)+"-"+str(milePerY*counter)+"-ALL-County.csv")

    KBB.CollectDataByAllZipcode(sURL)#,query_arg)
    counter += 1
"""
    query_arg = {
             'vehicleid':249075,
             'intent':'trade-in-sell',
             'mileage':60000,
             'condition':'excellent',
             'val':'b',
             'ref':'http%3a%2f%2fwww.kbb.com%2ftoyota%2fcamry%2f2010-toyota-camry%2fstyles%2f',
             'pricetype':'private-party'
             }
"""