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
	''' 
	Return the path of given file name

	:rtype: str
	'''
	return os.path.dirname(os.path.abspath(__file__))

def config_path():
	'''
	Return the file path of config.json.

	:rtype: str
	'''
	return os.path.join(base_dir(), "config", "config.yml")

def get_config():
	'''
	Read the data from config.yml and return it as dictionary

	:rtype: dict
	'''

	with open(config_path(), "r") as fp:
		config = yaml.safe_load(fp)
	return config

def post_mattermost(config):
	''' 
	Post to mattermost

	:rtype: int
	'''
	m_bot = MmBot(config)
	
	# set message to post
	message = "This is test!"
	m_bot.set_message(message)
	
	# post via publish notification bot
	m_bot.post()
	
	"""
	# Post via incomming webhook
	m_bot.postWebhook()
	"""
	return 0

def shotgrid_test(config):
	''' 
	Collect each shotgrid test function call 

	:rtype: int
	'''
	m_sg = MmShotgrid(config)

	"""
	#Create mattermost-shotgrid class
	
	# the function for getting asset list
	asset_list = m_sg.find_asset()
	print (asset_list)

	# get project id defined by project name
	project = m_sg.get_project("Linux_TK_Test")
	print (project["id"])
	"""
	# get all tasks assiged the artist
	tasks = m_sg.find_task_by_name(artist_name=m_sg.user_name,project_name=m_sg.project_name)
	for task in tasks :
		print (task["entity"],end="\n")
	
	
	return 0

def main():
	''' 
	Main function 

	:rtype: int
	'''
	# get mattermost and shotgrid config from yml file
	config = get_config()

	# Create mattermost-shotgrid class
	#m_sg = MmShotgrid(config)
	shotgrid_test(config)
	
	"""
	# the method to post mattermost
	post_mattermost(config)
	"""

	return 0

if __name__ == "__main__":
	sys.exit(main())