# -*- coding: utf-8 -*-
{
    'name': "Mi primer modulo de odoo ",
    'summary':"""
        Prueba de funcionalidades de odoo
    """,
    'author':'Gustavo Sied',
    'category':'General',
    'version':'1.0.0',
    'depends':[],
    'data':[
        'views/menu_view.xml',
        'views/libros_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv'
    ],
}