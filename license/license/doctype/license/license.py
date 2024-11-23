# Copyright (c) 2024, sanmugam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class License(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attachments: DF.Attach | None
		contact_details: DF.Data | None
		expiry_date: DF.Datetime
		issue_date: DF.Date
		issued_by: DF.Data
		license_count: DF.Int
		license_duration: DF.Literal["Monthly", "Quarterly", "Yearly"]
		license_fee: DF.Currency
		license_holder: DF.Data | None
		license_name: DF.Data
		license_number: DF.Data
		license_type: DF.Literal["Single", "Multiple"]
		payment_website: DF.Data | None
		renewal_date: DF.Date
		renewal_status: DF.Literal["Pending", "Renewed"]
		status: DF.Literal["Active", "Expired", "Suspended", "Revoked"]
		unused_cunt: DF.Int
		used_count: DF.Int
	# end: auto-generated types

	pass
