YouCanYouUp
===========
This code is scrapping Toyota Camry LE by different year from 2004 to 2013, increases miles per year by 15000 miles per year.

This also scraps with different zip code, it scraps one zipcode for each 110th congressional 2 digit county district code for all county in the US

The output consist of a CSV file that has the header format of:
Zip,
CD110,
privatepartyexcellent,
privatepartyfair,
privatepartygood,
privatepartyverygood,
min-tradeinfair,
tradeinfair,
max-tradeinfair,
min-tradeingood,
tradeingood,
max-tradeingood,
min-tradeinverygood,
tradeinverygood,
max-tradeinverygood

The records are very self descriptive, the first 2 column is Zipcode and the formmated locationa data of state name abbreviation concatentated with the 2 digits 110th congressional district code

The rest are self descriptive used car value of the car selling to private party or trade in to store.


For zipCodeDB_Trimmed.csv:
===========
Data Records: 42,741

Database Fields:
ZIP
LATITUDE
LONGITUDE
CITY
STATE
COUNTY
ZIP_CLASS

Source: http://www.populardata.com/zipcode_database.html

110CongZipDistrictCode.csv:
===========
Database Fields:
StateCode
ZipCode
Congressional District Code

