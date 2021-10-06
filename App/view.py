"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#Menu de opciones

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    #print("1- Obras más antiguas por técinca")
    print("1- Listar cronológicamente los artistas")
    print("2- Listar cronológicamente las adquisiciones")
    print("3- Clasificar las obras de una artista por técnica")
    print("4- Clasificar las obras por nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")
    print("6- Nuevo exposición en el museo")
    print("7- Salir")

catalog = None

def initCatalog():
    """
    Inicializa el catalogo de obras de arte y artistas
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga las obras de arte y artistas en el catalogo
    """
    controller.loadData(catalog)

def printArtistDate(artist,año_inicial, año_final):
    tamano = lt.size(artist)
    
    if tamano > 0 :
        first_3_artists = lt.subList(artist, 1, 3 )
        last_3_artists = lt.subList(artist, tamano - 2, 3)

        
        print ('Se encontraron ' + str(tamano) + ' artistas nacidos en el rango de ' + str(año_inicial) + ' hasta ' + str(año_final)+ "\n")

        print('Los primeros 3 artistas encontrados en el rango son: ')
        for artist in lt.iterator(first_3_artists):
            print("Nombre: " + artist["DisplayName"] + ", Año de nacimiento: " + artist["BeginDate"] + ", Año de muerte: " + artist["EndDate"] + ", Nacionalidad: "+ artist["Nationality"] + ", Género: " + artist["Gender"])
            

        print('\nLos últimos 3 artistas encontrados en el rango son: ')
        for artist in lt.iterator(last_3_artists):
            print("Nombre: " + artist["DisplayName"] + ", Año de nacimiento: " + artist["BeginDate"] + ", Año de muerte: " + artist["EndDate"] + ", Nacionalidad: "+ artist["Nationality"] + ", Género: " + artist["Gender"])
        
    else:
        print('No se encontraron artistas nacidos en este rango de años')
    pass

def printArtworkDate():
    pass
def printArtistTec():
    pass
def printArtworkNationality():
    pass
def printTransportationCost(transportation, costo_total, old, peso_total, dpto, tiempo):
    tamano = lt.size(transportation)
    if tamano > 0 :

        print('El total de obras a transporte del departamento de '+ dpto +' es: '+str(tamano)+'\n')
        print('\n El estimado total en USD para el costo del servicio es: '+ str(costo_total)+'\n')
        print('\n El estimado total del peso de las obras es: '+ str(peso_total)+'\n')

        top5_viejas = lt.subList(old, 1, 5 )
        print('\n Las 5 obras más antiguas a transportar son: \n')
        for artwork in lt.iterator(top5_viejas):
            
            print("Titulo: " + artwork['Artwork']["Title"] + ", Artistas: "+  str(artwork['Artwork']["Artist/s"]["elements"]) + ", Clasificación : " + artwork['Artwork']["Classification"] + ", Fecha: "+ artwork['Artwork']["Date"] + ", Medio: "+ artwork['Artwork']["Medium"] + ", Dimensiones: " + artwork['Artwork']["Dimensions"] + ", Costo de Transporte: " + str(artwork["Cost"]) + '\n')
        
        top5_costosas = lt.subList(transportation, 1 , 5)
        print('\n Las 5 obras más costosas de transportar son: \n')

        for artwork in lt.iterator(top5_costosas):
            
            print("Titulo: " + artwork['Artwork']["Title"] + ", Artistas: " + str(artwork['Artwork']["Artist/s"]["elements"])  + ", Clasificación : " + artwork['Artwork']["Classification"] + ", Fecha: "+ artwork['Artwork']["Date"] + ", Medio: "+ artwork['Artwork']["Medium"] + ", Dimensiones: " + artwork['Artwork']["Dimensions"] + ", Costo de Transporte: " + str(artwork["Cost"])+ '\n')
        print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))
    else: 
        print('No se encontraron obras para transportar de ese departamento')

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")

        catalog = initCatalog()
        loadData(catalog)

        tamano_artwork = lt.size(catalog['Artworks'])
        tamano_artist = lt.size(catalog['Artists'])

        last_3_artworks = lt.subList(catalog['Artworks'], tamano_artwork - 2, 3 )
        last_3_artists = lt.subList(catalog['Artists'], tamano_artist - 2, 3)

        print('Obras de arte cargadas: ' + str(tamano_artwork)+'\n')
        print('Artistas cargados: ' + str(tamano_artist)+ '\n')
        print('Últimas tres obras de arte cargadas:')

        for artwork in lt.iterator(last_3_artworks):
            print(artwork)

        print("")
        print("-----------------------------------------------------------------------------------")
        print("")
        print('Últimos tres artistas cargados:')
        
        for artist in lt.iterator(last_3_artists):
            print(artist)


    elif int(inputs[0]) == 1:


        """
        Parte del lab

        medio = (input('Medio de las obras que se pretende buscar: ')).lower()
        numero = int(input('Número de obras más antiguas a buscar: '))
        respuesta = controller.getMedium(catalog, medio)
        
        primeras_n_obras = lt.subList(respuesta, 1, numero)
        print('Las ' + str(numero)+ ' obras más antiguas para la medio ' + medio + ' son: ')
        for artwork in lt.iterator(primeras_n_obras):
            print(artwork)
        
        """
        """
        Requerimiento 1: artistas por fecha de nacimiento
        """

        año_inicial = int(input('Año inicial para el rango de busqueda: '))
        año_final = int(input ('Año final para el rango de busqueda: '))
        artist = controller.getArtistYear(catalog, año_inicial, año_final)
        printArtistDate(artist,año_inicial, año_final)
        
        
    elif int(inputs[0]) == 2:

        "Requerimiento 2: obras de arte por fecha de adquisición"

        fecha_inicial = (input('Fecha inicial para el rango de busqueda: '))
        fecha_final = (input('Fecha final para el rango de busqueda: '))
        artwork = controller.getArtworkYear(catalog, fecha_inicial, fecha_final)

    elif int(inputs[0]) == 3:

        "Requerimiento 3: clasifica obras de un artista por técnica"
        
        name = input('Nombre del artista sobre el cual quiere realizar la consulta: ')
        tecniques = controller.getArtistTecnique(catalog, name)

    elif int(inputs[0]) == 4:

        "Requerimiento 4: clasifica las obras por la nacionalidad de sus creadores"
  
        nationalities = controller.getArtistNationality(catalog)

    elif int(inputs[0]) == 5:

        'Requerimiento 5: transportar obras de un departamento '

        dpto = (input('Ingrese el departamento del que quiere calcular el costo de transporte de sus obras: ')).lower()
        transport = controller.getTranspCost(catalog, dpto)
        printTransportationCost(transport[0], transport[1] ,transport[2], transport[3],dpto, transport[4])

    elif int(inputs[0]) == 6:
        'Requerimiento 6: Artistas más prolíferos '


    else:
        sys.exit(7)
sys.exit(7)