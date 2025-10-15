import frappe
from frappe import _
import re

@frappe.whitelist()
def update_so_warehouse_based_on_loction_id(doc, method):
    for row in doc.get("items"):
        if row.get("custom_wcmlim_location_id") :
            custom_wcmlim_location_id=row.get("custom_wcmlim_location_id")
            if custom_wcmlim_location_id!='':
                 location_name=frappe.db.get_value('Wcmlim Location Detail', {'location_id': custom_wcmlim_location_id}, ['location_name'])
                 if location_name:
                     row.warehouse=location_name

@frappe.whitelist()
def add_saudi_arabia_postal_code(doc, method):
    if doc.country == "Saudi Arabia" and not doc.pincode:
        doc.pincode = "12211"


def update_so_mode_of_payment_based_on_payment_id(doc, method):
    woocommerce_payment_method=doc.get("woocommerce_payment_method")
    if woocommerce_payment_method!='':
            mode_of_payment=frappe.db.get_value('WC Payment Detail', {'wc_title':_(woocommerce_payment_method)}, ['mode_of_payment'])
            if mode_of_payment:
                 doc.custom_wc_mode_of_payment=mode_of_payment

def update_customer_based_on_mobile_no(doc, method):
    if doc.doctype == "Customer":
        if doc.mobile_no and not doc.custom_customer_phone_no:
            doc.custom_customer_phone_no = doc.mobile_no
    elif doc.doctype == "Sales Order":
        if doc.customer and doc.customer!='':
            customer_details=frappe.db.get_value('Customer', {'name': doc.customer}, ["mobile_no",'custom_customer_phone_no'], as_dict=1)
            if customer_details and customer_details.get("mobile_no") and not customer_details.get("custom_customer_phone_no"):
                frappe.db.set_value('Customer', doc.customer, 'custom_customer_phone_no', customer_details.get("mobile_no"))

def update_si_mode_of_payment_based_on_so_wc(doc, method):
     for row in doc.get("items"):
        if row.get("sales_order"):
            so_wc=row.get("sales_order")
            if so_wc!='':
                 wc_details=frappe.db.get_value('Sales Order', {'name': so_wc}, ['custom_wc_mode_of_payment','grand_total'], as_dict=1)
                 if wc_details:
                    doc.payments=[]
                    new_data_row = doc.append('payments', {})
                    new_data_row.mode_of_payment =  wc_details.get("custom_wc_mode_of_payment")
                    new_data_row.amount =  wc_details.get("grand_total")
                    break                 
                 


def remove_text_in_brackets(text):
  """Removes parentheses and any text inside them from a string."""
  # The pattern \(.*?\) finds an opening parenthesis,
  # followed by any character (non-greedily),
  # and then a closing parenthesis.
  return re.sub(r'\(.*?\)', '', text)

# # --- Examples ---

# # 1. Parentheses at the end (your original string)
# str1 = "الدفع نقدًا عند الإستلام(المتجر)"
# print(f"Original: {str1}")
# print(f"Cleaned: {remove_text_in_brackets(str1)}\n")

# # 2. Parentheses at the beginning
# str2 = "(المتجر)الدفع نقدًا عند الإستلام"
# print(f"Original: {str2}")
# print(f"Cleaned: {remove_text_in_brackets(str2)}\n")

# # 3. Parentheses in the middle
# str3 = "الدفع (المتجر) نقدًا عند الإستلام"
# print(f"Original: {str3}")
# print(f"Cleaned: {remove_text_in_brackets(str3)}\n")

# # 4. Multiple sets of parentheses
# str4 = "الدفع (المتجر) نقدًا (كاش) عند الإستلام"
# print(f"Original: {str4}")
# print(f"Cleaned: {remove_text_in_brackets(str4)}\n")                 