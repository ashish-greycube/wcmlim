import frappe

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