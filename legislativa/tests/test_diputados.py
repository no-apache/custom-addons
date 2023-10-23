# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from odoo.tools import mute_logger


class TestDiputados(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestDiputados, self).setUp(*args, **kwargs)
        self.Diputados = self.env['legislativa.diputados']

    def test_import_data_from_json(self):
        # Test importing data from a JSON file
        file_path = '/opt/odoo/16.0/odoo/custom/legislativa/tests/test_data.json'
        self.Diputados.import_data_from_json(file_path)

        # Check that the records were created
        diputados = self.Diputados.search([])
        self.assertEqual(len(diputados), 2)

        # Check that the data was imported correctly
        diputado1 = self.Diputados.search([('name', '=', 'Diputado 1')], limit=1)
        self.assertEqual(diputado1.circunscripcion, 'Circunscripción 1')
        self.assertEqual(diputado1.grupo_parlamentario_id.name, 'Grupo Parlamentario 1')

        diputado2 = self.Diputados.search([('name', '=', 'Diputado 2')], limit=1)
        self.assertEqual(diputado2.circunscripcion, 'Circunscripción 2')
        self.assertEqual(diputado2.grupo_parlamentario_id.name, 'Grupo Parlamentario 2')

        # Test importing invalid data
        invalid_file_path = '/opt/odoo/16.0/odoo/custom/legislativa/tests/invalid_data.json'
        with self.assertRaises(ValidationError):
            with mute_logger('odoo.sql_db'):
                self.Diputados.import_data_from_json(invalid_file_path)