#mm_bot.py

import requests

class MmBot:
	""" Base Bot class to post Mattermost.
	"""
	def __init__(self,config):
		mm_config = config["mattermost"]
		self.webhook_url = mm_config["webhook_url"]
		self.api_url = mm_config["mm_api_url"]
		self.bot_token = mm_config["bot_token"]
		self.channel_id = mm_config["channel_id"]

	def post(self):
		headers = {
			'Content-type': 'application/json',
			'Authorization': 'Bearer ' + self.bot_token,
		}

		data = {
			"channel_id": self.channel_id,
			"message": "This is a message from the bot",
			"username": "publish_notification",
		}
		response = requests.post(
			self.api_url,
			headers = headers,
			json = data
		)
