# -*- coding: utf-8 -*-
{
    'name': "Warehouse Restrictions Users",

    'summary': """
         Warehouse and Stock Location Restriction on Users.""",

    'description': """
        This Module Restricts the User from Accessing Warehouse and Process Stock Moves other than allowed to Warehouses and Stock Locations.
    """,

    'author': "Pixa-Grama",
    'website': "http://www.pixagrama.com",

    'category': 'Warehouse',
    'version': '0.1',

    'depends': ['base', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/users_view.xml',
    ],
}