import urllib2, json, sqlite3

query = "https://data.cityofnewyork.us/resource/2fra-mtpn.json?$select=ofns_desc,latitude,longitude"

'''f="crime.db"
db=sqlite.connect(f)
c=db.cursor()
'''
def crimeCall():
	try:
		ret = []
		u = urllib2.urlopen(query)
		data=json.load(u)
		u.close()
		'''for key in data:
			try:
				list = []
				list.append(key['latitude'])
				list.append(key['longitude'])
				list.append(key['ofns_desc'])
				ret.append(list)
			except:
				pass
		'''
		#return ret
		return data
	except urllib2.HTTPError, e:
		return "HTTP error: {}".format(e.code)
	except urllib2.URLError, e:
		return "Network error: {}".format(e.reason.args[1])
	
	##json_string = u.read()
	##parsed_json = json.loads(json_string)
	##return parsed_json.keys()
	
print crimeCall()

