# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
import sympy as sp
from sympy.plotting import plot
import console


class Application(object):

    def __init__(self):
        self.x = sp.Symbol('x')
        self.equation_i = (28*self.x**2)+36000*self.x
        self.equation_g = (44*self.x**2)+12000*self.x+70000

    def display(self):
        self.getCriticalValues()
        self.getMinMaxValues()
        #self.graphic()

    def getCriticalValues(self):
        """
        Obteniendo los valores críticos aplicando la primera derivada
        """
        console.printHyphen()
        console.highlight("Hallando valores criticos para la funcion I(x)")
        print("\nFuncion I(x) = 28*x**2 + 36000*x")
        console.highlight("Aplicando derivada a la funcion I(x)")
        self.dxCi = sp.diff(self.equation_i, self.x)
        print("I'(x) = {}".format(self.dxCi))

        # Hallando los valores críticos
        console.highlight("Hallando los valores criticos para I(x)")
        print("Igualamos la derivada de la funcion I a CERO para obtener X")
        print("I'(x) = 0")

        self.x_value_i = sp.solve(sp.Eq(self.dxCi, 0), self.x)
        print("Los valores criticos de X para la funcion I son: {}".format(str(self.x_value_i)))

        console.highlight("Hallando valores criticos para la funcion G(x)")
        print("\nFuncion G(x) = 44*x**2 + 12000*x + 70000")
        console.highlight("Aplicando derivada a la funcion G(x)")
        self.dxCg = sp.diff(self.equation_g, self.x)
        print("G'(x) = {}".format(self.dxCg))

        # Hallando los valores críticos
        console.highlight("Hallando los valores criticos para G(x)")
        print("Igualamos la derivada de la funcion G a CERO para obtener X")
        print("G'(x) = 0")

        self.x_value_g = sp.solve(sp.Eq(self.dxCg, 0), self.x)
        print("Los valores criticos de X para la funcion G son: {}".format(str(self.x_value_g)))
        
        console.printHyphen()

    def getMinMaxValues(self):
        """
        Hallando los valores mínimos y máximos de la función.
        """
        console.highlight(
            "Hallando los valores minimos y maximos de la funcion I(x)")
        print("Aplicamos la 2da derivada a la funcion I(x)\n")
        print("{} = {}".format('I(x)'.ljust(6, ' '), self.equation_i))
        print("{} = {}".format("I'(x)".ljust(6, ' '), self.dxCi))

        self.dxdxCi = sp.diff(self.equation_i, self.x, 2)
        print("{} = {}".format("I''(x)".ljust(6, ' '), self.dxdxCi))

        for p in self.x_value_i:
            if self.dxdxCi.subs(self.x, p) > 0:
                tipo = "Min"
            elif self.dxdxCi.subs(self.x, p) < 0:
                tipo = "Max"
            else:
                tipo = "Indefinido"
            print("x = %f (%s)" % (p, tipo))

        console.highlight(
            "Hallando los valores minimos y maximos de la funcion G(x)")
        print("Aplicamos la 2da derivada a la funcion G(x)\n")
        print("{} = {}".format('G(x)'.ljust(6, ' '), self.equation_g))
        print("{} = {}".format("G'(x)".ljust(6, ' '), self.dxCg))

        self.dxdxCg = sp.diff(self.equation_g, self.x, 2)
        print("{} = {}".format("G''(x)".ljust(6, ' '), self.dxdxCg))

        for p in self.x_value_g:
            if self.dxdxCg.subs(self.x, p) > 0:
                tipo = "Min"
            elif self.dxdxCg.subs(self.x, p) < 0:
                tipo = "Max"
            else:
                tipo = "Indefinido"
            print("x = %f (%s)" % (p, tipo))

        console.printHyphen()

    def graphic(self):
        sp.plot(self.equation_i, (self.x, self.x_value[0], self.equation_i.subs(self.x, self.x_value[0])))


if __name__ == '__main__':
    try:
        app = Application()
        app.display()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
