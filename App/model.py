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
from DISClib.Algorithms.Sorting import shellsort as sa
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
    catalog['Artworks'] = lt.newList(('ARRAY_LIST', compareObjectID))

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian las obras de arte y los artistas
    que se encuentran en las listas anteriormente creadas
    """

    """
    Este indice crea un map cuya llave es el año de nacimiento del artista
    """
    catalog['ArtistDates'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapArtistDate)

    """
    Este indice crea un map cuya llave es el autor del libro
    """
    catalog['authors'] = mp.newMap(800,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareAuthorsByName)
    """
    Este indice crea un map cuya llave es la etiqueta
    """
    catalog['tags'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareTagNames)
    """
    Este indice crea un map cuya llave es el Id de la etiqueta
    """
    catalog['tagIds'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareTagIds)
    """
    Este indice crea un map cuya llave es el año de publicacion
    """
    catalog['years'] = mp.newMap(40,
                                 maptype='PROBING',
                                 loadfactor=0.5,
                                 comparefunction=compareMapYear)

    return catalog


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
