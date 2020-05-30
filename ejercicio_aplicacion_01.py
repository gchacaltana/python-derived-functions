# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
import sympy as sp
import console


class Rectangle(object):

    def __init__(self, perimeter):
        """
        x = Base del rectangulo
        y = Altura del rectangulo
        Perimeter = 2x + 2y
        Area = x.y
        """
        self.perimeter = perimeter
        self.x, self.y = sp.Symbol('x'), sp.Symbol('y')
        self.equation_perimeter = 2*self.x+2*self.y
        self.equation_area = self.x*self.y

    def display(self):
        self.determineVariables()
        self.getAreaFunction()
        self.getCriticalValues()
        self.getMinMaxValues()
        self.showResults()

    def determineVariables(self):
        console.printHyphen()
        console.highlight("1. Determinamos las variables")
        print("x = Base del rectangulo")
        print("y = Altura del rectangulo")
        print("\nArea Rectangulo = x*y => A(x,y)")
        print("Perimetro Rectangulo = 2x + 2y")
        console.printHyphen()

    def getAreaFunction(self):
        console.highlight("2. Obtenemos el valor de y a partir del perimetro")
        print("2x + 2y = {}".format(perimeter))
        self.y_value_in_x = sp.solve(
            sp.Eq(self.equation_perimeter, self.perimeter), self.y)
        print("y = {}".format(str(self.y_value_in_x[0])))

        console.highlight("3. Reemplazamos el valor de y en la funcion A(x,y)")
        str_equation_area = 'x*({})'.format(str(self.y_value_in_x[0]))
        self.equation_area_x = sp.parse_expr(str_equation_area)
        print("A(x,y) = {}".format(self.equation_area_x))

        print("\nPodemos decir: ")
        print("A(x) = {}".format(self.equation_area_x))
        console.printHyphen()

    def getCriticalValues(self):
        """
        Obteniendo los valores críticos aplicando la primera derivada
        a la función A(x,y)
        """
        console.highlight("4. Aplicando derivada a la funcion A(x)")
        self.dxA = sp.diff(self.equation_area_x, self.x)
        print("A'(x) = {}".format(self.dxA))

        # Hallando los valores críticos
        console.highlight("5. Hallando los valores criticos")
        print("Igualamos la derivada de la funcion A a CERO para obtener X")
        print("A'(x) = 0")

        self.x_value = sp.solve(sp.Eq(self.dxA, 0), self.x)
        print("El valor de x = {}".format(self.x_value[0]))
        console.printHyphen()

    def getMinMaxValues(self):
        """
        Hallando los valores mínimos y máximos de la función.
        """
        console.highlight(
            "6. Hallando los valores minimos y maximos de la funcion A(x)")
        print("Aplicamos la 2da derivada a la funcion A(x)\n")
        print("{} = {}".format('A(x)'.ljust(6, ' '), self.equation_area_x))
        print("{} = {}".format("A'(x)".ljust(6, ' '), self.dxA))
        self.dxdxA = sp.diff(self.dxA, self.x)
        print("{} = {}".format("A''(x)".ljust(6, ' '), self.dxdxA))
        self.result_2da_dev = int(self.dxdxA)
        if (self.result_2da_dev < 0):
            print("{} < 0, entonces existe un {} en x = {}".format(
                "A''(x)".ljust(6, ' '), 'maximo absoluto', self.x_value[0]))

        console.printHyphen()

    def showResults(self):
        console.highlight("7. Finalmente, podemos decir:")
        print("x = {}".format(self.x_value[0]))
        self.equation_y = sp.parse_expr(str(self.y_value_in_x[0]))
        self.y_value = self.equation_y.subs(self.x, int(self.x_value[0]))
        print("y = {} => {}".format(str(self.y_value_in_x[0]), self.y_value))
        if int(self.x_value[0]) == int(self.y_value):
            print("La figura es un cuadrado por tener los mismos valores para X y Y")
        print("\nEl valor de la funcion A(x,y) = x.y")
        print("A(x,y) = {}".format(self.equation_area.subs(
            {self.x: int(self.x_value[0]), self.y: int(self.y_value)})))


if __name__ == '__main__':
    try:
        perimeter = int(input("\n{}".format(console.labelInput(
            "Ingrese la longitud de la cuerda (en cm): "))))
        app = Rectangle(perimeter)
        app.display()

    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
