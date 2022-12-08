#!/usr/bin/env python

#Init file for Mattermost BOT for Publish notification 

import json
import os
import sys
import yaml
import requests
from mm_post.mm_bot import MmBot

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
	''' read the data from config.yml and return it as dictionary

	:rtype: dict
	'''

	with open(config_path(), "r") as fp:
		config = yaml.safe_load(fp)
	return config


def post_w_webhook(m_bot):
	'''post message via webhook
	:rtype: int
	'''
	# This is test for using incomming webhook
	
	
	headers = {"Content-type": "application/json"}

	data = {
		"text": "This is test post"
	}

	response = requests.post(m_bot.webhook_url, json=data, headers=headers)
	print("Status code: {0} {1}".format(response.status_code, response.reason))

	return 0

def post_mattermost(m_bot):
	'''post message via webhook
	:rtype: int
	'''
	
	#post via webhook
	post_w_webhook(m_bot)
	
	
	return 0

def main():
	''' main function 

	:rtype: int
	'''
	# get mattermost setting
	config = get_config()

	m_bot = MmBot(config)
	m_bot.post()
	#post_mattermost(m_bot)

	return 0

if __name__ == "__main__":
	sys.exit(main())