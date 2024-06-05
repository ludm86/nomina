import unittest
from gerente import Gerente
from empleado import Empleado
from departamento import Departamento

class TestNomina(unittest.TestCase):

    def test_empresa(self):
        empresa = Empresa(1, "Empresa A")
        self.assertEqual(empresa.id, 1)
        self.assertEqual(empresa.nombre, "Empresa A")
    
    def test_gerente(self):
        gerente = Gerente(1, "Gerente A", 1)
        self.assertEqual(gerente.id, 1)
        self.assertEqual(gerente.nombre, "Gerente A")
        self.assertEqual(gerente.empresa_id, 1)

    def test_empleado(self):
        empleado = Empleado(1, "Empleado 1", 1)
        self.assertEqual(empleado.id, 1)
        self.assertEqual(empleado.nombre, "Empleado 1")
        self.assertEqual(empleado.empresa_id, 1)
    
    def test_departamento(self):
        departamento = Departamento(1, "Departamento A", 1)
        self.assertEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "Departamento A")
        self.assertEqual(departamento.empresa_id, 1)

if __name__ == '__main__':
    unittest.main()
