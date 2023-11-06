# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EntidadPersona(models.Model):
    _name = 'legislativa.entidad_persona'

    name = fields.Char(string='Iniciales', required=True)
    nombre = fields.Char(string='Nombre')
    escanios = fields.Integer(string='Escaños')
    porcentaje = fields.Float(
        compute='_compute_porcentaje_escanios',
        string='Porcentaje', digits=(2, 8)
    )
    actor_id = fields.Many2one(
        comodel_name='legislativa.actores',
        string='Actor')
    es_entidad = fields.Boolean(string='Es Entidad?', default=True)
    genero = fields.Selection(
        [('hombre', 'Hombre'),
         ('mujer', 'Mujer'),
         ('otro', 'Otro')],
        string='Género')
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False)

    @api.depends('escanios')
    def _compute_porcentaje_escanios(self):
        for record in self:
            if record.actor_id.id == 2:
                record['porcentaje'] = record.escanios / 350 * 1
            elif record.actor_id.id == 3:
                record['porcentaje'] = record.escanios / 265 * 1
            else:
                record['porcentaje'] = 0.0

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, '%s' % (rec.iniciales)))
    #     return result
