"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de obras y artistas. 
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de obras y artistas

    Crea una lista vacia para guardar todos los artistas y todas las obras

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    Obras de arte
    Año de nacimiento de artistas
    Fecha de adquisición de obras (por año)*
    Obras de arte de un artista clasificadas por técincas
    Obras clasificadas por las nacionalidades de los artistas

    Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,
               'ArtistBeginDate': None,
               'ArtworkDates': None,
               'Medium': None,
               'Nationality': None}


    """
    Estas listas contienen toda la información de las obras de arte y sus artistas.
    Las listas no se encuentran ordenadas por ningún criterio, pero seran utilizadas como referencia
    para los mapas que se van a crearP
    """
    catalog['Artists'] = lt.newList('ARRAY_LIST', compareArtistID)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', compareObjectID)

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian las obras de arte y los artistas
    que se encuentran en las listas anteriormente creadas
    """
    """
    Este indice crea un map cuya llave es el  ID del artista
    """
    catalog['ArtistID'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=3.0,
                                   comparefunction=None)
    """
    Este indice crea un map cuya llave es el año de nacimiento del artista
    """
    catalog['ArtistDates'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=3.0,
                                   comparefunction=compareMapArtistDate)

    """
    Este indice crea un map cuya llave es el autor del libro
    """
    catalog['ArtistArtwork'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtistsByName)
    """
    Este indice crea un map cuya llave es la etiqueta
    """
    catalog['Medium'] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareMediums)

    """
    Este indice crea un map cuya llave es la etiqueta
    """
    catalog['Nationality'] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareNationality)
    """
    Este indice crea un map cuya llave es el Id de la etiqueta
    
    catalog['tagIds'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareTagIds)
    """
    """
    Este indice crea un map cuya llave es el año de publicacion
    
    catalog['years'] = mp.newMap(40,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=compareMapYear)
    """
    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    artists = {'ConstituentID':(artist['ConstituentID']).replace(" ",""),
                    'DisplayName':(artist['DisplayName']).lower(),
                    'Nationality':(artist['Nationality']).lower().replace(" ",""),
                    'Gender':(artist['Gender']).lower(),
                    'BeginDate':artist['BeginDate'],
                    'EndDate':artist['EndDate']}

    lt.addLast(catalog['Artists'], artists)
    #mp.put(catalog['bookIds'], artist['ConstituentID'], artists)

def addArtwork(catalog,artwork):
    artworks = {'ObjectID':(artwork['ObjectID']).replace(" ",""), 
                    'Title':(artwork['Title']).lower(), 
                    'ConstituentID':(artwork['ConstituentID'][1:-1]).replace(" ",""),
                    'Date': artwork[ 'Date'],
                    'Medium':(artwork['Medium']).lower(), 
                    'Classification': (artwork['Classification']).lower(),
                    'Dimensions':artwork['Dimensions'],
                    'CreditLine': (artwork['CreditLine']).lower(), 
                    'Department':(artwork['Department']).lower(), 
                    'DateAcquired':artwork['DateAcquired'],
                    'Weight': artwork['Weight (kg)'],
                    'Circumference': artwork['Circumference (cm)'],
                    'Depth': artwork['Depth (cm)'],
                    'Diameter':artwork['Diameter (cm)'],
                    'Height': artwork['Height (cm)'],
                    'Length': artwork['Length (cm)'],
                    'Width':artwork['Width (cm)']}

    lt.addLast(catalog['Artworks'], artworks)
    #mp.put(catalog['bookIds'], book['goodreads_book_id'], book)
    #authors = book['authors'].split(",")  # Se obtienen los autores
    #for author in authors:
    #    addBookAuthor(catalog, author.strip(), book)
    #addBookYear(catalog, book)

    medium = artworks['Medium']
    addMedium(catalog, medium, artworks)

def newMedium():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    medium = {
              "Artworks": None}

    medium['Artworks'] = lt.newList('ARRAY_LIST', compareMediums)
    return medium

def newNationality():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    nationality = {
              "Artworks": None}

    nationality['Artworks'] = lt.newList('ARRAY_LIST', compareNationality)
    return nationality

def addMedium(catalog, medium_name, artwork):
    """
    Esta función adiciona una obra de arte a un maps que los clasifica por medio.
    """
    artwork_filtrada = {'ObjectID':artwork['ObjectID'], 
                    'Title':artwork['Title'], 
                    'ConstituentID':artwork['ConstituentID'],
                    'Date': artwork[ 'Date'],
                    'Medium':artwork['Medium'] }

    mediums = catalog['Medium']
    existmedium = mp.contains(mediums, medium_name)
    if existmedium:
        entry = mp.get(mediums, medium_name)
        medium_value = me.getValue(entry)
    else:
        medium_value = newMedium()
        mp.put(mediums, medium_name, medium_value)
    lt.addLast(medium_value['Artworks'], artwork_filtrada)

def addNationality(catalog, nation_name, artist):
    """
    Esta función adiciona una obra de arte a un maps que los clasifica por medio.
    """
    artwork_filtrada = {'DisplayName':artist['DisplayName'], 
                    'Nationality':artist['Nationality'], 
                    'Artworks':artist['Artworks'],}

    nations = catalog['Nationality']
    existmedium = mp.contains(nations, nation_name)
    if existmedium:
        entry = mp.get(nations, nation_name)
        nation_value = me.getValue(entry)
    else:
        nation_value = newMedium()
        mp.put(nations, nation_name, nation_value)
    lt.addLast(nation_value['Artworks'], artwork_filtrada)



# Funciones de consulta
def getMedium(catalog, Medium):
    """
    Retorna las obras de arte de un medio específico
    """
    medium_pareja = mp.get(catalog['Medium'], Medium)
    if medium_pareja:
        lista_obras = me.getValue(medium_pareja)
        sortYear(lista_obras['Artworks'])
        return lista_obras['Artworks']
    return None

def getNationality(catalog, Nationality):
    """
    Retorna las obras de arte de un medio específico
    """
    nation_pareja = mp.get(catalog['Nationality'], Nationality)
    if nation_pareja:
        lista_obras = me.getValue(nation_pareja)
        sortYear(lista_obras['Artworks'])
        return lista_obras['Artworks']
    return None

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtistID(id1,id2):
    """
    Compara dos ids de dos artistas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareObjectID(id1,id2):
    """
    Compara dos ids de dos obras de arte
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapArtistDate(date1,entry):
    """
    Compara dos fechas de nacimiento de dos artistas, date1 es un año
    y entry una pareja llave-valor
    """
    date2entry = me.getKey(entry)
    if (int(date1) == int(date2entry)):
        return 0
    elif (int(date1) > int(date2entry)):
        return 1
    else:
        return -1

def compareArtistsByName(Key_artID, artist_ID):
    """
    Compara dos ID's de artistas. El primero es un string
    y el segundo un entry de un map
    """
    arthentry = me.getKey(artist_ID)
    if (Key_artID == arthentry):
        return 0
    elif (Key_artID > arthentry):
        return 1
    else:
        return -1

def compareMediums (medium, entry):
    mediumentry = me.getKey(entry)
    if (medium == mediumentry):
        return 0
    elif (medium > mediumentry):
        return 1
    else:
        return -1

def compareNationality (nationality, entry):
    nationentry = me.getKey(entry)
    if (nationality == nationentry):
        return 0
    elif (nationality > nationentry):
        return 1
    else:
        return -1

def cmpArtworkYear(artwork1,artwork2):
    return int(artwork1['Date']) < int(artwork2['Date'])


# Funciones de ordenamiento

def sortYear(lista_obras):

    ms.sort(lista_obras, cmpArtworkYear)


