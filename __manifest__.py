# -*- coding: utf-8 -*-
{
    'name': "GESRE",

    'summary': """
        Modulo que Gestiona las Reparaciones del Hogar""",

    'description': """
       Modulo de Gestion de Clientes, Piezas, Trbajadores e Incidencias, en el 
       que todos los modulos hacen un CRUD(Create Read Update Delete) completo
    """,

    'author': "GESRE",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/gesre.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}