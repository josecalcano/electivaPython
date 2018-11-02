#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import constantes2

totalAPagar = 0
cantidad = 0
tamanio = ''
precioTamanio = 0

def tamañoPizza():
    tamaño = input('Seleccione un tamaños: Grande(g) | Mediana(m) | Personal (p): ')
    if ( (tamaño == "g") or (tamaño == "p") or (tamaño == "m") ):
        print('El tamaño que has seleccionado es: Pizza ' + str(constantes2.TAMANO.get(tamaño)))
        return constantes2.TAMANO.get(tamaño)
    else:
        print('Debe seleccionar un tamaño correcto!\n')
        tamañoPizza()

def seleccionaIngredientes():
    print('Ingredientes: ')
    print('Jamon          (ja)')
    print('Champinones    (ch)')
    print('Pimenton       (pi)')
    print('Doble Queso    (dq)')
    print('Aceitunas      (ac)')
    print('Pepperoni      (pp)')
    print('Salchichon     (sa)')
    topping = ''
    ingredientes = []
    while (topping != 'salir'):
        topping = input('¿Cuál de estos ingredientes desea? (Escriba "salir" para dejar de agregar ingredientes): ')
        
        if ( (topping == "ja") or (topping == "ch") or (topping == "pi") or (topping == "dq") or (topping == "ac") or (topping == "pp") or (topping == "sa")):
            print('Ha seleccionado ' + str(constantes2.TOOPING.get(topping)))
            ingredientes.append(constantes2.TOOPING.get(topping))
        
        elif (topping == 'salir'):
            print('Los ingredientes que ha seleccionado son: ')
            i = 0
            while i < len(ingredientes):
                print(' - ' + ingredientes[i])
                i += 1
        
        else: 
            print('Debe seleccionar un ingrediente correcto!\n')
    
    return ingredientes


print("¡Bienvenido a Por-tu Pizza!")
while (True):
    orden = input('Desea ordeanr una pizza? Indique su opcion (s) si | (n) no: ')
    if (orden == 'n'):
        break
    else: 
        cantidad += 1

    print('Pizza n° ' + str(cantidad))
    print('Opciones:')
    tamanio = tamañoPizza()
    precioTamanio = constantes2.PRECIOS_TAMANO.get(tamanio)
    totalAPagar =  totalAPagar + precioTamanio
    print('Ahora seleccione los ingredientes que desea en su pizza:')
    ingredientes = seleccionaIngredientes()
    precioIngredientes = 0

    if (len(ingredientes) == 0):
        print('Su pedido es de una Pizza Margarita ' + tamanio)
    else: 
        i = 0
        while (i < len(ingredientes)):
            precioIngredientes = precioIngredientes + constantes2.PRECIOS_TOPPING.get(ingredientes[i])
            i += 1
        
    totalAPagar = totalAPagar + precioIngredientes
    print('Su pedido es de una Pizza ' + tamanio + ' con los siguientes ingredientes: ')
    while i < len(ingredientes):
        print(' - ' + ingredientes[i])
        i += 1
    print('El total a pagar por esta pizza es de: BsS ' + str(totalAPagar))
    
    
if (cantidad == 0):
    print('Adiós!')
else:
    print('La cantidad de pizzas que ordenó fué de ' + str(cantidad) + '. Disfrute de su comida!')