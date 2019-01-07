# -*- coding: utf-8 -*-
{
    'name': "DRS Odoo Module",

    'summary': """ Used to modify odoo to better suit the needs of the company""",

    'description': """
    """,

    'author': "Leke Onile-ere",
    'website': "http://www.drs.network",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'purchase', 'account_invoicing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/drs_product_view.xml',
        'views/drs_company_view.xml',
        'views/drs_reference_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}