// Copyright (c) 2024, sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("License", {
	refresh(frm) {
        if(frm.doc.payment_website){
            frm.sidebar.add_user_action("Payment website",()=>{
                window.open(frm.doc.payment_website,'_blank')
            })
        }
	},
});
