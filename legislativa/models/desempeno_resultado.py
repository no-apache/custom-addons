# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DesempenoResultado(models.Model):
    _name = 'legislativa.desempeno_resultado'

    VALUE_SN_KPI = [('0', 'No'),
                    ('1', 'Sí')]

    name = fields.Char(string='Descripción')
    area_id = fields.Many2one(
        comodel_name='legislativa.areas',
        string='Área')
    sub_area_id = fields.Many2one(
        comodel_name='legislativa.sub_areas',
        string='Sub-Área')
    dimension_id = fields.Many2one(
        comodel_name='legislativa.dimension',
        string='Dimensión')
    activada = fields.Boolean(string='Activada')
    definicion = fields.Text(string='Definición')
    val_realizados = fields.Integer(string='Realizados Nº')
    val_planificados = fields.Integer(string='Planificados Nº')
    val_alineados = fields.Integer(string='Alineados')  # Outcomes
    porcentaje = fields.Float(string='% Outputs')
    ratio = fields.Char(string='Ratio')
    cumplimiento = fields.Selection(
        VALUE_SN_KPI,
        string='Cumplimiento')
    pon_planificados = fields.Float(
        string='Ponderación Planificados')  # Outcomes
    pon_realizados = fields.Float(
        string='Ponderación Realizados')  # Outcomes
    pon_alineados = fields.Float(
        string='Ponderación Alineados')  # Outcomes
    peso = fields.Float(string='Peso (sobre 1)')
    minutos = fields.Integer(
        string='Tiempo Empleado - Minutos')
    inversion = fields.Float(
        string='Inversión Empleada')
    por_sin_ponderar = fields.Float(
        string='Porcentaje sin ponderar')
    ratio_sin_ponderar = fields.Char(
        string='Ratio sin ponderar')
    por_ponderado = fields.Float(
        string='Porcentaje ponderado')
    ratio_ponderado = fields.Char(
        string='Ratio ponderado')
    por_sin_ponderar_avr = fields.Float(
        string='Porcentaje sin ponderar')  # Outcomes
    ratio_sin_ponderar_avr = fields.Char(
        string='Ratio sin ponderar')  # Outcomes
    por_ponderado_avr = fields.Float(
        string='Porcentaje ponderado')  # Outcomes
    ratio_ponderado_avr = fields.Char(
        string='Ratio ponderado')  # Outcomes
    tiempo_empleado = fields.Float(
        string='Tiempo Empleado - Horas')
    inversion_empleada = fields.Float(
        string='Inversión Empleada')
    logro = fields.Selection(
        VALUE_SN_KPI,
        string='Logro')  # Outcomes
