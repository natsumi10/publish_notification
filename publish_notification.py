#!/usr/bin/env python

#Init file for Mattermost BOT for Publish notification 

import json
import os
import sys
import yaml
import requests
from shotgun_api3 import Shotgun

from mm_post.mm_bot import MmBot
from mm_post.mm_shotgrid import MmShotgrid

class IdentityError(Exception):
	pass

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

def post_mattermost(config):
	''' post to mattermost

	:rtype: int
	'''
	m_bot = MmBot(config)
	
	# set message to post
	message = "This is test!"
	m_bot.set_message(message)
	
	# post via publish notification bot
	m_bot.post()
	
	"""
	# post via incomming webhook
	m_bot.postWebhook()
	"""
	return 0

def main():
	''' main function 

	:rtype: int
	'''
	# get mattermost setting
	config = get_config()
	m_sg = MmShotgrid(config)

	# get shotgun instance
	sg = Shotgun(m_sg.url, script_name=m_sg.script_name, api_key=m_sg.api_key)
	fields = ['id', 'code', 'sg_asset_type']
	filters = [
		['project', 'is', {'type': 'Project', 'id': int(m_sg.project_id) } ],
		['sg_asset_type', 'is', 'Character']
	]
	asset_all = sg.find("Asset",filters,fields)
	print (asset_all)

	
	"""
	post_mattermost(config)
	"""
	return 0

if __name__ == "__main__":
	sys.exit(main())