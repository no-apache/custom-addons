from odoo.tests.common import TransactionCase


class TestIniciativas(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestIniciativas, self).setUp(*args, **kwargs)
        self.Iniciativas = self.env['legislativa.iniciativas']

    def test_create_iniciativa(self):
        iniciativa = self.Iniciativas.create({
            'name': 'Test Iniciativa',
            'num_expediente': '1234/2022',
            'legislatura': 'XII',
            'supertipo': 'Proposición de Ley',
            'agrupacion': 'Grupo Parlamentario Popular',
            'tipo': 'Ordinaria',
            'fecha_presentacion': '2022-01-01',
            'fecha_calificacion': '2022-01-02',
            'autor': 'John Doe',
            'situacion_actual': 'En tramitación',
            'plazos': 'Plazo de presentación de enmiendas',
            'tramitacion_seguida': 'Tramitación ordinaria',
            'enlaces_bocg': 'http://www.congreso.es'
        })
        self.assertEqual(iniciativa.name, 'Test Iniciativa')
        self.assertEqual(iniciativa.num_expediente, '1234/2022')
        self.assertEqual(iniciativa.legislatura, 'XII')
        self.assertEqual(iniciativa.supertipo, 'Proposición de Ley')
        self.assertEqual(iniciativa.agrupacion, 'Grupo Parlamentario Popular')
        self.assertEqual(iniciativa.tipo, 'Ordinaria')
        self.assertEqual(iniciativa.fecha_presentacion, '2022-01-01')
        self.assertEqual(iniciativa.fecha_calificacion, '2022-01-02')
        self.assertEqual(iniciativa.autor, 'John Doe')
        self.assertEqual(iniciativa.situacion_actual, 'En tramitación')
        self.assertEqual(iniciativa.plazos,
                         'Plazo de presentación de enmiendas')
        self.assertEqual(iniciativa.tramitacion_seguida,
                         'Tramitación ordinaria')
        self.assertEqual(iniciativa.enlaces_bocg, 'http://www.congreso.es')

    def test_create_iniciativa_required_fields(self):
        with self.assertRaises(Exception) as e:
            self.Iniciativas.create({
                'name': 'Test Iniciativa',
            })
        self.assertIn(
            'null value in column "num_expediente" violates not-null constraint', str(e.exception))
        self.assertIn(
            'null value in column "fecha_presentacion" violates not-null constraint', str(e.exception))
