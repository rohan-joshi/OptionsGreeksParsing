#Options screener using Quotemedia's API
import json
import requests
#import csv

def main(): 

	#auth url containing the sid
	
	url_auth= "https://app.quotemedia.com/user/g/authenticate/v0/102368/XXXXXX/XXXXXXX"

	decode_auth = requests.get(url_auth)

	#print decode_auth.json()
	#print(type(decode_auth))	

	auth_data = json.dumps(decode_auth.json())	

	#Parse decode_auth, grab 'sid'	

	sid_parsed = json.loads(auth_data)["sid"]
	#print sid_parsed	

	#Pass sid into qm_options
	#Construct URL
	#http://app.quotemedia.com/data/getOptionQuotes.json?webmasterId=102368&symbol=AAPL&greeks=true&SID=2fa7e706-030c-442b-981b-ef69243ee000	

	symbol = 'AAPL'
	SID  = sid_parsed
	url_raw = 'http://app.quotemedia.com/data/getOptionQuotes.json?webmasterId=102368'	
	

	url_data = url_raw + '&symbol=' + symbol + '&greeks=true' + '&SID=' + SID	

	#print url_data	

	response = requests.get(url_data)
	#print response
	data = json.dumps(response.json())
	#print data	

	#save data to a file	

	with open('AAPL_20151118.json', 'w') as outfile:
		json.dumps (data, outfile)	

	#Turn into json object
	obj = json.loads(data)

	#slim the object
	quotes = obj['results']['quote']

	#find the number of options contracts
	range_count = obj['results']['symbolcount']

	#print all contracts with an vega > 0
	for x in range(0,range_count):
		if quotes[x]['greeks']['vega'] > 0:
			print quotes[x]['key']['symbol']

if __name__ == '__main__':
	main()