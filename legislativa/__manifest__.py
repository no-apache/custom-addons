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
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/tipo_institucion.xml',
        'data/actores.xml',
        'data/entidad_persona.xml',
        'data/tipo_mapa.xml',
        'views/entidad_persona_views.xml',
        'views/mapas_views.xml',
        'views/actores_alianzas_views.xml',
        'views/peticiones_actores_views.xml',
        'views/acciones_alianzas_views.xml',
        'views/comunicacion_views.xml',
        'views/influencia_digital_views.xml',
        'views/tipos_mapas_views.xml',
        'views/iniciativas_views.xml',
        'views/actores_views.xml',
        'views/areas_views.xml',
        'views/desempeno_views.xml',
        'views/resultado_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'legislativa/static/src/components/**/*',
            'legislativa/static/src/js/legacy_section_and_note_fields_backend.js',
            'legislativa/static/src/js/custom_width_tree.js',
            'legislativa/static/src/js/main.js',
            'legislativa/static/src/xml/*.xml',
        ]
    }
}
