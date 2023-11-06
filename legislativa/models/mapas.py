# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mapas(models.Model):
    _name = 'legislativa.mapas'

    name = fields.Char(compute="_compute_name", string='Nombre')
    mapa_name = fields.Selection([
        ('mdaa', 'Mapa de Actores y Alianzas'),
        ('mpda', 'Mapa de Peticiones de Actores'),
        ('mada', 'Mapa de Acciones de Alianzas'),
        ('mdco', 'Mapa de Comunicación'),
        ('mdid', 'Mapa de Influencia Digital')],
        string='Seleccione:', required=True)
    descripcion = fields.Text(string='Descripción')
    mapas_ids = fields.One2many(
        comodel_name='legislativa.tipos_mapas',
        inverse_name='tipo_mapas_id',
        string='Mapas')

    @api.depends('mapa_name')
    def _compute_name(self):
        for record in self:
            record.name = dict(self._fields['mapa_name'].selection).get(
                record.mapa_name)


class TiposMapas(models.Model):
    _name = 'legislativa.tipos_mapas'

    VALUE = [('1', '1'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'),
             ('5', '5'),
             ('6', '6'),
             ('7', '7')]

    VALUE_SN_KPI = [('0', 'No'),
                    ('1', 'Sí')]

    VALUE_NF_KPI = [('0', 'No'),
                    ('fe', 'Sí, Formales externos'),
                    ('fi', 'Sí, Formales internos'),
                    ('ie', 'Sí, Informales externos'),
                    ('ii', 'Sí, Informales internos')]

    VALUE_FI_KPI = [('0', 'No'),
                    ('f', 'Sí, Formales'),
                    ('i', 'Sí, Informales')]

    name = fields.Char(string='Comentarios')
    actor_id = fields.Many2one(
        comodel_name='legislativa.actores',
        string='Actores')
    entidad_id = fields.Many2one(
        comodel_name='legislativa.entidad_persona',
        string='Entidad')
    persona_id = fields.Many2one(
        comodel_name='legislativa.entidad_persona',
        string='Persona')
    escanios = fields.Integer(
        related='entidad_id.escanios', string='Escaños')
    porcentaje = fields.Float(
        related='entidad_id.porcentaje', string='Porcentaje')
    relevancia = fields.Selection(VALUE, 'Relevancia (1-7)')
    alineamiento = fields.Selection(VALUE, 'Alineamiento (1-7)')
    activable = fields.Selection(VALUE, 'Activable (1-7)')
    ponderacion_rel = fields.Float(
        compute='_compute_ponderacion_rel', string='Ponderación Relativa', digits=(2, 9))
    ponderacion_inst = fields.Selection(VALUE, 'Ponderación Instititucional')
    ponderacion_fin = fields.Float(
        compute='_compute_ponderacion_fin', string='Ponderación Final', digits=(2, 9))
    display_type = fields.Selection(
        selection=[
            ('line_section', "Section"),
            ('line_note', "Note"),
        ],
        default=False)
    tipo_mapas_id = fields.Many2one(
        comodel_name='legislativa.mapas',
        string='Mapa')

    peticiones = fields.Char(string='Peticiones')
    percent = fields.Float(string='Porcentaje')

    #
    # Campos para KPI Mapa de Actores y Alianzas
    #
    # Peso plan relacional. Actores
    planificados_actores = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de alianzas - Actores'
    )
    realizados_actores = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de alianzas - Actores'
    )
    alineados_actores = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de alianzas - Actores'
    )
    # Peso plan de alianzas. Aliados
    planificados_aliados = fields.Selection(
        VALUE_NF_KPI,
        string='Planificados',
        help='Planificados. Peso plan de alianzas - Aliados'
    )
    realizados_aliados = fields.Selection(
        VALUE_NF_KPI,
        string='Realizados',
        help='Realizados. Peso plan de alianzas - Aliados'
    )
    alineados_aliados = fields.Selection(
        VALUE_NF_KPI,
        string='Alineados',
        help='Alineados. Peso plan de alianzas - Aliados'
    )
    # Peso plan de alianzas. Alianzas
    planificados_alianzas = fields.Selection(
        VALUE_FI_KPI,
        string='Planificados',
        help='Planificados. Peso plan de alianzas - Alianzas'
    )
    realizados_alianzas = fields.Selection(
        VALUE_FI_KPI,
        string='Realizados',
        help='Realizados. Peso plan de alianzas - Alianzas'
    )
    alineados_alianzas = fields.Selection(
        VALUE_FI_KPI,
        string='Alineados',
        help='Alineados. Peso plan de alianzas - Alianzas'
    )

    #
    # Campos para KPI Mapa de Peticiones de Actores
    #
    # Peso plan relacional. Peticiones
    planificados_peticiones = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan relacional - Peticiones'
    )
    realizados_peticiones = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan relacional - Peticiones'
    )
    aceptadas_peticiones = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Peso plan relacional - Peticiones'
    )

    #
    # Campos para KPI Mapa de Acciones de Alianzas
    #
    # Mención expresa de mi marca en la alianza
    plan_mencion_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Mención expresa de mi marca en la alianza'
    )
    real_mencion_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Mención expresa de mi marca en la alianza'
    )
    acep_mencion_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Mención expresa de mi marca en la alianza'
    )
    # Mención expresa de mi marca en el posicionamiento de la alianza
    plan_posic_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Mención expresa de mi marca en el posicionamiento de la alianza'
    )
    real_posic_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Mención expresa de mi marca en el posicionamiento de la alianza'
    )
    acep_posic_marca = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Mención expresa de mi marca en el posicionamiento de la alianza'
    )
    # Participación en la actividad de la alianza
    plan_part_alianza = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Participación en la actividad de la alianza'
    )
    real_part_alianza = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Participación en la actividad de la alianza'
    )
    acep_part_alianza = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Participación en la actividad de la alianza'
    )
    # Participación en el posicionaiento de la alianza
    plan_part_posi = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Participación en el posicionaiento de la alianza'
    )
    real_part_posi = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Participación en el posicionaiento de la alianza'
    )
    acep_part_posi = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Participación en el posicionaiento de la alianza'
    )
    # Aliados con el posicionamiento de mi marca
    plan_aliados_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Aliados con el posicionamiento de mi marca'
    )
    real_aliados_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Aliados con el posicionamiento de mi marca'
    )
    acep_aliados_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Aliados con el posicionamiento de mi marca'
    )
    # Impulsor del posicionamiento de la alianza
    plan_impul_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Impulsor del posicionamiento de la alianza'
    )
    real_impul_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Impulsor del posicionamiento de la alianza'
    )
    acep_impul_posic = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Impulsor del posicionamiento de la alianza'
    )
    # Impulsor de las acciones a desarrollar en la alianza
    plan_impul_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Impulsor de las acciones a desarrollar en la alianza'
    )
    real_impul_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Impulsor de las acciones a desarrollar en la alianza'
    )
    acep_impul_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Impulsor de las acciones a desarrollar en la alianza'
    )
    # Portavoz o decisor de la alianza
    plan_decisor_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Portavoz o decisor de la alianza '
    )
    real_decisor_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Portavoz o decisor de la alianza '
    )
    acep_decisor_acciones = fields.Selection(
        VALUE_SN_KPI,
        string='Aceptadas',
        help='Aceptadas. Portavoz o decisor de la alianza '
    )

    #
    # Campos para KPI Mapa de Comunicación
    #
    # Peso plan relacional. Periodistas
    plan_plan_relacional = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan relacional. Periodistas'
    )
    real_plan_relacional = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan relacional. Periodistas'
    )
    alin_plan_relacional = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan relacional. Periodistas'
    )
    # Peso plan de comunicación. Medios
    plan_plan_comunic = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de comunicación. Medios'
    )
    real_plan_comunic = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de comunicación. Medios'
    )
    alin_plan_comunic = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de comunicación. Medios'
    )
    # Peso plan de comunicación. Periodistas y Medios
    plan_comunic_pm = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de comunicación. Periodistas y Medios'
    )
    real_comunic_pm = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de comunicación. Periodistas y Medios'
    )
    alin_comunic_pm = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de comunicación. Periodistas y Medios'
    )

    #
    # Campos para KPI Mapa de Influencia Digital
    #
    # Peso plan de influencia digital. Influencers
    plan_plan_influencers = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de influencia digital. Influencers'
    )
    real_plan_influencers = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de influencia digital. Influencers'
    )
    alin_plan_influencers = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de influencia digital. Influencers'
    )
    # Peso plan de influencia digital. Medios online
    plan_plan_medon = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de influencia digital. Medios online'
    )
    real_plan_medon = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de influencia digital. Medios online'
    )
    alin_plan_medon = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de influencia digital. Medios online'
    )
    # Peso plan de comunicación. Influencers + Medios On-Line
    plan_comunic_imo = fields.Selection(
        VALUE_SN_KPI,
        string='Planificados',
        help='Planificados. Peso plan de comunicación. Influencers + Medios On-Line'
    )
    real_comunic_imo = fields.Selection(
        VALUE_SN_KPI,
        string='Realizados',
        help='Realizados. Peso plan de comunicación. Influencers + Medios On-Line'
    )
    alin_comunic_imo = fields.Selection(
        VALUE_SN_KPI,
        string='Alineados',
        help='Alineados. Peso plan de comunicación. Influencers + Medios On-Line'
    )

    @api.depends('relevancia', 'alineamiento', 'activable')
    def _compute_ponderacion_rel(self):
        for record in self:
            record.ponderacion_rel = (
                int(record.relevancia) + int(record.alineamiento) + int(record.activable)) / 3

    @api.depends('ponderacion_rel', 'ponderacion_inst')
    def _compute_ponderacion_fin(self):
        for record in self:
            record.ponderacion_fin = (
                record.ponderacion_rel + int(record.ponderacion_inst)) / 2
