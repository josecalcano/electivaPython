#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import constantes

# variables globales para la cantidad total de pizzas y el precio total de estas.
cantidad = 0
precioTotal = 0

# funcion para la seleccion de los ingredientes para la pizza
def seleccionaIngredientes():
    # lista de ingredientes, pues una pizza puede tener mas de un ingrediente
    ingredientes = []

    print('Ingredientes: ')
    print('Jamon          (ja)')
    print('Champinones    (ch)')
    print('Pimenton       (pi)')
    print('Doble Queso    (dq)')
    print('Aceitunas      (ac)')
    print('Pepperoni      (pp)')
    print('Salchichon     (sa)')
    
    # ciclo infinito para la seleccion de los ingredientes. 
    while(True):
        # damos valor a la variable topping para que cuando el usuario solo presione enter salga del ciclo
        topping = "i"
        
        while ((topping != "") and (topping != "ja" ) and (topping != "ch" ) and (topping != "pi" ) and (topping != "dq" ) and (topping != "ac" ) and (topping != "pp" ) and (topping != "sa" )):
            # obtenemos el ingrediente que el usuario desea
            topping = input('¿Cuál de estos ingredientes desea? (enter para terminar)')

            #validamos que seleccione opciones disponibles
            if((topping != "") and (topping != "ja" ) and (topping != "ch" ) and (topping != "pi" ) and (topping != "dq" ) and (topping != "ac" ) and (topping != "pp" ) and (topping != "sa" )):
                print("Debe seleccionar una opcion correcta")
            
        if ((topping == "ja") or (topping == "ch" ) or (topping == "pi" ) or (topping == "dq" ) or (topping == "ac" ) or (topping == "pp" ) or (topping == "sa" )):
            # al seleccionar un ingrediente se muestra cual ha sido seleccionado
            print('Ha seleccionado ' + str(constantes.TOPPING.get(topping)))
            # y se agrega a la lista de ingredientes
            ingredientes.append(constantes.TOPPING.get(topping))

        # cuando el usuario ha presionado enter y hay ingredientes seleccionados
        if ((topping == "") and (len(ingredientes) != 0)):
            # mostramos uno a uno cuales han sido los ingredientes seleccionados con sus precios.
            print('Los ingredientes que ha seleccionado son: ')
            i = 0
            while i < len(ingredientes):
                print(' - ' + ingredientes[i] + ". Precio = " + str(constantes.PRECIOS_TOPPING.get(ingredientes[i])))
                i += 1
            break
        # si el usuario presiona enter se le aclara que no ha seleccionado ningun ingrediente
        if (topping == ""):    
            print("No ha seleccionado ningun ingrediente adicional")
            break
    return ingredientes

# Mensaje de bienvenida al sistema
print("Portu Pizza")
print("Bienvenido a Portu Pizza")

# ciclo infinito para la toma de ordenes de pizzas.
while (True):
    # variable que nos dira si el usuario quiere o no quiere pizzas
    orden = ""

    while ((orden != "n") and (orden != "s")):
        orden = input('Desea ordenar una pizza? Indique su opcion (s) si | (n) no: ')
        # si ha seleccionado algo distinto a las opciones se le notifica
        if ((orden != "n") and (orden != "s")):
            print("Debe seleccionar una opcion correcta")
    # si la opcion es 'n' salimos del sistema
    if ((orden == "n")):
        break
    else: 
        # si la opcion es 's' pasamos a agregar una pizza
        cantidad += 1
    
    # inicializamos variables para la pizza actual
    tamanoPizza=""
    precioPizza=0

    # mientras no tengamos un valor de tamano de pizza mostramos que opciones hay
    while( (tamanoPizza!="g") and (tamanoPizza!="p") and (tamanoPizza!="m") ):
        print("Tamanos: Grande(g) Mediana(m) Personal (p)")
        # leemos el tamano ingresado por el usuarios
        tamanoPizza = input('Ingrese el tamano de la pizza '+str(cantidad)+":")
        
        # debemos validar que el usuario seleccione un tamano correcto
        print(constantes.TAMANO.get(tamanoPizza, "Debes seleccionar el tamano correcto"))

        # si el tamano es correcto pasamos a indicar cual ha sido el tamano elegido
        if( (tamanoPizza=="g") or (tamanoPizza=="p") or (tamanoPizza=="m") ):
            print ("Selecciono el tamano "+str(constantes.TAMANO.get(tamanoPizza)))
    
    # creamos una variable 'respuesta' para saber el input del usuario
    respuesta = "i"
    while ((respuesta!="s") and (respuesta!="n") and (respuesta!="") ):
        print("Opciones: Si(s) No(n) (enter para finalizar)")

        #leemos la opcion que ha elegido el usuario
        respuesta = input("Desea ingredientes adicionales?")

        # validamos que el usuario seleccione una opcion valida
        if ((respuesta!="s") and (respuesta!="n") and (respuesta!="") ):
            print("Debe seleccionar una opcion correcta")

    # si selecciona 's' pasamos a llamar al metodo que se encarga de la seleccion de ingredientes
    if(respuesta=="s"):
        # obtenemos la lista de ingredientes que desea el usuario
        ingredientes = seleccionaIngredientes()

        # variable para el precio de los ingredientes
        precioIngrediente = 0
        i = 0
        while (i < len(ingredientes)):
            # por cada ingrediente calculamos su precio y lo sumamos al total de precio de ingredientes
            precioIngrediente = precioIngrediente + constantes.PRECIOS_TOPPING.get(ingredientes[i])
            i += 1
        
        # calculamos el precio de la pizza basado en su tamano mas el calculo del precio de los ingredientes
        precioPizza = constantes.PRECIOS_TAMANO.get(tamanoPizza) + precioIngrediente

        # como pueden existir pizzas anteriores debemos sumar el nuevo precio de la pizza al precio total
        precioTotal = precioPizza + precioTotal

        # mostramos informacion de la pizza elegida con su precio correspondiente
        print("El tamano escogido es: " + str(constantes.TAMANO.get(tamanoPizza)) +". El subtotal es: " +str(precioPizza))
      
    # cuando el usuario presiona enter o la opcion 'n'
    if ((respuesta=="n") or (respuesta=="")):
        # informamos de la decision que ha tomado
        print("Usted ordeno una pizza de tamano "+ constantes.TAMANO.get(tamanoPizza) +" sin ingredientes adicionales")
        
        # calculamos el total de la(s) pizza(s)
        precioPizza = constantes.PRECIOS_TAMANO.get(tamanoPizza)
        precioTotal = precioPizza + precioTotal

        # e informamos del monto final que debe pagar
        print("Por un monto de "+str(precioPizza) )

# si la cantidad es 0 lamentablemente no ha querido comprar pizzas, por lo que enviamos un mensaje alentando a comprar la proxima vez que nos visite
if (cantidad == 0):
    print('Esperamos que vuelva pronto por una deliciosa pizza. Adiós!')    
# finalmente mostramos la cantidad total de pizzas que ha ordenado con el precio total a pagar
else:
    print('La cantidad de pizzas que ordenó fué de ' + str(cantidad) +'. Por un total de ' + str(precioTotal) + ". Gracias por su compra! Que tenga buen dia.")