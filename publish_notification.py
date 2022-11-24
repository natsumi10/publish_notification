import json
import os
import sys

import requests

def base_dir():
	''' Return the path of given file name

	:rtype: str
	'''
	return os.path.dirname(os.path.abspath(__file__))

def config_path():
	'''return the file path of config.json.

	:rtype: str
	'''
	return os.path.join(base_dir(), "config", "config.json")

def get_config():
	''' get the data in config.json and return it as config
	:rtype: str
	'''

	with open(config_path(), "r") as fp:
		config = json.load(fp)
	return config

def main():
	''' main function 

	:rtype: int
	'''

	config = get_config()
	
	# get mattermost setting
	mm_config = config["mattermost"]
	mm_webhook_url = mm_config["webhook_url"]

	headers = {"Content-type": "application/json"}

	data = {
		"text": "This is test post"
	}

	response = requests.post(mm_webhook_url, json=data, headers=headers)
	print("Status code: {0} {1}".format(response.status_code, response.reason))

	


	return 0

if __name__ == "__main__":
	sys.exit(main())