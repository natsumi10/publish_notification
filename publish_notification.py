#!/usr/bin/env python

#Init file for Mattermost BOT for Publish notification 

import json
import os
import sys
import yaml
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
	return os.path.join(base_dir(), "config", "config.yml")

def get_config():
	''' get the data in config.json and return it as config
	:rtype: dict
	'''

	with open(config_path(), "r") as fp:
		config = yaml.safe_load(fp)
	return config

class PnBot:
	'''Base Publish Notification Bot class.
	'''
	def __init__(self,config):
		mm_config = config["mattermost"]
		self.mm_webhook_url = mm_config["webhook_url"]
		self.mm_api_url = mm_config["mm_api_url"]
		self.bot_token = mm_config["bot_token"]
		self.channel_id = mm_config["channel_id"]


def post_w_webhook(m_bot):
	'''post message via webhook
	:rtype: int
	'''
	# This is test for using incomming webhook
	
	
	headers = {"Content-type": "application/json"}

	data = {
		"text": "This is test post"
	}

	response = requests.post(m_bot.mm_webhook_url, json=data, headers=headers)
	print("Status code: {0} {1}".format(response.status_code, response.reason))

	return 0

def post_w_bot(m_bot):
	'''post message via webhook
	:rtype: int
	'''

	headers = {
		'Content-type': 'application/json',
		'Authorization': 'Bearer ' + m_bot.bot_token,
	}

	data = {
		"channel_id": m_bot.channel_id,
		"message": "This is a message from a bot",
		"username": "publish_notification",
	}
	
	response = requests.post(
		m_bot.mm_api_url,
		headers = headers,
		json = data
	)

	return 0

def post_mattermost(m_bot):
	'''post message via webhook
	:rtype: int
	'''
	
	#post via webhook
	post_w_webhook(m_bot)
	
	# post via publish notification bot
	post_w_bot(m_bot)
	
	return 0

def main():
	''' main function 

	:rtype: int
	'''
	# get mattermost setting
	config = get_config()

	m_bot = PnBot(config)
	post_mattermost(m_bot)

	return 0

if __name__ == "__main__":
	sys.exit(main())