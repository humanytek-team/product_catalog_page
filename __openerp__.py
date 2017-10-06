# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Add field "Catalog Page" to products.',
    'version': '9.0.0.1.0',
    'category': 'Product',
    'summary': 'Adds field "Catalog Page" to products.',
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': ['product', ],
    'data': [
        'views/product_view.xml',        
    ],
    'installable': True,
    'auto_install': False
}
