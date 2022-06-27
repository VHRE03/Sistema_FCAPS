
from pickle import TRUE
import eel
from pyparsing import line
import linecache

@eel.expose 
def configuracion():
    #OBTENER LOS PUERTOS CON CONEXIONES
    dispositivos_conexion = obtener_conexiones()
    
    #OBTENER EL NUMERO TOTAL DE LINEAS DEL ARCHIVO
    archivo = open("Archivos/config.txt")
    num_lineas = (len(archivo.readlines()))
    archivo.close()

    #OBTENER LOS DATOS DEL SWITCH
    nombre = ""
    ip = ""
    mascara = ""
    entradas = 0
    entradas_conectadas = 0
    estado = linecache.getline("Archivos/config.txt", 1).rstrip('\n')
    print(estado)
    datos_switch = []

    i = 0
    while i < num_lineas:
        linea = linecache.getline("Archivos/config.txt", i).rstrip('\n')

        if(linea == "interface Vlan1"):
            var_aux = linecache.getline("Archivos/config.txt", i+1).rstrip('\n')
            nombre = linea[10:15]
            ip = var_aux[12:25]
            mascara = var_aux[26:40]
            datos_switch.append(nombre)
            datos_switch.append(ip)
            datos_switch.append(mascara)

        i = i + 1

    #OBTENER EL NUMERO DE ENTRADAS DEL SWITCH
    dispositivos = []
    dispositivo = []

    i = 75
    while i < 138:
        j = i
        n = j + 4
        while j < n:
            linea = linecache.getline("Archivos/config.txt",j).rstrip('\n')
            dispositivo.append(linea)
            j = j + 1

        disp = dispositivo[:]
        dispositivo.clear()
        dispositivos.append(disp)
        i = i + 4

    #AGREGAR EL ESTADO A LAS ENTRADAS
    i = 0
    while i < len(dispositivos):
        aux = dispositivos[i][0]
        aux2 = aux[22:26]

        aux3 = False
        j = 0
        while j < len(dispositivos_conexion):
            if(aux2 == dispositivos_conexion[j]):
                dispositivos[i].append("ON")
                aux3 = TRUE
                pass
            j = j + 1

        if aux3 == False:
            dispositivos[i].append("OFF")

        i = i + 1

    entradas = len(dispositivos)
    entradas_conectadas = len(dispositivos_conexion)
    datos_switch.append(entradas)
    datos_switch.append(entradas_conectadas)
    datos_switch.append(estado)

    eel.mostra_conexiones(dispositivos)
    eel.mostrar_datos_switch(datos_switch)

#OBTENER LOS DISPOSITIVOS CON CONEXION
def obtener_conexiones():
    archivo = open("Archivos/config1.txt")
    num_lineas = (len(archivo.readlines()))
    archivo.close()

    conexiones = []
    i = 5
    while i < num_lineas:
        linea = linecache.getline("Archivos/config1.txt",i).rstrip('\n')
        num = linea[2:5]
        conexiones.append(num)
        i = i + 1

    return conexiones

eel.init('HTML')
eel.start('Inicio.html')
