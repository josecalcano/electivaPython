#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import constantes
cantidad = 0
precioTotal = 0

def seleccionaIngredientes():
    ingredientes = []
    print('Ingredientes: ')
    print('Jamon          (ja)')
    print('Champinones    (ch)')
    print('Pimenton       (pi)')
    print('Doble Queso    (dq)')
    print('Aceitunas      (ac)')
    print('Pepperoni      (pp)')
    print('Salchichon     (sa)')
    while(True):
        topping = "i"
        while ((topping != "") and (topping != "ja" ) and (topping != "ch" ) and (topping != "pi" ) and (topping != "dq" ) and (topping != "ac" ) and (topping != "pp" ) and (topping != "sa" )):
            topping = input('¿Cuál de estos ingredientes desea? (enter para terminar)')

            if((topping != "") and (topping != "ja" ) and (topping != "ch" ) and (topping != "pi" ) and (topping != "dq" ) and (topping != "ac" ) and (topping != "pp" ) and (topping != "sa" )):
                print("Debe seleccionar una opcion correcta")
            
        if ((topping == "ja") or (topping == "ch" ) or (topping == "pi" ) or (topping == "dq" ) or (topping == "ac" ) or (topping == "pp" ) or (topping == "sa" )):
            print('Ha seleccionado ' + str(constantes.TOPPING.get(topping)))
            ingredientes.append(constantes.TOPPING.get(topping))

        if ((topping == "") and (len(ingredientes) != 0)):
            print('Los ingredientes que ha seleccionado son: ')
            i = 0
            while i < len(ingredientes):
                print(' - ' + ingredientes[i] + ". Precio = " + str(constantes.PRECIOS_TOPPING.get(ingredientes[i])))
                i += 1
            break
        if (topping == ""):    
            print("No ha seleccionado ningun ingrediente adicional")
            break
    return ingredientes

def delivery():
    while (True):
        delivery = ""
        while ((delivery != "n") and (delivery != "s")):
            delivery = input("Actualmente contamos con un servicio de Delivery hacia cualquier lugar de Caracas por un precio extra de Bs 50. ¿Desea agregar al pedido el Delivery? Marque s(Si) | n(No): ")
            if ((delivery != "n") and (delivery != "s")):
                print("Debe seleccionar una opcion correcta")
        if (delivery == "n"):
            return 0
        if (delivery == "s"):
            direccion = input("Ha seleccionado el servicio Delivery. Coloque la dirección a la que se enviara su pedido: ")
            print("La direccion de destino será: " + direccion)
            return 50

def metodoPago(precioTotal):
    print("¿Con qué método de pago pagará? Opciones:")
    pago = ""
    while (True):
        while ((pago != "e") and (pago != "c") and (pago != "p")):
            pago = input(" (e) Efectivo \n (c) Cesta Tickets \n (p) Petros \n")
            if ((pago != "e") and (pago != "c") and (pago != "p")):
                print("Debe seleccionar una opción correcta")
        if (pago == "e"):
            print("Su pago pasará a efectuarse con el método de pago en efectivo.")
            break
        if (pago == "c"):
            print("Su pago pasará a efectuarse con el método de pago en Cesta Tickets.")
            break
        if (pago == "p"):
            precioTotal *= 0.05
            print("Su pago pasará a efectuarse con el método de pago en Petros. Debido a las condiciones del Petro su nuevo monto es de: " + str(precioTotal) + " petros.")
            break

print("--- Portu Pizza ---")
print("Bienvenido a Portu Pizza")

while (True):
    orden = ""
    while ((orden != "n") and (orden != "s")):
        orden = input('Desea ordenar una pizza? Indique su opcion (s) si | (n) no: ')
        if ((orden != "n") and (orden != "s")):
            print("Debe seleccionar una opcion correcta")
    if ((orden == "n")):
        break
    else: 
        cantidad += 1
    tamanoPizza=""
    precioPizza=0
    while((tamanoPizza!="g")and(tamanoPizza!="p")and(tamanoPizza!="m")):
        print("Tamanos: Grande(g) Mediana(m) Personal (p)")
        tamanoPizza = input('Ingrese el tamano de la pizza '+str(cantidad)+":")
        print (constantes.TAMANO.get(tamanoPizza, "Debes seleccionar el tamano correcto"))
        if((tamanoPizza=="g")or(tamanoPizza=="p")or(tamanoPizza=="m")):
            print ("Selecciono el tamano "+str(constantes.TAMANO.get(tamanoPizza)))
    respuesta = "i"
    while ((respuesta!="s") and (respuesta!="n") and (respuesta!="") ):
        print("Opciones: Si(s) No(n) (enter para finalizar)")
        respuesta=input("Desea ingredientes adicionales?")
        if ((respuesta!="s") and (respuesta!="n") and (respuesta!="") ):
            print("Debe seleccionar una opcion correcta")
    if(respuesta=="s"):
        ingredientes = seleccionaIngredientes()
        precioIngrediente = 0
        i = 0
        while (i < len(ingredientes)):
            precioIngrediente = precioIngrediente + constantes.PRECIOS_TOPPING.get(ingredientes[i])
            i += 1
        precioPizza = constantes.PRECIOS_TAMANO.get(tamanoPizza) + precioIngrediente
        precioTotal = precioPizza + precioTotal
        print("El tamano escogido es: " + str(constantes.TAMANO.get(tamanoPizza)) +". El subtotal es: " +str(precioPizza))
      
    if ((respuesta=="n") or (respuesta=="")):
        print("Usted ordeno una pizza de tamano "+ constantes.TAMANO.get(tamanoPizza) +" sin ingredientes adicionales")
        precioPizza = constantes.PRECIOS_TAMANO.get(tamanoPizza)
        precioTotal = precioPizza + precioTotal
        print("Por un monto de "+str(precioPizza) )

if (cantidad == 0):
    print('Adiós!')
else:
    precioTotal += delivery()
    print('La cantidad de pizzas que ordenó fué de ' + str(cantidad) +'. Por un total de ' + str(precioTotal) + ". ")
    metodoPago(precioTotal)