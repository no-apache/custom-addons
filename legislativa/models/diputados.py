# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json


class Diputados(models.Model):
    _name = 'legislativa.diputados'

    name = fields.Char(string='Name', required=True)
    imagen = fields.Binary(string='Imagen')
    edad = fields.Integer(string='Edad')
    genero = fields.Selection(
        [('hombre', 'Hombre'),
         ('mujer', 'Mujer')
         ], string='Género')
    circunscripcion = fields.Char(string='Circunscripción')
    grupo_parlamentario_id = fields.Many2one(
        'legislativa.grupos_parlamentarios', string='Grupo Parlamentario')

    @api.model
    def import_data_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

            for item in data:
                record = {
                    'name': item['NOMBRE'],
                    'circunscripcion': item['CIRCUNSCRIPCION'],
                    'grupo_parlamentario_id': item['GRUPOPARLAMENTARIO']
                }
                self.create(record)
