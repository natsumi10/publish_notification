#mm_shotgrid.py
from shotgun_api3 import Shotgun

class MmShotgrid:
	""" Base Bot class to post Mattermost.
		The Project ID should be listed in config.yml
	"""
	def __init__(self,config):
		sg_config = config["shotgrid"]
		self.url = sg_config["url"]
		self.script_name = sg_config["script_name"]
		self.api_key = sg_config["api_key"]
		self.user_name = sg_config["user_name"]
		self.project_id = sg_config["project_id"]
		self.project_name = sg_config["project_name"]
		self.sg = Shotgun(self.url, script_name=self.script_name, api_key=self.api_key)

	def find_asset(self):
		fields = ['id', 'code', 'sg_asset_type']
		filters = [
			['project', 'is', {'type': 'Project', 'id': int(self.project_id) } ],
			['sg_asset_type', 'is', 'Character']
		]
		asset_all = self.sg.find("Asset",filters,fields)
		
		return asset_all

	def get_project(self,project_name):
		"""Return the Project info including project id. 
		The project is defined from the project name.

		:rtype: dict
		"""
		return self.sg.find_one('Project',[['name', 'is',str(project_name)]])

	def find_task_by_name(self, artist_name, project_name):
		"""Return all tasks filtered by name. The list includes task id and entity.

		:rtype: list
		"""
		
		#get the project id
		project = self.get_project(project_name)

		fields = ['id', 'entity']
		filters = [
			['project', 'is', {'type': 'Project', 'id': int(project["id"]) } ],
			["task_assignees", "name_is", artist_name]
		]
		tasks = self.sg.find("Task",filters,fields)
		
		#print (tasks[0]["entity"],end="\n")
		return tasks
