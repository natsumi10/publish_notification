#mm_shotgrid.py
from shotgun_api3 import Shotgun

class MmShotgrid:
	""" Base Bot class to post Mattermost.
	"""
	def __init__(self,config):
		sg_config = config["shotgrid"]
		self.url = sg_config["url"]
		self.script_name = sg_config["script_name"]
		self.api_key = sg_config["api_key"]
		self.user_name = sg_config["user_name"]
		self.project_id = sg_config["project_id"]
		self.sg = Shotgun(self.url, script_name=self.script_name, api_key=self.api_key)

	def find_asset(self):
		#self.sg = Shotgun(self.url, script_name=self.script_name, api_key=self.api_key)
		fields = ['id', 'code', 'sg_asset_type']
		filters = [
			['project', 'is', {'type': 'Project', 'id': int(self.project_id) } ],
			['sg_asset_type', 'is', 'Character']
		]
		asset_all = self.sg.find("Asset",filters,fields)
		
		return asset_all