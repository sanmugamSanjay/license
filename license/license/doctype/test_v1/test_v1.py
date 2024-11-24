# Copyright (c) 2024, sanmugam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from license.utils import get_uptime_kuma
from frappe import _
from uptime_kuma_api import UptimeKumaApi, MonitorType

# def get_uptime_kuma():
#     # api_key=frappe.conf.get("uptime_key")
#     client = UptimeKumaApi('http://192.168.2.49:3001/')
#     client.login('velavan', 'Aalam@123')
#     return client


class TestV1(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		host_name: DF.Data
		id: DF.Data | None
		status: DF.Literal["Active", "InActive"]
		uptime_name: DF.Data | None
		url: DF.Data
	# end: auto-generated types

	
	def db_insert(self, *args, **kwargs):
		client=get_uptime_kuma()
		d=client.add_monitor(type=MonitorType.HTTP,name=self.uptime_name,url=self.url,hostname=self.host_name)
		# api.add_monitor(type=MonitorType.HTTP, name="Google", url="https://google.com",hostname="https://google.com")
		frappe.errprint(d)

	def load_from_db(self):
		client=get_uptime_kuma()
		d=client.get_monitor(self.name)
		st=client.get_monitor_status(d["id"])
		frappe.errprint(st)
		data={"name":d["id"],"uptime_name":d["name"],"host_name":d["hostname"],"url":d["url"],"status":self.check_status(str(st))}
		super(Document, self).__init__(data)
		# raise NotImplementedError
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
		# status = client.get_monitor_status(d["id"])
		# frappe.errprint(data)
		return [ frappe._dict({"name":d["id"],"uptime_name":d["name"],"url":d["url"],"host_name":d["hostname"],"status":"UP" if str(client.get_monitor_status(d["id"])) == "MonitorStatus.UP" else "DOWN"}) for d in data]

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

