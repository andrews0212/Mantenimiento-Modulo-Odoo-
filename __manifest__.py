# -*- coding: utf-8 -*-
{
    'name': "gestión_mantenimiento",

    'summary': """
        Módulo para la gestión de órdenes de mantenimiento y equipos""",

    'description': """
        Este módulo permite gestionar órdenes de mantenimiento, equipos, categorías y proveedores.
        Incluye vistas de lista y formulario para cada modelo, así como menús y controles de acceso.
    """,

    'author': "Andrews Dos Ramos",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Maintenance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/orden_views.xml',
        'views/equipo_views.xml',
        'views/categoria_views.xml',
        'views/proveedor_views.xml',
        'views/menu_views.xml',
        'views/mantenimiento_articulo_views.xml',
        'views/mantenimiento_reparacion_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
