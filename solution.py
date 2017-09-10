#!/usr/bin/python

#https://github.com/ealhomsi/shopify-dataengineering-infrastructureproblem.git

## Shopify data engineering infratstructure problem


#import json lib and url
import urllib, json
import sys #for arguments


#define main (this is an inner join)
def main(argv):
	if(len(argv) != 3):
		print("USAGE: " + argv[0] + " <column1> <column2> \n Those two corresponds two url1 and url2 respectivly")
	
	col1 = argv[1];
	col2 = argv[2];


	#fetch the first url
	url1 = "https://gist.githubusercontent.com/udnay/d8e2ea75f2cfd7d75482f42549c31c59/raw/60da021e9f083f0c4bf0910f690baf5f38410bc6/customers.json"
	response = urllib.urlopen(url1)
	customers = json.loads(response.read())

	#fetch the second url
	url2 = "https://gist.githubusercontent.com/udnay/20603ff9956064c8d1f1abf7a5e6f5b2/raw/9e841b973a3d9d51940bdffe162c1400a9bac022/orders.json"
	response = urllib.urlopen(url2)
	orders = json.loads(response.read())

	result = list()

	for customer in customers:
		result+= [ update(customer, order) for order in orders if order[col2] == customer[col1] ]

	print(json.dumps(result))

#def update add customer information to the merged list
def update(customer, order):
	#precondition those two should have a matching id
	dict1 = order.copy()
	dict2 = customer.copy()
	return (dict(dict1, **dict2))


#run main if this program is requested
if __name__ == "__main__":
	main(sys.argv)