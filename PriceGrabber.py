__author__ = 'junhuang'

import urllib2
import urllib
import json
import cookielib
import BeautifulSoup
import base64

"""
response = urllib2.urlopen("http://www.kbb.com/toyota/corolla/2003-toyota-corolla/ce-sedan-4d/?condition=excellent"+
                           "&intent=trade-in-sell&mileage=200000&val=b&pricetype=private-party")

print response.info

html = response.read()

response.close()

print html
"""


class PriceGrabber:
    def __init__(self):
        self.__sUrl = None
        self.__sResultHTML = None


    def FetchPriceFromUrl(self, sUrl, query_arg):
        sUrl = sUrl or self.__sUrl
        data = urllib.urlencode(query_arg)

        sUrl = sUrl + "&" + data
        zipCode = query_arg["zipCode"]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'
            , 'cookie': 'PersistentZipCode=' + zipCode + ';Referer=kbb.com'
            +'ZipCode='+zipCode
        }

        emptydata = None
        if sUrl is None:
            print "Url is not specified in PriceGrabber Object"
            return
        try:
        #sURL = ("http://www.kbb.com/toyota/camry/2010-toyota-camry/le-sedan-4d/?vehicleid=249075"
        #+"&intent=trade-in-sell&mileage=60000&pricetype=private-party&condition=excellent"
        #+"&val=b&ref=http%3A%2F%2Fwww.kbb.com%2Ftoyota%2Fcamry%2F2010-toyota-camry%"
        #+"2Fle-sedan-4d%2Foptions%2F")
            print sUrl
            req = urllib2.Request(sUrl, emptydata, headers)
            #req.add_header(headers)
            #request.add_data(data)
            #request.add_header(headers)
            print req
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPSHandler(debuglevel=1))

            username = "sosoflying@gmail.com"
            password = "qwer1234"
            base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
            req.add_header("Authorization", "Basic %s" % base64string)
            result = urllib2.urlopen(req)
            #opener.addheaders(headers)
            urllib2.install_opener(opener)
            self.__reobjResponse = urllib2.urlopen(req)
            #for cookie in cj:
            #    print cookie
            #print self.__reobjResponse.read()



        except Exception as e:
            print "oops, this url failed, the exception is " + str(e)
            print sUrl
            #finally:
        #    .urlcleanup()


        if (self.__reobjResponse is None):
            print "HTML response is invalid to process in PriceGrabber Object"
            return

        sPriceDataDict = ""
        bFound = False
        dictResult = {}
        try:
            for sRow in self.__reobjResponse:
                #print sRow
                if sRow.find("zipCode: \"") is not -1:
                    print sRow.strip()
                if sRow.find("data: {\"values\"") is not -1:
                    sPriceDataDict = sRow.strip()[6:]
                    print sPriceDataDict
                    bFound = True

                    # print self.__reobjResponse.read()
                #soup = BeautifulSoup(self.__reobjResponse.read())




            dictResult = json.loads(sPriceDataDict)

            #values = soup.find_all("div", class_="value")
            #print type(values)


        except Exception as e:
            print "Ooops,"
            print sUrl
            print "failed!"

        return dictResult,bFound
"""

sURL = ("http://www.kbb.com/toyota/corolla/2003-toyota-corolla/ce-sedan-4d/?condition=excellent"+
                           "&intent=trade-in-sell&mileage=200000&val=b&pricetype=private-party&ZipCode=40509")




PG = PriceGrabber()
#PG.setFetchURL(sURL)

#PG.StorePriceData()

"""