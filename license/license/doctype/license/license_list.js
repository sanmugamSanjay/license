
function ButtonFunction(listview) {
    window.open('http://nov-aalam.hack:8002/license-list','_blank')
}

frappe.listview_settings['License'] = {
   refresh: function(listview) {
       listview.page.add_inner_button("Custom View", function() {
           ButtonFunction(listview);
       });;
   },
};