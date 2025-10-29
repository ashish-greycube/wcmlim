frappe.ui.form.on("Sales Invoice", {
    refresh: function (frm) {
        setTimeout(() => {
            if (frm.is_new() && frm.doc.customer && !frm.doc.custom__customer_mobil_no) {
                frappe.db.get_value('Customer', frm.doc.customer, 'custom_customer_phone_no')
                    .then(r => {
                        // console.log(r.message.custom_customer_phone_no, "---------")
                        frm.set_value('custom__customer_mobil_no', r.message.custom_customer_phone_no);
                    })
            }
        }, 1000);
    }
})