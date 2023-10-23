# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json


class Iniciativas(models.Model):
    """
    Este modelo representa las iniciativas legislativas del sistema.
    Campos:
    - name: Objeto de la iniciativa
    - num_expediente: Numero de expediente de la iniciativa
    - legislatura: Legislatura en la que se presenta la iniciativa
    - supertipo: Supertipo de la iniciativa
    - agrupacion: Agrupacion de la iniciativa
    - tipo: Tipo de la iniciativa
    - fecha_presentacion: Fecha de presentacion de la iniciativa
    - fecha_calificacion: Fecha de calificacion de la iniciativa
    - autor: Autor de la iniciativa
    - comision_competente: Comision competente de la iniciativa
    - situacion_actual: Situacion actual de la iniciativa
    - plazos: Plazos de la iniciativa
    - tipo_tramitacion: Tipo de tramitacion de la iniciativa
    - tramitacion_seguida: Tramitacion seguida de la iniciativa
    - enlaces_bocg: Enlaces a Boletin Oficial de las Cortes Generales de la iniciativa
    """
    _name = 'legislativa.iniciativas'

    name = fields.Char(string='Objeto', required=True)
    num_expediente = fields.Char(string='Numero de expediente')
    legislatura = fields.Char(string='Legislatura')
    supertipo = fields.Char(string='Supertipo')
    agrupacion = fields.Char(string='Agrupacion')
    tipo = fields.Char(string='Tipo')
    fecha_presentacion = fields.Date(string='Fecha presentacion de propuesta')
    fecha_calificacion = fields.Date(string='Fecha calificacion de propuesta')
    autor = fields.Char(string='Autor')
    # comision_competente = fields.Char(string='Comision competente')
    situacion_actual = fields.Char(string='Situacion Actual')
    plazos = fields.Char(string='Plazos')
    # tipo_tramitacion = fields.Char(string='Tipo de tramitacion')
    tramitacion_seguida = fields.Char(string='Tramitacion Seguida')
    enlaces_bocg = fields.Char(string='Enlaces a Bocg')

    @api.model
    def import_data_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

            for item in data:
                record = {
                    'name': item['OBJETO'],
                    'num_expediente': item['NUMEXPEDIENTE'],
                    'legislatura': item['LEGISLATURA'],
                    'supertipo': item['SUPERTIPO'],
                    'agrupacion': item['AGRUPACION'],
                    'tipo': item['TIPO'],
                    'autor': item['AUTOR'],
                    'situacion_actual': item['SITUACIONACTUAL'],
                }
                self.create(record)
