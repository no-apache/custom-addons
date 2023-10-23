from odoo.tests.common import TransactionCase


class TestInstituciones(TransactionCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.Instituciones = self.env['legislativa.instituciones']

    def test_instituciones_uniqueness(self):
        # Create a new institucion with a unique name
        institucion_1 = self.Instituciones.create({
            'name': 'Institucion 1',
            'tipo': '1',
            'comunidad_autonoma': 'andalucia'
        })

        # Try to create another institucion with the same name
        with self.assertRaises(Exception):
            self.Instituciones.create({
                'name': 'Institucion 1',
                'tipo': '2',
                'comunidad_autonoma': 'aragon'
            })

    def test_instituciones_fields(self):
        # Create a new institucion
        institucion_1 = self.Instituciones.create({
            'name': 'Institucion 1',
            'tipo': '1',
            'comunidad_autonoma': 'andalucia'
        })

        # Check that the fields were correctly set
        self.assertEqual(institucion_1.name, 'Institucion 1')
        self.assertEqual(institucion_1.tipo, '1')
        self.assertEqual(institucion_1.comunidad_autonoma, 'andalucia')
