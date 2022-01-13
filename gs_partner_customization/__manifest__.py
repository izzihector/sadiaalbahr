# -*- coding: utf-8 -*-
{
    'name': "GS Partner Customization",

    'summary': """
        GS Partner Customization
        """,

    'description': """
        GS Partner Customization
    """,

    'author': "Global Solutions",
    'website': "https://GlobalSolutions.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
    'data': [
        'views/views.xml',
    ],
    "license": "Other proprietary",
}