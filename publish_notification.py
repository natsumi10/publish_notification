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

def shotgrid_test(config):
	''' collect each shotgrid test function call 

	:rtype: int
	'''

	"""
	#Create mattermost-shotgrid class
	m_sg = MmShotgrid(config)
	# the function for getting asset list
	asset_list = m_sg.find_asset()
	print (asset_list)

	# get project id defined by project name
	project = m_sg.get_project("Linux_TK_Test")
	print (project["id"])
	"""
	return 0

def main():
	''' main function 

	:rtype: int
	'''
	# get mattermost and shotgrid config from yml file
	config = get_config()

	# Create mattermost-shotgrid class
	m_sg = MmShotgrid(config)
	sg = Shotgun(m_sg.url, script_name=m_sg.script_name, api_key=m_sg.api_key)
	fields = ['id','task_assignees']
	filters = [
		['project', 'is', {'type': 'Project', 'id': int(m_sg.project_id) } ],
		["task_assignees", "is_not", None]
	]
	task = sg.find("Task",filters,fields)
	print (task)

	"""
	# the method to post mattermost
	post_mattermost(config)
	"""

	return 0

if __name__ == "__main__":
	sys.exit(main())