# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Sales BSS",
			"category": "Modules",
			"label": _("Sales BSS"),
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module",
			"description": "Lead, Opportunity, Quotation, Sales Order, Sales Invoice and Payment Entry."
		},
	]
