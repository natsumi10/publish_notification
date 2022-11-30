import json
import os
import sys
import yaml

import requests
from flask import Flask, request


def base_dir():
	''' Return the path of given file name

	:rtype: str
	'''
	return os.path.dirname(os.path.abspath(__file__))

def config_path():
	'''return the file path of config.json.

	:rtype: str
	'''
	return os.path.join(base_dir(), "config", "config.yml")

def get_config():
	''' get the data in config.json and return it as config
	:rtype: dict
	'''

	with open(config_path(), "r") as fp:
		config = yaml.safe_load(fp)
	return config

def post_w_webhook(mm_config):
	'''post message via webhook
	:rtype: int
	'''
	# This is test for using incomming webhook

	mm_webhook_url = mm_config["webhook_url"]
	
	
	headers = {"Content-type": "application/json"}

	data = {
		"text": "This is test post"
	}

	response = requests.post(mm_webhook_url, json=data, headers=headers)
	print("Status code: {0} {1}".format(response.status_code, response.reason))

	return 0

def post_w_bot(mm_config):
	'''post message via webhook
	:rtype: int
	'''

	# get mattermost bot config
	mm_api_url = mm_config["mm_api_url"]
	bot_token = mm_config["bot_token"]
	channel_id = mm_config["channel_id"]
	
	headers = {
		'Content-type': 'application/json',
		'Authorization': 'Bearer ' + bot_token,
	}

	data = {
		"channel_id": channel_id,
		"message": "This is a message from a bot",
		"username": "publish_notification",
	}
	
	response = requests.post(
		mm_api_url,
		headers = headers,
		json = data
	)

	return 0

def post_mattermost(config):
	'''post message via webhook
	:rtype: int
	'''
	# get mattermost setting
	mm_config = config["mattermost"]
	
	'''
	#post via webhook
	post_w_webhook(mm_config)
	
	# post via publish notification bot
	post_w_bot(mm_config)
	'''
	return 0

def main():
	''' main function 

	:rtype: int
	'''

	config = get_config()
	post_mattermost(config)
	
	


	return 0

if __name__ == "__main__":
	sys.exit(main())