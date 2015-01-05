"""
Python Library for Softaculous API

	https://www.softaculous.com/docs/API

Author: Benton Snyder
Website: http://bensnyde.me
Created: 1/4/15

"""
import logging
import base64
import httplib
import json
import socket

class Softaculous:
	def __init__(self, softaculous_base_url, softaculous_username, softaculous_password):
		"""Constructor
		Paremeters
			softaculous_base_url: str base url of softaculous (ex. whm.example.com)
			softaculous_username: str softaculous username
			softaculous_password: str softaculous password
		Returns
			None
		"""
		self.base_url = softaculous_base_url
		self.username = softaculous_username
		self.password = softaculous_password

	def __softaculous_api_query(self, **kwargs):
		"""Query Softaculous API

		Parameters
			kwargs:
		Returns:
			json response from server
		"""
        try:
            conn = httplib.HTTPSConnection(self.base_url)
            conn.request('GET', queryStr, headers={'Authorization':'Basic ' + base64.b64encode(self.whm_username+':'+self.whm_password).decode('ascii')})
            response = conn.getresponse()
            data = json.loads(response.read())
            conn.close()

            return data
        # Log errors
        except httplib.HTTPException as ex:
            logging.critical("HTTPException from CpanelFTP API: %s" % ex)
        except socket.error as ex:
            logging.critical("Socket.error connecting to CpanelFTP API: %s" % ex)
        except ValueError as ex:
            logging.critical("ValueError decoding CpanelFTP API response string: %s" % ex)
        except Exception as ex:
            logging.critical("Unhandled Exception while querying CpanelFTP API: %s" % ex)
		return True

	def list_scripts(self):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data {
			"act": None
		}

		return self.__softaculous_api_query(data)

	def install_script(self, script_id, **kwargs):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "software",
			"soft": script_id,
		}

		return self.__softaculous_api_query(data)

	def upgrade_script(self, installation_id):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "upgrade",
			"insid": installation_id,
		}

		return self.__softaculous_api_query(data)

	def remove_script(self, installation_id):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "remove",
			"insid": installation_id,
		}

		return self.__softaculous_api_query(data)

	def import_installation(self, script_id):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "import",
			"soft": script_id,
		}

		return self.__softaculous_api_query(data)

	def list_installed_scripts(self, show_only_installations_with_updates_available = False):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "installations",
			"showupdates": show_only_installations_with_updates_available,
		}

		return self.__softaculous_api_query(data)

	def list_backups(self):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "backups"
		}

		return self.__softaculous_api_query(data)

	def backup_installed_script(self, installation_id):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "backup",
			"insid": installation_id,
		}

		return self.__softaculous_api_query(data)

	def restore_installed_script(self, back_file_name):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "restore",
			"restore": backup_filename
		}

		return self.__softaculous_api_query(data)

	def download_backups(self, backup_filename):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "backups",
			"download": backup_filename,
		}

		return self.__softaculous_api_query(data)

	def delete_backup(self, backup_filename):
		"""List Scripts

			https://www.softaculous.com/docs/API#List_Scripts
		Parameters
			None
		Returns
			json dictionary:
				iscripts: [] of installed scripts
		"""
		data = {
			"act": "backups",
			"remove": backup_filename,
		}

		return self.__softaculous_api_query(data)
