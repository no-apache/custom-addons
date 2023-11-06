# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Areas(models.Model):
    _name = 'legislativa.areas'

    name = fields.Char(compute="_compute_name", string='Nombre')
    area_name = fields.Selection([
        ('glob', 'Global'),
        ('diag', 'Diagnósticos'),
        ('prel', 'Plan Relacional'),
        ('pali', 'Plan de Alianzas'),
        ('pcom', 'Plan de Comunicación'),
        ('pdid', 'Plan de Influencia Digital')],
        string='Seleccione Plan:', required=True)
    aapp_name = fields.Selection([
        ('outputs', 'Modelo AAPP Outputs'),
        ('outcomes', 'Modelo AAPP Outcomes')],
        string='Seleccione Modelo:', required=True)
    descripcion = fields.Text(string='Descripción')
    sub_areas_ids = fields.One2many(
        comodel_name='legislativa.sub_areas',
        inverse_name='area_id',
        string='Sub-Área')

    @api.depends('area_name')
    def _compute_name(self):
        for record in self:
            record.name = dict(self._fields['area_name'].selection).get(
                record.area_name)


class SubAreas(models.Model):
    _name = 'legislativa.sub_areas'

    name = fields.Char(string='Nombre')
    area_id = fields.Many2one(
        comodel_name='legislativa.areas',
        string='Área')
    dimension_ids = fields.One2many(
        comodel_name='legislativa.dimension',
        inverse_name='sub_area_id',
        string='Dimensiones')


class Dimension(models.Model):
    _name = 'legislativa.dimension'

    name = fields.Char(string='Nombre')
    sub_area_id = fields.Many2one(
        comodel_name='legislativa.sub_areas',
        string='Sub-Área')
