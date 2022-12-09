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


def main():
	''' main function 

	:rtype: int
	'''
	# get mattermost setting
	config = get_config()

	m_bot = MmBot(config)
	#m_bot.post()
	#m_bot.postWebhook()
	
	return 0

if __name__ == "__main__":
	sys.exit(main())