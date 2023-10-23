# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase


class TestGruposParlamentarios(TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.grupo_parlamentario = self.env['legislativa.grupos_parlamentarios'].create({
            'name': 'Grupo Parlamentario de Prueba',
            'iniciales': 'GPP',
            'nombre_corto': 'GP Prueba',
        })

    def test_compute_diputados(self):
        diputado1 = self.env['legislativa.diputados'].create({
            'name': 'Diputado 1',
            'grupo_parlamentario_id': self.grupo_parlamentario.id,
        })
        diputado2 = self.env['legislativa.diputados'].create({
            'name': 'Diputado 2',
            'grupo_parlamentario_id': self.grupo_parlamentario.id,
        })
        self.assertEqual(self.grupo_parlamentario.numero_diputados,
                         2, 'El número de diputados no coincide')
        diputado1.unlink()
        self.assertEqual(self.grupo_parlamentario.numero_diputados,
                         1, 'El número de diputados no coincide')
