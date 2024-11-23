import frappe
from uptime_kuma_api import UptimeKumaApi, MonitorType

def get_uptime_kuma():
    # api_key=frappe.conf.get("uptime_key")
    client = UptimeKumaApi('http://192.168.2.49:3001/')
    client.login('velavan', 'Aalam@123')
    return client