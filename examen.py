from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, RFC, apellidos, nombres):
        self.RFC = RFC
        self.apellidos = apellidos
        self.nombres = nombres
        self.sueldoNeto = 0.0

    @abstractmethod
    def calcularSueldoNeto(self):
        pass

    def obtenerRFC(self):
        return self.RFC

    def establecerSueldoNeto(self, sueldo):
        self.sueldoNeto = sueldo


class EmpleadoVendedor(Empleado):
    def __init__(self, RFC, apellidos, nombres, montoVendido, tasaComision):
        super().__init__(RFC, apellidos, nombres)
        self.montoVendido = montoVendido
        self.tasaComision = tasaComision
        self.bonificacion = 0.0

    def calcularIngresos(self):
        return self.montoVendido * self.tasaComision

    def calcularBonificacion(self):
        self.bonificacion = 500 if self.montoVendido > 10000 else 0
        return self.bonificacion

    def calcularDescuento(self):
        ingresos = self.calcularIngresos()
        if ingresos <= 5000:
            return ingresos * 0.05
        elif ingresos <= 10000:
            return ingresos * 0.10
        else:
            return ingresos * 0.15

    def calcularSueldoNeto(self):
        ingresos = self.calcularIngresos()
        bonificacion = self.calcularBonificacion()
        descuento = self.calcularDescuento()
        self.sueldoNeto = ingresos + bonificacion - descuento
        return self.sueldoNeto


class EmpleadoPermanente(Empleado):
    def __init__(self, RFC, apellidos, nombres, sueldoBase, numeroSeguroSocial, constructorInfo):
        super().__init__(RFC, apellidos, nombres)
        self.sueldoBase = sueldoBase
        self.numeroSeguroSocial = numeroSeguroSocial
        self.constructorInfo = constructorInfo

    def calcularIngresos(self):
        return self.sueldoBase

    def calcularDescuento(self):
        return self.sueldoBase * 0.12

    def calcularSueldoNeto(self):
        ingresos = self.calcularIngresos()
        descuento = self.calcularDescuento()
        self.sueldoNeto = ingresos - descuento
        return self.sueldoNeto


class PlantaDeEmpleados:
    def __init__(self):
        self.empleados = []

    def agregarEmpleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("El objeto debe ser una instancia de Empleado o sus subclases.")
        self.empleados.append(empleado)

    def calcularNominaTotal(self):
        totalNomina = 0.0
        for empleado in self.empleados:
            empleado.calcularSueldoNeto()
            totalNomina += empleado.sueldoNeto
            print(f"Empleado: {empleado.nombres} {empleado.apellidos}, RFC: {empleado.RFC}, Sueldo Neto: {empleado.sueldoNeto:.2f}")
        print(f"Total de la Nómina: {totalNomina:.2f}")

    @staticmethod
    def main():
        planta = PlantaDeEmpleados()

        vendedor1 = EmpleadoVendedor("RFC123", "Perez", "Juan", 12000, 0.10)
        vendedor2 = EmpleadoVendedor("RFC456", "Lopez", "Ana", 8000, 0.08)
        permanente1 = EmpleadoPermanente("RFC789", "Garcia", "Luis", 15000, "NSS123456", "Constructor A")
        permanente2 = EmpleadoPermanente("RFC012", "Martinez", "Sofia", 20000, "NSS654321", "Constructor B")

        planta.agregarEmpleado(vendedor1)
        planta.agregarEmpleado(vendedor2)
        planta.agregarEmpleado(permanente1)
        planta.agregarEmpleado(permanente2)

        planta.calcularNominaTotal()


if __name__ == "__main__":
    PlantaDeEmpleados.main()
