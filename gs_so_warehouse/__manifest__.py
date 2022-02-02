# -*- encoding: utf-8 -*-
{
    'name': "gs_so_warehouse",
    'version': '1.1',
    'category': 'Tools',
    'summary': """""",
    'description': """""",
    'author': '',
    'website': '',
    'depends': ['base', 'stock', 'sale', 'sale_stock'],
    'data': [
        'views/sale_order_inherit.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'price': 19.99,
    'currency': 'EUR',
}