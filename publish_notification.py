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
	print (config)
	

	return 0

if __name__ == "__main__":
	print ("Hello world")
	sys.exit(main())