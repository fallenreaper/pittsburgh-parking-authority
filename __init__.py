# The purpose of INIT will update and define our config files.
# You will need to pass in the API key, which will update conf.json, and all other files.

# After all you will want to do is to ensure elasticsearch is running, then turn on logstash with the correct conf files.
import sys
import json
from pprint import pprint
import requests
from typing import List
import math
#config json is imported into CONFIG in main.
CONFIG = {}

def establish_elasaticsearch():
	pass

def establish_logstash():
	pass

def get_api_request_urls(routes: List):
	if "api_key" not in CONFIG or len(CONFIG["api_key"]) == 0 or "api" not in CONFIG or "getVehicles" not in CONFIG["api"] or "max_vehicles_per_request" not in CONFIG :
		raise KeyError
	n = math.ceil( len(routes) / CONFIG["max_vehicles_per_request"])
	final = [routes[i * n:(i + 1) * n] for i in range((len(routes) + n - 1) // n )]
	# final = [c["rt"] for chunk in final for c in chunk ]
	# print(final)
	for chunk in final:
		yield CONFIG["api"]["getVehicles"].format(
			api_key= CONFIG["api_key"], 
			comma_delimited_list_of_routes= ",".join([ c["rt"] for c in chunk]))
	# return CONFIG["api"]["getVehicles"].format(
	# 	api_key= CONFIG["api_key"], 
	# 	comma_delimited_list_of_routes= ",".join())

def get_all_routes():
	# Returns None or List.
	try:
		if "api_key" not in CONFIG or len(CONFIG["api_key"]) == 0 or "api" not in CONFIG or "getAllRoutes" not in CONFIG["api"]:
			raise KeyError
			# pass
		url = CONFIG["api"]["getAllRoutes"].format(api_key=CONFIG["api_key"])
		print(f"URL: {url}")
		routes = requests.get(url).json()["bustime-response"]["routes"]
		pprint(routes)
		return routes
	except:
		print("Unable to get get all routes.")
		return None

def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print("Need to pass in an API key as an Argument")
		exit(1)
	print("API:", args[0])
	global CONFIG
	with open("config.json", "r") as fp:
		CONFIG = json.load(fp)
	print("CONFIG Information:")
	pprint(CONFIG)
	routes = get_all_routes()
	if routes is None or "max_vehicles_per_request" not in CONFIG:
		exit(1)
	number_requests_to_get_all_routes = math.ceil( len(routes) / CONFIG["max_vehicles_per_request"])
	if "max_requests_per_day" not in CONFIG:
		exit(1)
	daily = CONFIG["max_requests_per_day"]
	minute = daily / 24 / 60
	print(f"How many requests per minute: {minute}")
	print(f"Requests per iteration: {number_requests_to_get_all_routes}")
	minutes_per_scan = math.ceil( number_requests_to_get_all_routes /  minute)
	print(f"Rate of Processing: {minutes_per_scan}")

	pprint(list(get_api_request_urls(routes)))
	


if __name__ == "__main__":
	main()
