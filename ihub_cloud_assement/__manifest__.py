# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'IHub Module Assessment',
    'version' : '16.0.1',
    'summary': 'This is a sample module for Ihub Assessment ',
    'sequence': -100,
    'category': 'Accounting/Accounting',
    'website': 'https://estainmakaudze.com',
    'depends': ['mail'],
    'data': [
    #security -- data -- views --reports
    'security/ir.model.access.csv',
    'data/data.xml',
    'views/growers_views.xml',
    'views/creditors_views.xml',
    'report/report_options.xml',
    'report/creditors_report.xml',
    'report/growers_report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

