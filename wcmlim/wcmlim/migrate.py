from __future__ import unicode_literals

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_migrate():
    custom_fields = {
        "Sales Order Item": [
            dict(
                fieldname="custom_wcmlim_location_id",
                label="wcmlim_location_id",
                fieldtype="Data",
                insert_after="warehouse",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
                read_only=1,

            ),
        ]        
    }
    print("Creating custom fields for app wcmlim")
    for dt, fields in custom_fields.items():
        print("*******\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)