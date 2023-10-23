# -*- coding: utf-8 -*-
{
    'name': "Legislativa",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Apache",
    'website': "https://www.apachedigital.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.8',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/grupos_parlamentarios.xml',
        'data/instituciones.xml',
        'data/ir_cron.xml',
        'views/grupo_parlamentario_views.xml',
        'views/diputados_views.xml',
        'views/iniciativas_views.xml',
        'views/instituciones_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
