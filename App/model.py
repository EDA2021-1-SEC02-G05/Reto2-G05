﻿"""
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
from DISClib.Algorithms.Sorting import mergesort_req6 as ms6
assert cf
import datetime as d
import time
import math


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
               'ArtistDates': None,
               'ArtworkDates': None,
               'ArtistTecnique':None,
               'Nationality': None,
               'ArtworkDpto':None}


    """
    Estas listas contienen toda la información de las obras de arte y sus artistas.
    Las listas no se encuentran ordenadas por ningún criterio, pero seran utilizadas como referencia
    para los mapas que se van a crearP
    """
    catalog['Artists'] = lt.newList('ARRAY_LIST', compareArtistID)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', cmpfunction = compareObjectID)

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian las obras de arte y los artistas
    que se encuentran en las listas anteriormente creadas
    """

    """
    Este indice crea un map cuya llave es el año de nacimiento del artista
    """
    catalog['ArtistDates'] = mp.newMap(100,
                                   maptype='PROBING',
                                   loadfactor= 0.5,
                                   comparefunction=compareMapArtistDate)

    """
    Este indice crea un map cuya llave es el artista y dentro se encuentra otro mapa que 
    """
    catalog['ArtworkDates'] = mp.newMap(100,
                                   maptype='PROBING',
                                   loadfactor= 0.5,
                                   comparefunction=compareMapArtistDate)

    """
    Este indice crea un map cuya llave es el artista y dentro se encuentra otro mapa que 
    """
    catalog['Medium'] = mp.newMap(100,
                                   maptype='PROBING',
                                   loadfactor= 0.5,
                                   comparefunction=compareMapMediums)

    """
    Este indice crea un map cuya llave es el artista y dentro se encuentra otro mapa que 
    """
    catalog['ArtistTecnique'] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=compareArtistsByName)
    """
    Este indice crea un map cuya llave es el artista y dentro se encuentra otro mapa que 
    """
    catalog['Nationality'] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.8,
                                comparefunction=compareNationality)
    """
    Este indice crea un map cuya llave es el departamento y el valor son sus obras de arte
    """
    catalog['ArtworkDpto'] = mp.newMap(300,
                                  maptype='PROBING',
                                  loadfactor=0.5,
                                  comparefunction=compareMapDptos)


    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    artists = {'ConstituentID':(artist['ConstituentID']).replace(" ",""),
                    'DisplayName':(artist['DisplayName']).lower(),
                    'Nationality':(artist['Nationality']).lower().replace(" ",""),
                    'Gender':(artist['Gender']).lower(),
                    'BeginDate':artist['BeginDate'],
                    'EndDate':artist['EndDate'],
                    'Artworks':lt.newList('ARRAY_LIST')}

    lt.addLast(catalog['Artists'], artists)
    addArtistDate(catalog,artists['BeginDate'], artists)


def addArtwork(catalog,artwork):
    artwork = {'ObjectID':(artwork['ObjectID']).replace(" ",""), 
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
                    'Width':artwork['Width (cm)'],
                    'Artists':lt.newList('ARRAY_LIST')}

    lt.addLast(catalog['Artworks'], artwork)
    
    department = artwork['Department']
    addDpto(catalog, department, artwork)

    addArtworkDate(catalog, artwork['DateAcquired'], artwork)

    artist_id = artwork['ConstituentID'].split(',')
    
    #Lab 5
    medium = artwork['Medium']
    addMediumlab5(catalog, medium, artwork)
    
    for id in artist_id:

        addArtistTecnique(catalog,id,artwork)
        addArtistNation(catalog,id,artwork)

def newMediumlab5():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    medium = {
              "Artworks": None}

    medium['Artworks'] = lt.newList('ARRAY_LIST')
    return medium

def addMediumlab5(catalog, medium_name, artwork):
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
        medium_value = newMediumlab5()
        mp.put(mediums, medium_name, medium_value)
    lt.addLast(medium_value['Artworks'], artwork_filtrada)

def addArtistTecnique(catalog,id,artwork):
    """
    Función que primero busca en la lista de artistas el artista que le corresponde al ID que está entrando como parámetro y luego con el displayname de ese artista
    crea un map cuya llave es el nombre del artista y el valor asociado es un map clasificando sus obras de arte por técnicas.
    """
    artists = catalog['Artists']

    posartist = lt.isPresent(artists, id)

    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        lt.addLast(artist['Artworks'], artwork)
        lt.addLast(artwork['Artists'], artist['DisplayName'])

    artists_map = catalog['ArtistTecnique']
    existartist = mp.contains(artists_map, artist['DisplayName'])

    if existartist:
        entry = mp.get(artists_map, artist['DisplayName'])
        artist_value = me.getValue(entry)
        artist_value['TotalArtworks'] += 1
        addMedium(artist_value, artwork['Medium'], artwork)

    else:
        artist_value = newArtist()
        addMedium(artist_value, artwork['Medium'], artwork)
        mp.put(artists_map, artist['DisplayName'], artist_value)

def newArtist():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    artist_tec = {
                    'TotalArtworks':'',
                    'MediumMayor':None,
                    "Artworks": None,
                    'TotalMedium':0}

    artist_tec['Artworks'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMediums)

    artist_tec['TotalArtworks'] = 1


    return artist_tec

def newMedium(tec):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    medium = {'Tecnique': tec,
               'Size': 1,
               'Artworks': None}

    medium['Artworks'] = lt.newList('ARRAY_LIST')

    return medium


def addMedium(medium, medium_name, artwork):
    """
    Esta función adiciona una obra de arte a un maps que los clasifica por medio.
    """
    
    artwork_filtrada = {'ObjectID':artwork['ObjectID'], 
                    'Title':artwork['Title'], 
                    'Date': artwork[ 'Date'],
                    'Medium':artwork['Medium'],
                    'Dimensions':artwork['Dimensions'] }

    mediums = medium['Artworks']
    existmedium = mp.contains(mediums, medium_name)
    if existmedium:
        entry = mp.get(mediums, medium_name)
        medium_value = me.getValue(entry)
        medium_value['Size'] += 1
    else:
        medium_value = newMedium(medium_name)
        mp.put(mediums, medium_name, medium_value)
        medium['TotalMedium'] += 1
    lt.addLast(medium_value['Artworks'], artwork_filtrada)


def addArtistNation(catalog,id,artwork):
    """
    #Función que primero busca en la lista de artistas el artista que le corresponde al ID que está entrando como parámetro y luego con el displayname de ese artista
    #crea un map cuya llave es el nombre del artista y el valor asociado es un map clasificando sus obras de arte por técnicas.
    """
    artists = catalog['Artists']
    posartist = lt.isPresent(artists, id)

    if posartist > 0:
        artist = lt.getElement(artists, posartist)

    nationality_map = catalog['Nationality']
    nation_name = artist['Nationality']
    if nation_name == '' or nation_name == 'nationalityunknown':
        nation_name = 'unknown'

    existnation = mp.contains(nationality_map, nation_name)

    if existnation:
        entry = mp.get(nationality_map, nation_name)
        nation_value = me.getValue(entry)
    else:
        nation_value = newNationality()
        mp.put(nationality_map, nation_name, nation_value)
    lt.addLast(nation_value['Artworks'], artwork)

def newNationality():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    nationality_work = {
                        "Artworks": None}

    nationality_work['Artworks'] = lt.newList('ARRAY_LIST', cmpfunction = compareObjectID)
    return nationality_work


def addArtistDate(catalog,begindate ,artist):
    begindate_int = int(begindate)
    if int(begindate) != 0 and begindate != '':

        artist_filt = {'DisplayName': artist['DisplayName'],
                    'BeginDate': artist['BeginDate'],
                    'EndDate': artist['EndDate'],
                    'Nationality':artist['Nationality'],
                    'Gender': artist['Gender']
                    }

        dates_map = catalog['ArtistDates']
        existdate = mp.contains(dates_map, begindate_int)
        if existdate:
            entry = mp.get(dates_map, begindate_int)
            date_value = me.getValue(entry)
        else:
            date_value = newDate(begindate_int)
            mp.put(dates_map, begindate_int, date_value)
        lt.addLast(date_value['Artists'], artist_filt)

def newDate(date):

    date = {'Date': date,
            'Artists':None}

    date['Artists'] = lt.newList('ARRAY_LIST')
    
    return date

def addArtworkDate(catalog,fecha_ad, artwork):

    if  fecha_ad != '':
        fecha_sep = (fecha_ad).split('-')
        year_int = int(fecha_sep[0])

        artwork_filt = {'Title': artwork['Title'],
                    'Artists': artwork['Artists'],
                    'Date': artwork['Date'],
                    'Medium':artwork['Medium'],
                    'Dimensions': artwork['Dimensions'],
                    'DateAcquired': artwork['DateAcquired'],
                    'CreditLine': artwork ['CreditLine']
                    }

        dates_map = catalog['ArtworkDates']
        existdate = mp.contains(dates_map, year_int)
        if existdate:
            entry = mp.get(dates_map, year_int)
            date_value = me.getValue(entry)
        else:
            date_value = newArtworkDate(year_int)
            mp.put(dates_map, year_int, date_value)
        lt.addLast(date_value['Artworks'], artwork_filt)
        

def newArtworkDate(date):

    date = {'Year': date,
            'Artworks':None}

    date['Artworks'] = lt.newList('ARRAY_LIST')
    
    return date

def addDpto(catalog,dpto ,artwork):

    department = catalog['ArtworkDpto']
    existdepartment = mp.contains(department, dpto)
    if existdepartment:
        entry = mp.get(department, dpto)
        dpto_value = me.getValue(entry)
    else:
        dpto_value = newDpto()
        mp.put(department, dpto, dpto_value)
    lt.addLast(dpto_value['Artworks'], artwork)

def newDpto():
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    dpto = {
              "Artworks": None}

    dpto['Artworks'] = lt.newList('ARRAY_LIST')
    return dpto


# Funciones de consulta

def getArtistYear(catalog, year_i, year_f):
    start_time = time.process_time()
    artist_inrange = lt.newList('ARRAY_LIST')
    i = year_i

    while i >= year_i and i <= year_f:
        pareja_year = mp.get(catalog['ArtistDates'], i)

        if pareja_year:
            year_value = me.getValue(pareja_year)

            for artist in lt.iterator(year_value['Artists']): 
                lt.addLast(artist_inrange,artist)
        
        i += 1
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return artist_inrange, elapsed_time_mseg

def getArtworkYear(catalog, fecha_i, fecha_f):
    start_time = time.process_time()
    artwork_inrange = lt.newList('ARRAY_LIST')

    fecha_i_sep = (fecha_i).split('-')
    fecha_f_sep = (fecha_f).split('-')
    purchased = 0

    i = int(fecha_i_sep[0]) 

    while i >= int(fecha_i_sep[0]) and i <= int(fecha_f_sep[0]):
        di = d.datetime(int(fecha_i_sep[0]),int(fecha_i_sep[1]), int(fecha_i_sep[2]))
        df = d.datetime(int(fecha_f_sep[0]),int(fecha_f_sep[1]), int(fecha_f_sep[2]))
        pareja_year = mp.get(catalog['ArtworkDates'], i)
        i+=1
           
        if pareja_year:
            year_value = me.getValue(pareja_year)

            for artwork in lt.iterator(year_value['Artworks']):
                date_artwork = artwork['DateAcquired'].split("-")
                d1 = d.datetime(int(date_artwork[0]),int(date_artwork[1]), int(date_artwork[2]))

                if d1 >= di and d1 <= df:
                    lt.addLast(artwork_inrange, artwork)
                    if 'purchase' in artwork['CreditLine'].lower():
                        purchased += 1

    size = lt.size(artwork_inrange)
    sortArtwork(artwork_inrange)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return artwork_inrange, size, elapsed_time_mseg, purchased

def getMediumlab5(catalog, Medium):
    
    #Parte del lab 5

    medium_pareja = mp.get(catalog['Medium'], Medium)
    if medium_pareja:
        lista_obras = me.getValue(medium_pareja)
        sortYear(lista_obras['Artworks'])
        return lista_obras['Artworks']
    return None

def getArtistTecnique(catalog, artist_name):
    """
    Retorna las obras de arte de un artista clasificadas por medio/técnica
    """
    start_time = time.process_time()
    artist_map = mp.get(catalog['ArtistTecnique'], artist_name)
    mayor_num = 0
    mayor_elem = None
    
    if artist_map:
        tecnique_map = me.getValue(artist_map)
        tecnique_values = mp.valueSet(tecnique_map['Artworks'])
        tamano_tecs = mp.size(tecnique_map['Artworks'])
        total_obras = tecnique_map['TotalArtworks']


        for tecnique in lt.iterator(tecnique_values):

            if lt.size(tecnique['Artworks']) > mayor_num:
                mayor_num = lt.size(tecnique['Artworks'])
                mayor_elem = tecnique 

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return mayor_elem, tamano_tecs, total_obras, elapsed_time_mseg


def getNationality_lab(catalog, nationality):
   
    #Parte del lab 6

    nation_map = catalog['Nationality']
    nationality_entry = mp.get(nation_map, nationality)
    nationality_value = me.getValue(nationality_entry)

    total_obras = lt.size(nationality_value['Artworks'])

    return total_obras

def getNationality(catalog):

    start_time = time.process_time()
    answer = lt.newList("ARRAY_LIST",cmpfunction=compareNationality)

    nation_map = catalog['Nationality']
    nationality =  mp.keySet(nation_map)
    
    for name in lt.iterator(nationality):
        nationality_entry = mp.get(nation_map, name)
        nationality_value = me.getValue(nationality_entry)

        artworks = nationality_value['Artworks']
        
        total_obras = lt.size(nationality_value['Artworks'])
        diccionario = {"Nationality": name,
                        "Total works": total_obras,
                        "Artwork": artworks
                        }
        lt.addLast(answer, diccionario)
    
    sortNationalitysize(answer)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return answer,elapsed_time_mseg

def getTranspCost(catalog, dpto):
    start_time = time.process_time()
    costo_total = 0
    peso_total = 0
    transp_cost = lt.newList('ARRAY_LIST')
    artwork_dpto_entry = mp.get(catalog['ArtworkDpto'], dpto)

    if artwork_dpto_entry: 

        artworksBydpto = me.getValue(artwork_dpto_entry)

        for artwork in lt.iterator(artworksBydpto['Artworks']):

            artwork_filtrada = {'Title': artwork['Title'],
                                'Artist/s':artwork['Artists'],
                                'Classification': artwork['Classification'],
                                'Date':artwork['Date'],
                                'Medium':artwork['Medium'],
                                'Dimensions':artwork['Dimensions']}
            weight = artwork['Weight']

            if artwork['Weight'] == '':
                weight = 0
            else: 
                weight = float(artwork['Weight'])

            cost_weight=round(((weight)*72),2)
            cost_a = round(((cost_Area(artwork))/10000),2) 
            cost_vol = round(((cost_volume(artwork))/1000000),2)

            if cost_weight == 0 and cost_a == 0 and cost_vol == 0:
                costo_total  += 48.00
                cost = {'Artwork':artwork_filtrada, 
                        'Cost':48.00}

                lt.addLast(transp_cost,cost)

            elif cost_weight > cost_vol and cost_weight > cost_a:
                
                    costo_total  += cost_weight
                    peso_total += weight
                    cost = {'Artwork':artwork_filtrada, 
                            'Cost':cost_weight}

                    lt.addLast(transp_cost,cost)

            elif cost_a > cost_weight and cost_a > cost_vol:
                
                    costo_total += cost_a
                    peso_total += weight
                    cost = {'Artwork':artwork_filtrada, 
                            'Cost':cost_a}

                    lt.addLast(transp_cost,cost)

            elif cost_vol > cost_a and cost_vol > cost_weight:

                    costo_total  += cost_vol
                    peso_total += weight
                    cost = {'Artwork':artwork_filtrada, 
                            'Cost':cost_vol}

                    lt.addLast(transp_cost,cost)
            
        copy= lt.subList(transp_cost,1,lt.size(transp_cost))
        sortTransportation(transp_cost)
        sortTranspOld(copy)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000

        return transp_cost,round(costo_total,2), copy, peso_total, elapsed_time_mseg

def cost_Area(artwork):
    pi = math.pi
    length = artwork['Length']
    height = artwork['Height']
    width = artwork['Width']
    diameter =artwork['Diameter']

    #area de la forma largo por altura
    if artwork['Length'] == '':
        length = 0
    else: 
        length = float(length)
    if artwork['Height'] == '':
        height = 0
    else: 
        height = float(height)   
    
    if artwork['Diameter'] == '':
        diameter = 0
    else: 
        diameter = float(diameter)

    if artwork['Width'] == '':
        width = 0
    else: 
        width = float(width)


    cost_area1 = (length*height)*72
    cost_area5 = (width*height)*72
    #area de circulo    
    cost_area2 = (pi*((diameter)/2)**2)*72
    #area cilindro
    cost_area3 = (2*(pi*(diameter)/2)*height) + 2*((math.pi*((diameter)/2)**2))*72
    #area esfera
    cost_area4 = (4*(pi*(diameter)/2)**2)*72

    if cost_area1 > cost_area2 and cost_area1 >cost_area3 and cost_area1 > cost_area4 and cost_area1 > cost_area5:
        return cost_area1
    elif cost_area2 > cost_area1 and cost_area2 > cost_area3 and cost_area2 > cost_area4 and cost_area2 > cost_area5: 
        return cost_area2
    elif cost_area3 > cost_area1 and cost_area3 > cost_area2 and cost_area3 > cost_area4 and cost_area3 > cost_area5 :
        return cost_area3
    elif cost_area4 > cost_area1 and cost_area4 > cost_area2 and cost_area4 > cost_area3 and cost_area4 > cost_area5 :
        return cost_area4
    else: 
        return cost_area5


def cost_volume(artwork):

    pi = math.pi

    length = artwork['Length']
    height = artwork['Height']
    diameter = artwork['Diameter']
    width = artwork['Width']
    depth = artwork['Depth']

    if artwork['Width'] == '':
        width = 0
    else: 
        width = float(width)
    if artwork['Length'] == '':
        length = 0
    else: 
        length = float(length)
    if artwork['Height'] == '':
        height = 0
    else: 
        height = float(height)
    if artwork['Diameter'] == '':
        diameter = 0
    else: 
        diameter = float(diameter)
    if artwork['Depth'] == '':
        depth = 0
    else: 
        depth = float(depth)

    #volumen de la forma longitud por altura por ancho

    cost_vol1 = (length*height*width)*72
    cost_vol2 = (length*height*depth)*72

    #volumen esfera
    cost_vol3 = ((4/3)*((pi*(diameter)/2)**3))*72
    #volumen cilindro
    cost_vol4 = ((pi*((diameter)/2)**2)*height)*72

    if cost_vol1 > cost_vol2 and cost_vol1 > cost_vol3 and cost_vol1 > cost_vol4:
        return cost_vol1
    elif cost_vol2 > cost_vol1 and cost_vol2 > cost_vol3 and cost_vol2 > cost_vol4:
        return cost_vol2
    elif cost_vol3 > cost_vol1 and cost_vol3 > cost_vol2 and cost_vol3 > cost_vol4:
        return cost_vol3
    
    else: 
        return cost_vol4



def getProlificArtists(artists_inrange, catalog ,num):
    artists_inrange_map = lt.newList('ARRAY_LIST')


    for artist in artists_inrange['elements']:

        artist_map = mp.get(catalog['ArtistTecnique'], artist['DisplayName'])

        if artist_map:
            artist_value = me.getValue(artist_map)

            lt.addLast(artists_inrange_map, artist_value)

    print(artists_inrange_map)

    sortProlificArtist(artists_inrange_map)

    sublist = lt.subList(artists_inrange_map, 1, num)

    return sublist

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtistID(id1,id2):
    """
    Compara dos ids de dos artistas
    """
    if (int(id1) == int(id2['ConstituentID'])):
        return 0
    elif int(id1) > int(id2['ConstituentID']):
        return 1
    else:
        return -1

def compareObjectID(id1,id2):
    """
    Compara dos ids de dos obras de arte
    """
    if (int(id1) == int(id2['ObjectID'])):
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

def compareArtistsByName(Key_artname, artist_name):
    """
    Compara dos nombres de artistas. El primero es un string
    y el segundo un entry de un map
    """
    arthentry = me.getKey(artist_name)
    if (Key_artname == arthentry):
        return 0
    else:
        return -1

def compareMapMediums (medium, entry):
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

def cmpNationalitysize(nat1,nat2):

    return (nat1['Total works']) > (nat2['Total works'])

def cmpArtworkYear(artwork1,artwork2):
    return int(artwork1['Date']) < int(artwork2['Date'])

def compareMapDptos(dpto,entry):
    dptoentry = me.getKey(entry)
    if (dpto == dptoentry):
        return 0
    elif (dpto > dptoentry):
        return 1
    else:
        return -1

def cmpTranspOld (artwork1,artwork2):

    if artwork1['Artwork']['Date'] != '' and artwork2['Artwork']['Date'] != '':

        return int(artwork1['Artwork']['Date']) <  int(artwork2['Artwork']['Date'])

def cmpTranspCost(cost1,cost2):

    return int(cost1['Cost']) > int(cost2['Cost'])

def cmpartworkyear(artwork1,artwork2):

    if artwork1['DateAcquired'] != '' and artwork2['DateAcquired'] != '':

        date_1 = d.date.fromisoformat(artwork1['DateAcquired'])
        date_2 = d.date.fromisoformat(artwork2['DateAcquired'])

        return date_1 < date_2

def cmpArtworkDate(artwork1,artwork2):
    return int(artwork1['Date']) < int(artwork2['Date'])

def cmpTecSize(size1, size2):

    return int(size1['Size']) < int(size2['Size'])

def cmpProlific(artist1, artist2):

    if artist1['TotalArtworks'] > artist2['TotalArtworks']:

        return 0
    
    elif artist1['TotalArtworks'] == artist2['TotalArtworks']:

        if artist1['TotalMedium'] > artist2['TotalMedium']:

            return 0

    else:
        return -1

# Funciones de ordenamiento
def sortProlificArtist(artistrange):

    ms6.sort(artistrange, cmpProlific)

def sortTecSize(tecnique_map):

    ms.sort(tecnique_map, cmpTecSize)

def sortYear(lista_obras):
    "lab 5"
    ms.sort(lista_obras, cmpArtworkDate)

def sortTranspOld(list_old):

    ms.sort(list_old, cmpTranspOld)

def sortTransportation(transp_cost):

    ms.sort(transp_cost, cmpTranspCost)

def sortNationalitysize(nationalities):
    
    ms.sort(nationalities, cmpNationalitysize)

def sortArtwork(artwork_inrange):

    ms.sort(artwork_inrange, cmpartworkyear)
