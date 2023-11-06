# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoInstitucion(models.Model):
    _name = 'legislativa.tipo_institucion'

    name = fields.Char()

    # Restricciones de unicidad del campo nombre en la base de datos (SQL) para el modelo TipoInstitucion (legislativa.tipo_institucion)
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "El nombre del tipo de institución debe ser único"),
    ]


class Actores(models.Model):
    """
    Este modelo representa las instituciones o actores que participan en las iniciativas legislativas.
    Campos:
    - name: Nombre de la institucion
    - tipo: Tipo de institucion
    - es_legislativa: Indica si la institucion es legislativa o no
    - legislatura: Legislatura a la que pertenece la institucion
    - entidad_persona_ids: Relacion con el modelo Entidad Persona 
    """
    _name = 'legislativa.actores'

    name = fields.Char(string='Nombre', required=True)
    tipo = fields.Many2one('legislativa.tipo_institucion',
                           string='Tipo', required=True)
    es_legislativa = fields.Boolean(string='Es Legislativa?', default=False)
    legislatura = fields.Char(string='Legislatura')
    entidad_persona_ids = fields.One2many(
        comodel_name='legislativa.entidad_persona',
        inverse_name='actor_id',
        string='Entidades - Personas')

    # Restricciones de unicidad del campo nombre en la base de datos (SQL) para el modelo Actores (legislativa.actores)
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name,legislatura)',
         "El nombre de la institución debe ser único"),
    ]
