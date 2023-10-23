# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GruposParlamentarios(models.Model):
    _name = 'legislativa.grupos_parlamentarios'

    name = fields.Char(string='Nombre', required=True)
    iniciales = fields.Char(string='Iniciales')
    nombre_corto = fields.Char(string='Abreviatura')
    numero_diputados = fields.Integer(compute='_compute_diputados',
                                      string='Número de diputados', store=True)
    diputados_ids = fields.One2many(
        comodel_name='legislativa.diputados',
        inverse_name='grupo_parlamentario_id',
        string='Diputados')

    def _compute_diputados(self):
        for record in self:
            record['numero_diputados'] = self.env['legislativa.diputados'].search_count(
                [('grupo_parlamentario_id', '=', record.id)])
