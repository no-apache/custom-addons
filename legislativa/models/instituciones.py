# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instituciones(models.Model):
    """
    Este modelo representa las instituciones o actores que participan en las iniciativas legislativas.
    Campos:
    - name: Nombre de la institucion
    - tipo: Tipo de institucion
    - comunidad_autonoma: Comunidad Autonoma a la que pertenece la institucion
    """
    _name = 'legislativa.instituciones'

    COMUNIDAD_CIUDAD_AUTONOMA = [
        ('andalucia', 'Andalucía'),
        ('aragon', 'Aragón'),
        ('asturias', 'Asturias'),
        ('baleares', 'Baleares'),
        ('canarias', 'Canarias'),
        ('cantabria', 'Cantabria'),
        ('castilla_la_Mancha', 'Castilla la Mancha'),
        ('castilla_y_leon', 'Castilla y León'),
        ('catalunia', 'Cataluña'),
        ('comunidad_valenciana', 'Comunidad Valenciana'),
        ('extremadura', 'Extremadura'),
        ('galicia', 'Galicia'),
        ('la_rioja', 'La Rioja'),
        ('madrid', 'Madrid'),
        ('murcia', 'Murcia'),
        ('navarra', 'Navarra'),
        ('pais_vasco', 'País Vasco'),
        ('ciudad_de_ceuta', 'Ciudad de Ceuta'),
        ('ciudad_de_melilla', 'Ciudad de Melilla')
    ]

    name = fields.Char(string='Nombre Institución', required=True)
    tipo = fields.Selection(
        [('1', 'Instituciones del Estado'),
         ('2', 'Instituciones Autonomicas'),
         ('3', 'Sector Publico Institucional'),
         ('4', 'Alianzas'),
         ('5', 'Otros')
         ], string='Tipo', required=True)
    comunidad_autonoma = fields.Selection(
        COMUNIDAD_CIUDAD_AUTONOMA, string='Comunidad/Ciudad Autónoma')

    # Restricciones de unicidad del campo nombre en la base de datos (SQL) para el modelo Instituciones (legislativa.instituciones)
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "El nombre de la institución debe ser único"),
    ]
