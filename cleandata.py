import json
from collections import OrderedDict
from datetime import datetime as dt

def formatDate(date):
	clean = dt.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%H:%M")
	strIntVal = clean.replace(":", "")
	strIntVal = strIntVal.lstrip("0")
	return(int(strIntVal))



with open('rawdata1.json') as f:
    data = json.load(f)

with open('rawdata2.json') as f:
    data2 = json.load(f)

with open('rawdata3.json') as f:
    data3 = json.load(f)


flights = []
for flight in range(0, len(data["scheduledFlights"])): 
	
	strVal = ""
	strVal += (data["scheduledFlights"][flight]["carrierFsCode"])
	strVal += "_" + (data["scheduledFlights"][flight]["flightNumber"])

	
	timeVal = formatDate(data["scheduledFlights"][flight]["departureTime"])
	vals = (strVal, timeVal)

	flights.append(vals)



for flight in range(0, len(data2["scheduledFlights"])): 
	
	strVal = ""
	strVal += (data2["scheduledFlights"][flight]["carrierFsCode"])
	strVal += "_" + (data2["scheduledFlights"][flight]["flightNumber"])

	
	timeVal = formatDate(data2["scheduledFlights"][flight]["departureTime"])
	vals = (strVal, timeVal)

	flights.append(vals)

for flight in range(0, len(data3["scheduledFlights"])): 
	
	strVal = ""
	strVal += (data3["scheduledFlights"][flight]["carrierFsCode"])
	strVal += "_" + (data3["scheduledFlights"][flight]["flightNumber"])

	
	timeVal = formatDate(data3["scheduledFlights"][flight]["departureTime"])
	vals = (strVal, timeVal)

	flights.append(vals)


flightDict = OrderedDict(flights)



#print(flightDict)

with open('cleandata.txt', 'w') as file:
     file.write(json.dumps(flightDict))
file.close()