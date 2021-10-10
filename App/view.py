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
    print("1- Listar cronológicamente los artistas")
    print("2- Listar cronológicamente las adquisiciones")
    print("3- Clasificar las obras de una artista por técnica")
    print("4- Numero de obras asociadas a una nacionalidad (lab 6)")
    #print("4- Clasificar las obras por nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")
    print("6- Artistas más prolíferos en el museo")
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

def printArtworkDate():
    pass
def printArtistTec():
    pass
def printArtworkNationality(nationalities):
    print('Las 10 nacionalidades con mayor número de obras son: ')

    top10 = lt.subList(nationalities,1, 10)
    top = lt.subList(nationalities,1, 1)


    for nacionalidad in lt.iterator(top10):
        tamano = lt.size(nacionalidad['Artworks'])
        print(nacionalidad['Nationality']+': '+ str(tamano))
    
    for nacionalidad in lt.iterator(top):
        tamano = lt.size(nacionalidad['Artworks'])
        print("La nacionalidad con más obras es: "+nacionalidad["Nationality"]+" con un total de "+str(tamano)+" obras.")
        print("La información de las primeras y ultimas 3 obras de dicha nacionalidad se presenta a continuación:")
        tresprimeras = lt.subList(nacionalidad['Artworks'], 1, 3)
        tresultimas = lt.subList(nacionalidad['Artworks'],tamano-2, 3)
        for artwork in lt.iterator(tresprimeras):
            #print(artwork)
            print("Titulo: " + artwork["Title"] + ", Artista/s : " + str(artwork["Artists"]["elements"])+ ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')
        
        for artwork in lt.iterator(tresultimas):
            #print(artwork)
            print("Titulo: " + artwork["Title"] + ", Artista/s : " + str(artwork["Artists"]["elements"])+ ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')
    
    #print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))


def printArtistTecnique(tecniques_mayor, tamano_tecs, name, total_obras):

    if total_obras > 0:
    
        print('Se encontraron ' + str(total_obras) + ' obras del artista ' + name)
        print('El total de medios/tecnicas utilizados por el artista son: '+str(tamano_tecs))
        
        print('La técnica más utilizada es: '+str(tecniques_mayor['Tecnique'])+'\n y las obras que la utilizan son: \n')
        tamano_mayor = lt.size(tecniques_mayor['Artworks'])

        if tamano_mayor > 6:
        
            prim3 = lt.subList(tecniques_mayor['Artworks'],1,3)
            ult3 = lt.subList(tecniques_mayor['Artworks'],tamano_mayor-2,3)
            
            for artwork in lt.iterator(prim3):
                    print("Titulo: " + artwork["Title"] + ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')

            for artwork in lt.iterator(ult3):
                    print("Titulo: " + artwork["Title"] + ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')

            #print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo)) 
        else: 
            for artwork in lt.iterator(tecniques_mayor['Artworks']):
                    print("Titulo: " + artwork["Title"] + ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')

    else:
        print('No se encontraron obras de arte de la técnica requerida.')


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

        #print(catalog['Nationality'])

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
        printArtworkDate(artwork)

    elif int(inputs[0]) == 3:

        "Requerimiento 3: clasifica obras de un artista por técnica"
        
        name = (input('Nombre del artista sobre el cual quiere realizar la consulta: ')).lower()
        tecniques = controller.getArtistTecnique(catalog, name)
        printArtistTecnique(tecniques[0],tecniques[1], name, tecniques[2])

    elif int(inputs[0]) == 4:

        "Requerimiento 4: clasifica las obras por la nacionalidad de sus creadores"

        #lab 6 

        nationality = (input('Nacionalidad que desea consultar: ')).lower()
         
        nationalities = controller.getNationality(catalog, nationality)

        print(nationalities)

    elif int(inputs[0]) == 5:

        'Requerimiento 5: transportar obras de un departamento '

        dpto = (input('Ingrese el departamento del que quiere calcular el costo de transporte de sus obras: ')).lower()
        transport = controller.getTranspCost(catalog, dpto)
        printTransportationCost(transport[0], transport[1] ,transport[2], transport[3],dpto, transport[4])

    elif int(inputs[0]) == 6:
        'Requerimiento 6: Artistas más prolíferos '

        numero_artistas = int(input('Número de artistas que desea en la clasificación: '))
        año_inicial = int(input('Año inicial para el rango de busqueda: '))
        año_final = int(input('Año final para el rango de busqueda: '))

        artists_inrange = controller.getArtistYear(catalog, año_inicial, año_final)
        proliferos = controller.getProlificArtists(artists_inrange, numero_artistas)



    else:
        sys.exit(7)
sys.exit(7)