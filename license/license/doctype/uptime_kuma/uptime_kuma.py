# Copyright (c) 2024, sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from license.utils import get_uptime_kuma
from frappe import _
from uptime_kuma_api import UptimeKumaApi, MonitorType



class UptimeKuma(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		host_name: DF.Data | None
		id: DF.Data | None
		is_pause: DF.Check
		status: DF.Data | None
		uptime_kuma_name: DF.Data | None
		url: DF.Data | None
	# end: auto-generated types

	
	def db_insert(self, *args, **kwargs):
		client=get_uptime_kuma()
		d=client.add_monitor(type=MonitorType.HTTP,name=self.name,url=self.url,hostname=self.host_name)

	def load_from_db(self):
		client=get_uptime_kuma()
		d=client.get_monitor(self.name)
		st=client.get_monitor_status(d["id"])
		frappe.errprint(st)
		status = self.check_status(str(st))
		status = "PAUSE" if status == "UP" and not d["active"] else status  # Retain current status if not paused
		data={"name":d["id"],"uptime_kuma_name":d["name"],"id":d["name"],"url":d["url"],"host_name":d["hostname"],"status":status,"is_pause": 1 if not d["active"] else 0}
		super(Document, self).__init__(data)
	def check_status(self,d):
		return "UP" if d == "MonitorStatus.UP" else "DOWN"

	def db_update(self):
		raise NotImplementedError

	def delete(self):
		raise NotImplementedError

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		client=get_uptime_kuma()
		data=client.get_monitors()
		frappe.errprint(data)
		# list_data=[ frappe._dict({"id":d["name"],"uptime_kuma_name":d["name"],"name":d["id"],"url":d["url"],"host_name":d["hostname"],"status":"UP" if str(client.get_monitor_status(d["id"])) == "MonitorStatus.UP" else "DOWN","is_pause": 0 if d["active"] else 1}) for d in data]
		# list_data=[ frappe._dict({"id":d["name"],"uptime_kuma_name":d["name"],"name":d["id"],"url":d["url"],"host_name":d["hostname"],"status":"UP" if str(client.get_monitor_status(d["id"])) == "MonitorStatus.UP" else "DOWN","is_pause": 0 if d["active"] else 1}) for d in data]
		output_data = []
		for item in data:
			status = "UP" if str(client.get_monitor_status(item["id"])) == "MonitorStatus.UP" else "DOWN"
			status = "PAUSE" if status == "UP" and not item["active"] else status  # Retain current status if not paused
			is_pause = 1 if not item["active"] else 0
			output_data.append({
				"id": item["name"],
				"uptime_kuma_name": item["name"],
				"name": item["id"],
				"url": item["url"],
				"host_name": item["hostname"],
				"status": status,
				"is_pause": is_pause
			})
		return output_data

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

def check_status_out(d,flag):
		return "UP" if str(client.get_monitor_status(d["id"])) == "MonitorStatus.UP" else "PAUSE" if str(client.get_monitor_status(d["id"])) == "MonitorStatus.UP" or not d["active"] else "DOWN"

@frappe.whitelist()
def pause_monitor(id):
	clinet=get_uptime_kuma()
	clinet.pause_monitor(id)
	return 1

@frappe.whitelist()
def unpause_monitor(id):
	clinet=get_uptime_kuma()
	clinet.resume_monitor(id)
	return 1
	
