import json


with open('rawdata1.json') as f:
    data = json.load(f)



flights = []
for flight in range(0, len(data["scheduledFlights"])): 
	strVal = ""
	
	strVal += (data["scheduledFlights"][flight]["carrierFsCode"])
	strVal += "_" + (data["scheduledFlights"][flight]["flightNumber"])

	flights.append(strVal)

print(flights)