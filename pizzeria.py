#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import constantes

print("Portu Pizza")

print("Bienvenido a Portu Pizza")

cantPizzas = int(input('Ingrese la cantidad de pizzas que desea ordenar: '))

print(cantPizzas)

i=1

while(i<=cantPizzas):
    print("Pizza numero "+ str(i))
    tamanoPizza=""
    precioPizza=0
    while((tamanoPizza!="g")and(tamanoPizza!="p")and(tamanoPizza!="m")):
        print("Tamanos: Grande(g) Mediana(m) Personal (p)")
        tamanoPizza = input('Ingrese el tamano de la pizza '+str(i)+":")
        print (constantes.TAMANO.get(tamanoPizza, "Debes seleccionar el tamano correcto"))
        print ("Selecciono el tamano "+str(constantes.TAMANO.get(tamanoPizza)))
    
    print("Opciones: Si(s) No(n)")
    respuesta=input("Desea ingredientes adicionales?")
    
    while(respuesta=="s"):
        print("Con ingredientes adicionales")
        print("Ingredientes:")
        print("Jamon (ja)")
        print("Champinones (ch)")
        print("Pimenton (pi)")
        print("Doble queso (dq)")
        print("Aceitunas (ac)")
        print("Pepperoni (pp)")
        print("Salchichon (sa)")
        ingAdicional = input('Ingrese el ingrediente :')
    if(respuesta=="n"):
        print("Usted ordeno una pizza de tamano "+ constantes.TAMANO.get(tamanoPizza) +" sin ingredientes adicionales")
        precioPizza=constantes.PRECIOS_TAMANO.get(tamanoPizza)
        print("Por un total de "+str(precioPizza) )
    i=i+1