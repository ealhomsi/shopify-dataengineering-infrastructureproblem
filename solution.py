#!/usr/bin/python

#https://github.com/ealhomsi/shopify-dataengineering-infrastructureproblem.git

## Shopify data engineering infratstructure problem


#import json lib and url
import urllib, json
import sys #for arguments


#define main (this is an inner join)
def main(argv):
	if not (len(argv) in [3, 5]):
		print("USAGE: " + argv[0] + " <column1> <column2> [<file1>] [<file2>] \n Those two corresponds two url1/file1 and url2/file2 respectivly \n note that if files were not specified the program will use the default url")
		exit(1)

	col1 = argv[1];
	col2 = argv[2];

	customers = None
	orders = None

	if(len(argv) == 3):
		#fetch the first url
		url1 = "https://gist.githubusercontent.com/udnay/d8e2ea75f2cfd7d75482f42549c31c59/raw/60da021e9f083f0c4bf0910f690baf5f38410bc6/customers.json"
		response = urllib.urlopen(url1)
		customers = json.loads(response.read())

		#fetch the second url
		url2 = "https://gist.githubusercontent.com/udnay/20603ff9956064c8d1f1abf7a5e6f5b2/raw/9e841b973a3d9d51940bdffe162c1400a9bac022/orders.json"
		response = urllib.urlopen(url2)
		orders = json.loads(response.read())


	elif(len(argv) == 5):
		file1= argv[3]
		file2= argv[4]

		with open(file1) as json_data:
			customers = json.load(json_data)
	
		with open(file2) as json_data:
			orders = json.load(json_data)
		

    #result array
	result = list()

	#count barry and steve while building the solution
	barryCounter = 0
	steveCounter = 0
	for customer in customers:
		for order in orders:
			if order[col2] == customer[col1]:
				result.append(update(customer, order))
				if(customer[col1] == 1): # this is for barry
					barryCounter+=1
				elif(customer[col1] == 3): # this is for steve
					steveCounter+=1

	print(json.dumps(result))
	print("the length of the resulting array is " + str(len(result)))
	print("\nbarry counter is " + str(barryCounter))
	print("steve counter is " + str(steveCounter))

#def update add customer information to the merged list also it counts
def update(customer, order):
	#precondition those two should have a matching id
	dict1 = order.copy()
	dict2 = customer.copy()

	return (dict(dict1, **dict2))


#run main if this program is requested
if __name__ == "__main__":
	main(sys.argv)