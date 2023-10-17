# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'pos customer',
    'auther': 'kordy',
    'depends': ['base', 'point_of_sale'],
    'installable': True,
    'license': 'LGPL-3',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/partner_gender.xml',
        'views/customer_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            "pos_customer/static/src/js/pos.js",
            "pos_customer/static/src/js/load_fields.js",
            "pos_customer/static/src/xml/cleint_pos.xml",
            "pos_customer/static/src/xml/Partneredit.xml",
        ],
    },
    'application': True,
    'auto_install': False,
}
