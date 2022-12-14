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
		self.message = "This is test!"

	def set_message(self,message_text):
		self.message = message_text

	def post(self):
		# post message via matterrmost bot
		headers = {
			'Content-type': 'application/json',
			'Authorization': 'Bearer ' + self.bot_token,
		}

		data = {
			"channel_id": self.channel_id,
			"message": self.message,
			"username": "publish_notification",
		}
		response = requests.post(
			self.api_url,
			headers = headers,
			json = data
		)

	def postWebhook(self):
		headers = {"Content-type": "application/json"}

		data = {
			"text": self.message
		}
		response = requests.post(self.webhook_url, json=data, headers=headers)
		print("Status code: {0} {1}".format(response.status_code, response.reason))