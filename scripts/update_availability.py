import json, urllib, pymongo, datetime
from pymongo import MongoClient
from bson import json_util

# Alko's API returns only 50 products at a time despite a larger pageSize, so we have to fetch results multiple times.
pageSize = 50
pageRange = 6
availabilityUrl = "http://www.alko.fi/api/product/availability?cityId=Helsinki&languageId=fi&productId="

#init DB
#mongoUrl = "mongodb://<your_mongo_db_here>"
#client = client.<your_db_name_here>
#availabilityCollection = db.<your_collection_name_here>"

for page in range(0, pageRange):

	# for debugging
	i = 0
	print "Page " + str(page) + "/" + str(pageRange)

	productUrl = "http://www.alko.fi/api/search/results?q=&tags=tag%3Aoluet&language=fi&page=" + str(page) + "&pageSize=" + str(pageSize) + "&sort=Default"

	#load products
	productData = json.load(urllib.urlopen(productUrl))

	for product in productData["Results"]:
		totalAmount = 0
		storeAvailabilityData = []

		#fetch availability
		availabilityData = json.load(urllib.urlopen(availabilityUrl + product["ProductId"]))

		#fetch the object we are going to modify
		availabilityObject = availabilityCollection.find_one({"productId":product["ProductId"]})

		if availabilityObject is not None:
		#create timestamp
			datenow = datetime.date.today()

			#update store availability and calculate total availability
			for store in availabilityData:
				totalAmount = totalAmount + int(store["Amount"])
				storeData = availabilityCollection.find_one({"productId":product["ProductId"], "availability.store":store["StoreName"]})
				if storeData is not None:
					for singleStore in storeData["availability"]:
						if(store["StoreName"] == singleStore["store"]):
							singleStore["amount"] = store["Amount"]
							singleStore["history"].append({"amount":store["Amount"], "date":str(datenow)})
							storeAvailabilityData.append(singleStore)
			#update object
			availabilityObject["availability"] = storeAvailabilityData
			availabilityObject["amount"] = totalAmount
			availabilityObject["timestamp"] = str(datenow)
			availabilityObject["history"].append({"amount": totalAmount, "date": str(datenow)})

			#debugging
 			print str(i) + "/" + str(len(productData["Results"])) + ": Updated product: " + product["Name"]
 			i = i + 1

 			#save the object
			availabilityCollection.save(availabilityObject)

		else:
			# new product found, add it to db
			
			for store in availabilityData:
				totalAmount = totalAmount + int(store["Amount"])
				storeAvailability.append({"store": store["StoreName"], "amount":store["Amount"], "history":[{"amount":store["Amount"], "date":str(datenow)}]})

			#create JSON
			availabilityCollectionData = {"productId" : product["ProductId"], "name" : product["Name"], "timestamp" : str(datenow), "amount" : totalAmount, "history": [{"amount":totalAmount, "date":str(datenow)}], "availability" : storeAvailability}

			print "Added new product: " + product["Name"]

			#store JSON to DB
			availabilityCollection.insert(availabilityCollectionData)