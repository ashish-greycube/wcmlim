app_name = "wcmlim"
app_title = "Wcmlim"
app_publisher = "GreyCube Technologies"
app_description = "Customization for Woocommerce Multilocations Invnetory Management"
app_email = "admin@greycube.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "wcmlim",
# 		"logo": "/assets/wcmlim/logo.png",
# 		"title": "Wcmlim",
# 		"route": "/wcmlim",
# 		"has_permission": "wcmlim.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wcmlim/css/wcmlim.css"
# app_include_js = "/assets/wcmlim/js/wcmlim.js"

# include js, css files in header of web template
# web_include_css = "/assets/wcmlim/css/wcmlim.css"
# web_include_js = "/assets/wcmlim/js/wcmlim.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wcmlim/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "wcmlim/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "wcmlim.utils.jinja_methods",
# 	"filters": "wcmlim.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wcmlim.install.before_install"
# after_install = "wcmlim.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wcmlim.uninstall.before_uninstall"
# after_uninstall = "wcmlim.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument
after_migrate = "wcmlim.migrate.after_migrate"
# before_app_install = "wcmlim.utils.before_app_install"
# after_app_install = "wcmlim.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wcmlim.utils.before_app_uninstall"
# after_app_uninstall = "wcmlim.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wcmlim.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"before_insert": ["wcmlim.api.update_so_warehouse_based_on_loction_id","wcmlim.api.update_so_mode_of_payment_based_on_payment_id"],
	},
	"Sales Invoice": {
		"before_insert": ["wcmlim.api.update_si_mode_of_payment_based_on_so_wc"],
	},    
	"Address": {
		"before_validate": "wcmlim.api.add_saudi_arabia_postal_code",
	},
	"Customer": {
		"before_insert": ["wcmlim.api.update_customer_based_on_mobile_no"],
	}	    
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wcmlim.tasks.all"
# 	],
# 	"daily": [
# 		"wcmlim.tasks.daily"
# 	],
# 	"hourly": [
# 		"wcmlim.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wcmlim.tasks.weekly"
# 	],
# 	"monthly": [
# 		"wcmlim.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "wcmlim.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wcmlim.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wcmlim.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wcmlim.utils.before_request"]
# after_request = ["wcmlim.utils.after_request"]

# Job Events
# ----------
# before_job = ["wcmlim.utils.before_job"]
# after_job = ["wcmlim.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"wcmlim.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

