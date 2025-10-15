# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import base64

# https://techspawn.com/docs/woocommerce-multi-locations-inventory-management/how-to-use-the-rest-api/
# 1. You need to autheticate each MultiLoca API request in exactly same way as we autheticate woocommerce API with the created client key & secret. The authentication method will be "Basic Auth" as shown in the attached screenshot.
# 2. To get a detailed understadnding of all our supported API's Please review our postman collection - https://documenter.getpostman.com/view/38446422/2sAXqs8NcX
class WCMLIMSettings(Document):
	@frappe.whitelist()
	def fetch_location_details(self, throw_if_missing=False):
		wcs_list=frappe.get_list("WooCommerce Server", filters={"enable_sync": 1, "enable_stock_level_synchronisation": 1})		
		if len(wcs_list)>0:
			for wc_server_row in wcs_list:
				wc_server=frappe.get_doc("WooCommerce Server", wc_server_row.name)
				url = wc_server.woocommerce_server_url+"/wp-json/wc/v3/locations"
				client_id = wc_server.api_consumer_key
				client_secret = wc_server.api_consumer_secret
				# encode client_id:client_secret
				basic_token = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

				headers = {
					"Authorization": f"Basic {basic_token}",
					"Content-Type": "application/x-www-form-urlencoded"
				}

				response = requests.get(
					url,
					data={},
					headers=headers
				)

				print(response.json())
				output=response.json()
				for row in output:
					print(row,"==",row.get("term_id"),row.get("name"))
					if row.get("term_id") and row.get("name"):
						if not frappe.db.exists("Wcmlim Location Detail", {"location_id": row.get("term_id")}):
							if frappe.db.exists("Warehouse", {"name": row.get("name")}):
								new_data_row = self.append('location_details', {})
								print(row.get("term_id"), row.get("name"))
								new_data_row.location_id =  row.get("term_id")
								new_data_row.location_name =  row.get("name")	
							else:
								msg_text=f"Warehouse {row.get('name')} not found. Its location ID is {row.get('term_id')}. \n Please create it first."
								self.add_comment('Comment', text=msg_text)
								frappe.msgprint(msg_text)
				self.save()