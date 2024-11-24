# Copyright (c) 2024, sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from license.utils import create_aws_client,get_ec2_details


class EC2Instance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		availabilityzone: DF.Data | None
		instanceid: DF.Data | None
		instancetype: DF.Data | None
		launchtime: DF.Datetime | None
		name: DF.Int | None
		privateip: DF.Data | None
		publicip: DF.Data | None
		state: DF.Data | None
	# end: auto-generated types

	
	def db_insert(self, *args, **kwargs):
		raise NotImplementedError

	def load_from_db(self):
		client=create_aws_client('ec2', aws_access_key, aws_secret_key, region)
		data_list=get_ec2_details(client)
		data = next((item for item in data_list if item["name"] == self.name), None)
		# 

		# client=get_uptime_kuma()
		# d=client.get_monitor(self.name)
		# st=client.get_monitor_status(d["id"])
		# frappe.errprint(st)
		# status = self.check_status(str(st))
		# status = "PAUSE" if status == "UP" and not d["active"] else status  # Retain current status if not paused
		# data={"name":d["id"],"uptime_kuma_name":d["name"],"id":d["name"],"url":d["url"],"host_name":d["hostname"],"status":status,"is_pause": 1 if not d["active"] else 0}
		super(Document, self).__init__(data)

		# raise NotImplementedError

	def db_update(self):
		raise NotImplementedError

	def delete(self):
		raise NotImplementedError

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
	
		client=create_aws_client('ec2', aws_access_key, aws_secret_key, region)
		data=get_ec2_details(client)
		frappe.errprint(data)
		return data


	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

