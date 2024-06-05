class Empleado:
    def __init__(self, id, nombre, empresa_id):
        self.id = id
        self.nombre = nombre
        self.empresa_id = empresa_id

    def __str__(self):
        return f"Empleado(id={self.id}, nombre={self.nombre}, empresa_id={self.empresa_id})"
