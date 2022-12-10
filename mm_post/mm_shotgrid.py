#mm_shotgrid.py



class MmShotgrid:
	""" Base Bot class to post Mattermost.
	"""
	def __init__(self,config):
		sg_config = config["shotgrid"]
		self.url = sg_config["url"]
		self.script_name = sg_config["script_name"]
		self.api_key = sg_config["api_key"]