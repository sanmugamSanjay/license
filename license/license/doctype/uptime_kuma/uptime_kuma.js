// Copyright (c) 2024, sanmugam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Uptime Kuma", {
	refresh(frm) {
        if(frm.doc.status === "UP" && !frm.doc.is_pause){
            frm.add_custom_button("Pause",()=>{
                frappe.call({
                    method: "license.license.doctype.uptime_kuma.uptime_kuma.pause_monitor",
                    args: {
                        id: frm.doc.name
                    },
                    callback: function(response) {
                        if (response.message) {
                            if(response.message ){
                                frm.reload_doc()
                                frappe.msgprint(`Monitor Paused Succesfully`);
                            }
                        } else {
                            frappe.msgprint("Something Went Wrong.");
                        }
                    }
                });
            })
        }else if (frm.doc.status === "PAUSE" && frm.doc.is_pause){
            frm.add_custom_button("Un Pause",()=>{
                frappe.call({
                    method: "license.license.doctype.uptime_kuma.uptime_kuma.unpause_monitor",
                    args: {
                        id: frm.doc.name
                    },
                    callback: function(response) {
                        if (response.message) {
                            if(response.message ){
                                frm.reload_doc()
                                frappe.msgprint(`Monitor Resumed Succesfully`);
                            }
                        } else {
                            frappe.msgprint("Something Went Wrong.");
                        }
                    }
                });
            })

        }
	},
});
