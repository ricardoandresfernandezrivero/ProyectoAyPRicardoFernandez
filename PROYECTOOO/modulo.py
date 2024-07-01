from equipo import Equipo
from estadios import Estadio
from partidos import Partido
from clientes import Cliente
from entradas import Normal
from entradas import VIP
from productos import Alimento
from productos import Bebidas
from restaurante import Restaurant
import random
import json

import requests
import matplotlib.pyplot as plt



def registrarequipo(datos,equipos):
    """ Registra los equipos encontrados en la API """
    for i in range(len(datos)):
        codigofifa=datos[i]["code"]
        nombre=datos[i]["name"]
        grupo=datos[i]["group"]
        equipo = Equipo(codigofifa,nombre,grupo).show()
        equipos.append(equipo)


def registrarestadio(datos2,estadios):
    """ Registra los estadios encontrados en la API """
    for i in range(len(datos2)):
        nombre=datos2[i]["name"]
        ubicacion=datos2[i]["city"]
        id = datos2[i]["id"]
        estadio = Estadio(nombre,ubicacion,id).show()
        estadios.append(estadio)





def registrarpartido(datos3,equipos,partidos,estadios,datos2):
    """ Registra los partidos encontrados en la API a partir de los equipos y estadios ya registrados """
    for i in range(len(datos3)):
        equipolocal1 = datos3[i]["home"]["name"]
        equipovisitante1 = datos3[i]["away"]["name"]
        for n in range(len(equipos)):
            if equipolocal1 == equipos[n]["nombre"]:
                equipolocal = equipos[n]["nombre"]
        equipolocal
        for n2 in range(len(equipos)):
            if equipovisitante1 == equipos[n2]["nombre"]:
                equipovisitante = equipos[n2]["nombre"]
        equipovisitante
        fecha = datos3[i]["date"]
        estadioid = datos3[i]["stadium_id"]
        for j in range(len(datos2)):
            if datos2[j]["id"] == estadioid:
                estadio = estadios[j]["nombre"]
        partido = Partido(equipolocal,equipovisitante,fecha,estadio).show()
        partidos.append(partido)





#Buscar todos los partidos de un pais
def buscarpais(partidos):
    """ Busca los partidos por el nombre del pais en ingles
        -------
        pais
            Pais que quiere ser buscado

    """
    for i in range(len(partidos)):
        local = partidos[i]["local"]
        visitante = partidos[i]["visitante"]
        partidover = f"{local} vs {visitante}"
        print(i,partidover)
    pais = input("Ingrese el nombre del pais en ingles del que quieras buscar todos los partidos: \n")
    for partido in partidos:
        for j,partido1 in partido.items():
            if pais == partido["local"] or pais == partido["visitante"]:
                print(f"{j.title()}: {partido1}")
        
#Buscar los partidos que se juega  en un estadio especifico
def buscarestadio(estadios,partidos):
    """ Busca los partidos por el nombre del estadio
        -------
        estadio1
            Estadio que quiere ser buscado

    """
    print("Listado de todos los estadios:\n")
    for i in range(len(estadios)):
        print(estadios[i]["nombre"])
    estadio1 = input("Ingrese el nombre del estadio: \n") 
    for l in range(len(partidos)):
        if estadio1 == partidos[l]["estadio"]:
            print(f"{partidos[l]["local"]} vs. {partidos[l]["visitante"]}")
        
#Buscar los partidos que se jugaran en una fecha determinada
def buscarfecha(partidos):
    """ Busca los partidos de por el nombre del estadio
        -------
        fechapartido
            Fecha que quiere ser buscada

    """
    dia=int(input("Ingrese el dia del partido que quiera ver: \n"))
    while dia < 14 or dia > 26:
        dia=int(input("Ingrese el dia (14-26) del partido que quiera ver: \n"))
    fechapartido = f"2024-06-{dia}"
    for i in partidos:
        if fechapartido == i["fecha"]:
            print(f"{i["local"]} vs {i["visitante"]}")

def filtropartidos(estadios,partidos):
    """ Crea un menu para filtrar los partidos por distintas caracteristicas
        -------
        opcion 
            Permite seleccionar la opcion que desea ver
    """
    while True:
        print("Seleccione la opcion 1 si quiere filtrar los partidos por pais")
        print("Seleccione la opcion 2 si quiere filtrar los partidos por estadio")
        print("Seleccione la opcion 3 si quiere filtrar los partidos por fecha")
        print("Ingrese 0 si quiere salir")
        opcion = input("Ingrese la opcion que quiera ver: \n")
        if opcion == "1":
            buscarpais(partidos)
        elif opcion == "2":
            buscarestadio(estadios,partidos)
        elif opcion == "3":
            buscarfecha(partidos)
        elif opcion == "0":
            break
        else:
            print("Error")



#Registro del cliente
def registrocliente(clientes,partidos,entradas):
    """ Esta parte del codigo permite registrar el cliente en el archivo txt clientes.txt
        -----
        nombre
            Nombre del cliente
        cedula
            Cedula del cliente
        edad
            Edad del cliente entre 5 y 99 años
        index
            Numero del partido que quiera ver
        tipo
            Tipo de entrada que desea comprar
    """
    nombre = input("ingrese su nombre completo: \n")
    while nombre == None or nombre.isnumeric():
        nombre = input("ingrese su nombre completo: \n")
    cedula = input("ingrese cedula: \n")
    while int(cedula) not in range(1000000,40000000) or not cedula.isnumeric():
        print("Error")
        cedula = input("ingrese cedula de nuevo: \n")
    edad = input("ingrese su edad: \n")
    if int(edad)<5 or int(edad)>99:
        while not edad.isnumeric():
            print("Error")
            edad = int(input("ingrese su edad de nuevo: \n"))
    while True:
        for i in range(len(partidos)):
            print(i, f"{partidos[i]["local"]} vs {partidos[i]["visitante"]} - {partidos[i]["estadio"]} - {partidos[i]["fecha"]} ")
        index = int(input("Ingrese el partido que quiera ver\n"))
        for j in range(len(partidos)):
            if index == j:
                local = partidos[j]["local"]
                visitante = partidos[j]["visitante"]
                partido = f"{local} vs {visitante}"
        while index<0 or index > 35:
            while not index.isnumeric():
                index = int(input("Ingrese el partido que quiera ver de nuevo.\n"))
        if index>=0 or index<36:
            break
    tipo=int(input("seleccione 1- si es cliente normal seleccione 2- si es cliente VIP: \n"))
    id = f"{random.randint(10000000, 100000000)}"
    if tipo == 1:
        tipo2 = "-"
        cliente=Cliente(nombre,cedula,edad,partido,tipo2).show()
        clientes.append(cliente)
        boleto = Normal(cedula,partido,id).show()
        entradas.append(boleto)
        archivoc = open("PROYECTOOO/clientes.txt","a")
        archivoc.write(json.dumps(cliente))
        archivoe = open("PROYECTOOO/entradas.txt","a")
        archivoe.write(json.dumps(boleto))
        archivoc.close()
        archivoe.close()
    elif tipo == 2:
        tipo2 = "VIP"
        cliente=Cliente(nombre,cedula,edad,partido,tipo2).show()
        clientes.append(cliente)
        boleto = VIP(cedula,partido,id).show() 
        entradas.append(boleto)
        archivoc = open("PROYECTOOO/clientes.txt","a")
        archivoc.write(json.dumps(cliente))
        archivoe = open("PROYECTOOO/entradas.txt","a")
        archivoe.write(json.dumps(boleto))
        archivoc.close()
        archivoe.close()
    else:
        print("Error")
    print(clientes)
    print(entradas)
    return cedula,clientes,entradas



#Mapa del estadio
def mapa(clientes,partidos,datos2,entradas):
    print(clientes)
    """ Esta parte del codigo permite al cliente obtener un asiento en el estadio del partido que vera
        -----
        cedula
            Cedula del cliente
        A1
            Columna del asiento
        A2
            Fila del asiento
    """
    cedula = input("Ingrese su cedula: \n")
    for i in range(len(clientes)):
        if cedula == clientes[i]["cedula"]:
            for j in range(len(partidos)):
                if clientes[i]["partido"] == f"{partidos[j]["local"]} vs {partidos[j]["visitante"]}":
                    estadiomapa = partidos[j]["estadio"]
                    for stadium in range(len(datos2)):
                        if estadiomapa == datos2[stadium]["name"]:
                            capacidad = datos2[stadium]["capacity"]
                            capacidadvip = capacidad[0]
                            capacidadnormal = capacidad[1]

            if clientes[i]["tipo"] == "VIP":
                lineas = capacidadvip//10 
                columnas = capacidadvip//lineas
                columnas += 1
                print(f"El estadio tiene {columnas} columnas y {lineas} lineas")
                mapavip = []
                for i in range(lineas):
                    r = []
                    for j in range(columnas):
                        i = i
                        j = j
                        x = 0
                        r.append(x)
                        mapavip.append(r)
                print(mapavip)
                A1 = int(input("Seleccione la columna que quiera estar"))-1
                B1 = int(input("Seleccione la linea que quiera estar"))-1
                if mapavip[A1][B1] == "X":
                    print("Error, el asiento esta ocupado")
                elif A1>lineas or B1>columnas:
                    print("Error")
                else:
                    mapavip[A1][B1] = "X"
                    print([A1],[B1])
                for e in range(len(entradas)):
                    if cedula == entradas[e]["cedula"]:
                        entradas[e]["asiento"]=[[A1],[B1]]



                return entradas
            elif clientes[i]["tipo"] == "-":
                columnas = capacidadnormal//10 
                lineas = capacidadnormal//columnas
                columnas += 1
                print(f"El estadio tiene {columnas} columnas y {lineas} lineas")
                mapa = []
                for i in range(lineas):
                    r = []
                    for j in range(columnas):
                        i = i
                        j = j
                        x = 0
                        r.append(x)
                        mapa.append(r)
                print(mapa)
                A1 = int(input("Seleccione la columna que quiera estar"))-1
                B1 = int(input("Seleccione la linea que quiera estar"))-1

                if mapa[A1][B1] == "X":
                    print("Error, el asiento esta ocupado")
                else:
                    mapa[A1][B1] = "X"
                print([A1],[B1])
                for e in range(len(entradas)):
                    if cedula == entradas[e]["cedula"]:
                        entradas[e]["asiento"]=mapa[A1][B1]
    return entradas








#Costo de la entrada
def numerovampiro(cedula):
    """ Esta parte del codigo permite verificar si la cedula del cliente corresponde a un numro vampiro
        ---
        cedula
            Cedula a evaluar
    """
    cedula1 = str(cedula)

    if len(cedula1) % 2!= 0:
        return False
    mitad = len(cedula1) // 2

    for i in range(10**(mitad-1), 10**mitad):
        if cedula % i == 0:
            par1 = i
            par2 = cedula // i
            x = str(par1)
            y = str(par2)
            if sorted(x+y) == sorted(cedula1):
                return True
  
    return False








#Calcula el costa y muestra una factura
def calcularcosto(clientes,entradas):
    """ Esta parte del codigo permite al cliente comprar su entrada
        cedula
            Cedula del cliente
        confirmar
            Sirve para confirmar si el cliente quiere comprar la entrada
    """
    print(clientes)
    print(entradas)
    cedula=input("Ingrese cedula: \n")
    for i in range(len(clientes)):
        if cedula == clientes[i]["cedula"]:
            if clientes[i]["tipo"] == "-":
                costo = 35
            elif clientes[i]["tipo"] == "VIP":
                costo = 75
        else:
            print("Error, no se encuentra en el sistema")
        vampiro = numerovampiro(int(cedula))
        if vampiro==True:
            costo3 = 0.5*costo
        else:
            costo3 = costo
        confirmar = input("Desea pagar la entrada? S-Si N-No: \n")
        if confirmar.upper() == "S":
            print("RECIBO: \n")
            print(f"Nombre del cliente: {clientes[i]["nombre"]} \nCedula: {cedula} \nPartido:{clientes[i]["partido"]}")
            for e in range(len(entradas)):
                if cedula == entradas[e]["cedula"]:
                    print(f"Asiento: {entradas[e]["asiento"]}")
            print(f"Subtotal: {costo3}\nDescuento:{costo-costo3} \nIVA:{costo3*0.16:.2f}\nTotal:{costo3*1.16:.2f}")
            for j in range(len(entradas)):
                if cedula == entradas[j]["cedula"]:
                    entradas[j]["total"] = f"{costo3*1.16:.2f}"
            print(entradas)

        elif confirmar.upper() == "N":
            print("Regreso al menu")
        else:
            print("Error")










#Menu del modulo de venta de entradas
def ventadeentradas(clientes,partidos,entradas,datos2):
    """ Esta parte del codigo permite al cliente ver la opcion que quiera ver en la venta de entradas
        -
        opcion
            Opcion que el cliente desea
    """
    while True:
        print("Ingrese 1 si quiere registrarse: \n")
        print("Ingrese 2 si quiere elegir un asiento: \n")
        print("Ingrese 3 si quiere comprar el boleto: \n")
        print("Ingrese 0 si quiere salir")
        opcion = input("Ingrese la opcion que quiera ver")
        if opcion == "1":
            registrocliente(clientes,partidos,entradas)
        elif opcion == "2":
            mapa(clientes,partidos,datos2,entradas)
        elif opcion == "3":
            calcularcosto(clientes,entradas)
        elif opcion == "0":
            break
        else:
            print("Error")









#Validar autenticidad del boleto con el codigo    
def autenticidad(entradas):
    """ Esta funcion evalua si el boleto es autentico y a su vez cambia el estado de asistencia del boleto
        id
            ID del boleto que se quiere verificar
    """
    id=input("Ingrese la ID de su boleto: \n")
    for i in range(len(entradas)):
        if id == entradas[i]["id"]:
            print(f"ID: {entradas[i]["id"]}")
            print("La entrada ha sido verificada. Puede asistir al partido.")
            asistencia = entradas[i]["usada"]
            asistencia = True
            entradas[i]["usada"] = asistencia
            print("\n-----INFO DE LA ENTRADA-----")
            print(f"Cedula : {entradas[i]["cedula"]}")
            print(f"Partido : {entradas[i]["partido"]}")
            print(f"Tipo de entrada : {entradas[i]["tipo"]}")
            print(f"ID : {entradas[i]["id"]}")
            print(f"Asiento: {entradas[i]["asiento"]}")
            print(f"Asistido : {entradas[i]["usada"]}")
            print(f"Total : {entradas[i]["total"]}")
        else:
            print("El sistema no tiene ningun usuario con esa ID")











#Boleto repetido
def boletofalso(entradas):
    """ Esta funcion evalua si el boleto ya ha sido utilizado o no o si el boleto es falso
        idaverificar
            ID del boleto que se quiere verificar
    """
    idaverificar = input("Ingrese la id del boleto que quiera verificar:\n")
    for i in range(len(entradas)):
        if idaverificar != entradas[i]["id"]:
            print("El boleto que usted esta ingresando es falso.")
            print("Lastimosamente usted no podra ingresar al estadio con ese boleto.")
        elif idaverificar == entradas[i]["id"] and entradas[i]["usada"] == True:
            print("El boleto que usted ha ingresado ya ha sido utilizado")
            print("Lastimosamente usted no podra ingresar al estadio con ese boleto.")
        else:
            print("Usted puede utilizar el boleto que tiene en mano")








#Menu para los boletos
def boletos(entradas):
    """ 
    Menu para verificar su boleto de distintas formas
    opcion
        Opcion que el cliente desea
    """
    while True:
        print("Ingrese 1 si quiere validar su boleto")
        print("Ingrese 2 si quiere verificar la veracidad de su boleto")
        print("Ingrese 0 si quiere salir")
        opcion = input("Ingrese la opcion que quiera ver:\n")
        if opcion == "1":
            autenticidad(entradas)
        elif opcion == "2":
            boletofalso(entradas)
        elif opcion == "0":
            break
        else:
            print("Error")








#Registra los productos
def registroproducto(productos,datos2):
    """Esta funcion permite registrar los productos por sus distintos atributos y luego guardarlos en un archivo txt productos.txt"""
    for i in range(len(datos2)):
        for l in range(len(datos2[i]["restaurants"])):
                for n in range(len(datos2[i]["restaurants"][l]["products"])):
                    aux = datos2[i]["restaurants"][l]["products"][n]
                    if aux["adicional"] == "plate" or aux["adicional"] == "package":
                        nombre = aux["name"]
                        cantidad = aux["stock"]
                        precio = round(float(aux["price"])*1.16,2)
                        tipo = aux["adicional"]
                        restaurante = datos2[i]["restaurants"][l]["name"]
                        producto = Alimento(nombre,cantidad,precio,tipo,restaurante).show()
                        productos.append(producto)
                    elif aux["adicional"] == "alcoholic" or aux["adicional"] == "non-alcoholic":
                        nombre = aux["name"]
                        cantidad = aux["stock"]
                        precio = round(float(aux["price"])*1.16,2)
                        tipo = aux["adicional"]
                        restaurante = datos2[i]["restaurants"][l]["name"]
                        producto = Bebidas(nombre,cantidad,precio,tipo,restaurante).show()
                        productos.append(producto)  
                    prod = open("PROYECTOOO/productos.txt","w")
                    for j in range(len(productos)):
                        prod.write(f"{productos[j]}\n")
                    prod.close()











#Registra los restaurantes
def registrarrestaurante(datos2,restaurante):
    """Esta funcion permite registrar los restaurantes por sus distintos atributos"""
    for i in range(len(datos2)):
        estadio = datos2[i]["name"]
        for j in range(len(datos2[i]["restaurants"])):
            nombre= datos2[i]["restaurants"][j]["name"]
            productos = datos2[i]["restaurants"][j]["products"]
            restaurant = Restaurant(estadio,nombre,productos).show()
            restaurante.append(restaurant)











#Buscar por nombre
def buscarproductopornombre(estadios,restaurante,productos):
    """Esta funcion permite filtrar los productos por su nombre
    ----
    estadionombre
        Nombre del estadio que quiera evaluar
    nombrerestaurant
        Nombre del restaurante que quiera evaluar
    nombrep
        Nombre del producto que quiera ver
    
    """
    for p in range(len(estadios)):
        print(estadios[p]["nombre"])
    estadionombre = input("Ingrese el nombre del estadio:\n")
    print("Lista de restaurantes:")
    for i in range(len(restaurante)):
        if estadionombre == restaurante[i]["estadio"]:
            print(restaurante[i]["nombre"])
    nombrerestaurant = input("Ingrese el nombre del restaurante que quieras ir:\n")
    for j in range(len(restaurante)):
        if nombrerestaurant == restaurante[j]["nombre"]:
            for p1 in range(len(restaurante[j]["productos"])):
                for p2 in range(len(productos)):
                    if restaurante[j]["productos"][p1]["name"] == productos[p2]["nombre"]:
                        print(productos[p2]["nombre"])
    nombrep = input("Ingrese el nombre del producto que quiera ver:\n")
    for n in range(len(productos)):
        if nombrep == productos[n]["nombre"]:
            print(f"{productos[n]["nombre"]} - {productos[n]["precio"]} - {productos[n]["tipo"]} - {productos[n]["cantidad"]}")








#Buscar por tipo
def buscarproductoportipo(estadios,restaurante,productos):
    """Esta funcion permite filtrar los productos por su nombre
    ----
    estadionombre
        Nombre del estadio que quiera evaluar
    nombrerestaurant
        Nombre del restaurante que quiera evaluar
    tipop
        Tipo de producto que quiera ver
    
    """
    for p in range(len(estadios)):
        print(estadios[p]["nombre"])
    estadionombre = input("Ingrese el nombre del estadio:\n")
    print("Lista de restaurantes:")
    for i in range(len(restaurante)):
        if estadionombre == restaurante[i]["estadio"]:
            print(restaurante[i]["nombre"])
    nombrerestaurant = input("Ingrese el nombre del restaurante que quieras ir:\n")
    for j in range(len(restaurante)):
        if nombrerestaurant == restaurante[j]["nombre"]:
            for p1 in range(len(restaurante[j]["productos"])):
                for p2 in range(len(productos)):
                    if restaurante[j]["productos"][p1]["name"] == productos[p2]["nombre"]:
                        print(productos[p2]["nombre"])
    tipop = input("Ingrese el tipo de producto que quiera ver (plate,package,alcoholic,non-alcoholic):\n")
    for n in range(len(productos)):
        if productos[n]["restaurante"] == nombrerestaurant and tipop == productos[n]["tipo"]:
            print(f"{productos[n]["nombre"]} - {(productos[n]["precio"])} - {productos[n]["tipo"]} - {productos[n]["cantidad"]}")
    if tipop == "0":
        print("Saliendo...")










def buscarproductoporrango(estadios,restaurante,productos):
    """Esta funcion permite filtrar los productos por su nombre
    ----
    estadionombre
        Nombre del estadio que quiera evaluar
    nombrerestaurant
        Nombre del restaurante que quiera evaluar
    rangomin
        Rango minimo de precio que quiera ver
    rangomax
        Rango maximo de precio que quiera ver
    
    """
    for p in range(len(estadios)):
        print(estadios[p]["nombre"])
    estadionombre = input("Ingrese el nombre del estadio:\n")
    print("Lista de restaurantes:")
    for i in range(len(restaurante)):
        if estadionombre == restaurante[i]["estadio"]:
            print(restaurante[i]["nombre"])
    nombrerestaurant = input("Ingrese el nombre del restaurante que quieras ir:\n")
    rangomin=float(input("Ingrese el precio minimo:\n"))
    rangomax=float(input("Ingrese el precio maximo:\n"))
    for n in range(len(productos)):
        if productos[n]["restaurante"] == nombrerestaurant :
            if productos[n]["precio"] >= rangomin and productos[n]["precio"] <= rangomax: 
                print(f"{productos[n]["nombre"]} - {(productos[n]["precio"])} - {productos[n]["tipo"]} - {productos[n]["cantidad"]}")










def menuproductos(estadios,restaurante,productos):
    """Esta funcion permite que el cliente pueda ver los productos y su informacion por distintos filtros
        opcion
            Permite al usuario ver la opcion que el cliente desea ver
    """
    while True:
        print("1- Si quiere ver el producto por nombre")
        print("2- Si quiere ver el producto por tipo")
        print("3- Si quiere ver el producto por rango de precio")
        print("Ingrese 0 si quiere salir")
        opcion = input("Ingrese la opcion que desee")
        if opcion == "1":
            buscarproductopornombre(estadios,restaurante,productos)
        elif opcion == "2":
           buscarproductoportipo(estadios,restaurante,productos)
        elif opcion == "3":
            buscarproductoporrango(estadios,restaurante,productos)
        elif opcion == "0": 
            break
        else:
            print("Error")


#Datos

#Datos






def comprarestaurante(clientes,partidos,restaurante,productos,productoguardado):
    """Esta funcion permite al cliente VIP comprar los productos dependiendo del restaurante
    cedula
        Cedula del cliente
    confirmar
        Permite confirmar la compra
    restauranteselec
        Restaurante al que quiera comprar un producto
    productocomprar
        Producto que desea comprar
    """
    cedula=input("ingrese cedula: \n")
    for cliente in range(len(clientes)):
        if cedula == clientes[cliente]["cedula"]:
            print("Usted está registrado en el sistema")
            if clientes[cliente]["tipo"] == "VIP":
                confirmar = input("Desea realizar una compra?")
                if confirmar.title() == "S":
                    print("Perfecto")
                    for i in range(len(partidos)):
                        local = partidos[i]["local"]
                        visitante = partidos[i]["visitante"]
                        partido1 = f"{local} vs {visitante}"
                        if clientes[cliente]["partido"] == partido1:
                            estadioabuscar = partidos[i]["estadio"]
                            print(f"LISTA DE RESTAURANTES DEL {estadioabuscar}:")
                            for e in range(len(restaurante)):
                                if restaurante[e]["estadio"] == estadioabuscar:
                                    print(restaurante[e]["nombre"])
                            restauranteselec = input("Ingrese el restaurante al que quiera comprar algun producto: ")
                            for r in range(len(restaurante)):
                                if restaurante[r]["nombre"] == restauranteselec:
                                    for p in range(len(productos)-1):
                                        for p2 in range(len(restaurante[r]["productos"])):
                                            if productos[p]["nombre"] == restaurante[r]["productos"][p2]["name"]:
                                                print(f"{productos[p]["nombre"]} - Precio: {productos[p]["precio"]} - Cantidad: {productos[p]["cantidad"]}- Tipo: {productos[p]["tipo"]}")
                            while True:
                                productocomprar = input("Ingrese el producto que quiera comprar. Ingrese salir si quiere salir del menu: \n")
                                for p3 in range(len(productos)):
                                    if productocomprar == productos[p3]["nombre"]:
                                        print(f"{productos[p3]["nombre"]} - Precio: {productos[p3]["precio"]} - Cantidad: {productos[p3]["cantidad"]}- Tipo: {productos[p3]["tipo"]}")
                                        if productos[p3]["tipo"] == "alcoholic" and int(clientes[cliente]["edad"]) < 18:
                                            print("No puede comprar el producto")
                                            productocomprar = input("Ingrese el producto que quiera comprar:\n")
                                        else:
                                            productoelegido = {"Nombre": f"{productos[p3]["nombre"]}", "Precio": f"{productos[p3]["precio"]}", "Cantidad": f"{productos[p3]["cantidad"]}", "Tipo": f"{productos[p3]["tipo"]}"}
                                            productoguardado.append(productoelegido)
                                                
                
                                if productocomprar == "salir":
                                    clientes[cliente]["productos"].append(productoguardado)
                                    break
                            
            else:
                print("No puede comprar nada por no ser VIP")
                           





                    
 

def mostrarcarrito(productoguardado):
    """Esta funcion permite al cliente ver los productos que va a comprar
    cedula
        Cedula del cliente
    """
    print("Producto seleccionado:\n")
    for i in range(len(productoguardado)):
        print(productoguardado[i])








def numeroperfecto(cedula):
    """Esta funcion permite al cliente ver los productos que va a comprar
    cedula
        Cedula del cliente
    """
    multiplos = 0
    for i in range(1,int(cedula)):
        if (int(cedula) % i == 0):
            multiplos += i
    if int(cedula) == multiplos:
        return True
    else:
        return False
    






def procedercompra(clientes,productoguardado,productos):
    """Esta funcion permite realizar la compra de los productos del cliente e imprimpir una factura
    cedula
        Cedula del cliente
    confirmar
        Confirma la opcion del cliente
    """
    cedula=input("ingrese cedula: \n")
    numeroperfecto(cedula)
    total = 0
    for cliente in range(len(clientes)):
        if cedula == clientes[cliente]["cedula"]:
            for j in range(len(productoguardado)):
                total += float(productoguardado[j]["Precio"])
            if numeroperfecto(cedula):
                total2 = 0.85*total
            else:
                total2 = total
        print(f"Total a pagar: {total}")
        confirmar = input("Desea proceder con la compra?")
        if confirmar.title() == "S":
            for k in range(len(productoguardado)):
                for p in range(len(productos)):
                    if productoguardado[j]["Nombre"] == productos[p]["nombre"]:
                        cantidad = int(productos[p]["cantidad"])
                        cantidad -=1
                        productos[p]["cantidad"] = cantidad
                print("RECIBO DE LA COMPRA:\n")
                print("Nombre de los productos:\n")
                for n in range(len(productoguardado)):
                     print(productoguardado[n]["Nombre"])
                print(f"- {productoguardado[j]["Nombre"]} : {productoguardado[j]["Precio"]}")
                print(f"Subtotal: {total}")
                print(f"Descuento: {total-total2}")
                print(f"Total: {total2}")
                print(clientes[cliente]["productos"])
                clientes.append(cliente)


                archivoc = open("PROYECTOOO/clientes.txt","a")
                archivoc.write(json.dumps(productoguardado))
                archivoc.close()

        else:
            print("Saliendo...")









def gestionrestaurante(clientes,partidos,restaurante,productos,productoguardado):
    """Esta funcion muestra un menu para las compras del cliente
    opcion
        Opcion que el cliente desea ver"""
    while True:
        print("1- Si quiere guardar un producto")
        print("2- Si quiere ver los productos que tiene guardado")
        print("3- Si quiere comprar los productos")
        print("Ingrese 0 si quiere salir")
        opcion = input("Ingrese la opcion que desee: ")
        if opcion == "1":
            comprarestaurante(clientes,partidos,restaurante,productos,productoguardado)
        elif opcion == "2":
            mostrarcarrito(productoguardado)
        elif opcion == "3":
            procedercompra(clientes,productoguardado,productos)
        elif opcion == "0": 
            break
        else:
            print("Error")









def gastovip(clientes,cliente1):
    """Esta funcion permite mostrar el gasto promedio de los clientes VIP y muestra un grafico
    """
    cliente1 =[{'nombre': 'dadada', 'cedula': '1231313', 'edad': '17', 'partido': 'France vs Poland', 'tipo': 'VIP', 'productos': []},{'nombre': 'dadada', 'cedula': '1231013', 'edad': '17', 'partido': 'France vs Poland', 'tipo': 'VIP', 'productos': []}]
    gasto = 0
    clientes.append(cliente1[0])
    clientes.append(cliente1[1])
    for i in range(len(clientes)):
        if clientes[i]["tipo"] == "VIP":
            gasto += 75
    for j in range(len(clientes)):
        for j2 in range(len(clientes[j])):
            productoguardado = clientes[j]["productos"]
            for d in range(len(productoguardado)):
                precio = float(productoguardado[d][d]["Precio"])
                gasto += precio
    print(f"El promedio de gasto de los clientes VIP es de {gasto/len(clientes)}")
    x = ["A"]
    y = [gasto/len(clientes)]
    plt.plot(x,y,marker=".")
    plt.show()























def main():
    """Esta funcion contiene todo lo que funciona en el archivo
        """
    url="https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    url2="https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    url3="https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"

    # Get content
    r = requests.get(url)
    r2 = requests.get(url2)
    r3 = requests.get(url3)

    # Decode JSON response into a Python dict:
    if r.status_code == 200 and r2.status_code == 200:
        datos = r.json()
        datos2 = r2.json()
        datos3 = r3.json()

    equipos=[]
    estadios=[]
    partidos=[]
    clientes=[]
    productos=[]
    entradas=[]
    restaurante=[] 
    productoguardado=[]
    cliente1 =[{'nombre': 'dadada', 'cedula': '1231313', 'edad': '17', 'partido': 'France vs Poland', 'tipo': 'VIP', 'productos': []},{'nombre': 'dadada', 'cedula': '1231013', 'edad': '17', 'partido': 'France vs Poland', 'tipo': 'VIP', 'productos': []}]



    registrarequipo(datos,equipos)
    registrarestadio(datos2,estadios)
    registrarpartido(datos3,equipos,partidos,estadios,datos2)
    registroproducto(productos,datos2)
    registrarrestaurante(datos2,restaurante)

    print("----------------BIENVENIDO AL MENU DE EURO 2024---------------------------")
    while True:

        print("Ingrese 1 si quiere filtrar los partidos")
        print("Ingrese 2 si quiere comprar un boleto")
        print("Ingrese 3 si quiere verificar la autenticidad de su boleto ")
        print("Ingrese 4 si quiere filtrar los productos")
        print("Ingrese 5 si quiere comprar productos")
        print("Ingrese 6 si quiere ver el promedio de gasto de los clientes VIP")
        print("Ingrese 0 si quiere salir")
        opcion = int(input("Ingrese la opcion que quiera ver: \n"))
        if opcion == 1:
            filtropartidos(estadios,partidos)
        elif opcion == 2:
            ventadeentradas(clientes,partidos,entradas,datos2)
        elif opcion == 3:
            boletos(entradas)
        elif opcion == 4:
            menuproductos(estadios,restaurante,productos)
        elif opcion == 5:
            gestionrestaurante(clientes,partidos,restaurante,productos,productoguardado) 
        elif opcion == 6:
            gastovip(clientes,cliente1)
        elif opcion == 0:
            break
main()
