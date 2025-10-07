# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import base64
from woocommerce_fusion.tasks.utils import APIWithRequestLogging
from wcmlim.api import remove_text_in_brackets

verify_ssl = not frappe._dev_server

class WCPaymentSettings(Document):
	@frappe.whitelist()
	def fetch_payment_details(self, throw_if_missing=False):
		print('='*10)
		wc_servers = frappe.get_all("WooCommerce Server")
		wc_servers = [frappe.get_doc("WooCommerce Server", server.name) for server in wc_servers]
		for server in wc_servers:
			if server.enable_sync == 1:
				wc_api = APIWithRequestLogging(
					url=server.woocommerce_server_url,
					consumer_key=server.api_consumer_key,
					consumer_secret=server.api_consumer_secret,
					version="wc/v3",
					timeout=40,
					verify_ssl=verify_ssl,
				)				
				try:
					endpoint = f"payment_gateways"
					response=wc_api.get("payment_gateways").json()
					for row in response:
						print(row,"==",row.get("id"),row.get("method_title"))
						if row.get("id") and row.get("method_title"):
							if not frappe.db.exists("WC Payment Detail", {"wc_id": row.get("id")}):
								new_data_row = self.append('wc_payment_details', {})
								new_data_row.wc_id =  row.get("id")
								if row.get("id")=="cod":
									new_data_row.wc_title = remove_text_in_brackets(row.get("title"))
								new_data_row.wc_title =  row.get("title") 
								new_data_row.wc_payment_method_title =  row.get("method_title")	
							self.save()

				except Exception as err:
					error_message = f"{frappe.get_traceback()}"
					frappe.log_error("WooCommerce Error", error_message)
					raise err