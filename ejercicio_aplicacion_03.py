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
        self.equation_cost = (0.2*(0.01*self.x**2+121))/self.x

    def display(self):
        self.determineVariables()
        self.getCriticalValues()
        self.getMinMaxValues()
        self.graphic()

    def determineVariables(self):
        console.printHyphen()
        console.highlight("1. Determinamos las variables")
        print("\nFuncion de Costo C(x) = 0.2* (0.01x**2 + 121)")
        console.printHyphen()

    def getCriticalValues(self):
        """
        Obteniendo los valores críticos aplicando la primera derivada
        a la función C(x)
        """
        console.highlight("Aplicando derivada a la funcion C(x)")
        self.dxC = sp.diff(self.equation_cost, self.x)
        print("C'(x) = {}".format(self.dxC))

        # Hallando los valores críticos
        console.highlight("Hallando los valores criticos")
        print("Igualamos la derivada de la funcion C a CERO para obtener X")
        print("C'(x) = 0")

        self.x_value = sp.solve(sp.Eq(self.dxC, 0), self.x)
        print("Los valores criticos de X son: {}".format(str(self.x_value)))
        #print("Seleccionamos x = {}".format(self.x_value[1]))
        console.printHyphen()

    def getMinMaxValues(self):
        """
        Hallando los valores mínimos y máximos de la función.
        """
        console.highlight(
            "Hallando los valores minimos y maximos de la funcion C(x)")
        print("Aplicamos la 2da derivada a la funcion C(x)\n")
        print("{} = {}".format('C(x)'.ljust(6, ' '), self.equation_cost))
        print("{} = {}".format("C'(x)".ljust(6, ' '), self.dxC))

        self.dxdxC = sp.diff(self.equation_cost, self.x, 2)
        print("{} = {}".format("C''(x)".ljust(6, ' '), self.dxdxC))
        
        for p in self.x_value:
            if self.dxdxC.subs(self.x,p)>0: 
                tipo="Min"
            elif self.dxdxC.subs(self.x,p)<0: 
                tipo="Max"
            else: 
                tipo="Indefinido"
            print("x = %f (%s)"%(p,tipo))

        console.printHyphen()

    def graphic(self):
        sp.plot(self.equation_cost, (self.x,self.x_value[0], self.x_value[1]))

if __name__ == '__main__':
    try:
        app = Application()
        app.display()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
