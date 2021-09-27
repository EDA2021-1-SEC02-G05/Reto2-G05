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
    print("1- Obras más antiguas por técinca")
    #print("1- Listar cronológicamente los artistas")
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

def printArtistYear():
    pass

def printArtworkDate():
    pass
def printArtistTec():
    pass
def printArtworkNationality():
    pass
def printTransportation():
    pass
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

        medio = (input('Medio de las obras que se pretende buscar: ')).lower()
        numero = int(input('Número de obras más antiguas a buscar: '))
        respuesta = controller.getMedium(catalog, medio)
        
        primeras_n_obras = lt.subList(respuesta, 1, numero)
        print('Las ' + str(numero)+ ' obras más antiguas para la medio ' + medio + ' son: ')
        for artwork in lt.iterator(primeras_n_obras):
            print(artwork)
        
        """
        
        Requerimiento 1: artistas por fecha de nacimiento

        año_inicial = int(input('Año inicial para el rango de busqueda: '))
        año_final = int(input ('Año final para el rango de busqueda: '))
        artist = controller.getArtistYear(catalog, año_inicial, año_final)
        """
        
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

        dpto = input('Ingrese el departamento del que quiere calcular el costo de transporte de sus obras: ')
        transport = controller.getTransportationCost(catalog, dpto)

    elif int(inputs[0]) == 6:
        'Requerimiento 6: Artistas más prolíferos '


    else:
        sys.exit(7)
sys.exit(7)
