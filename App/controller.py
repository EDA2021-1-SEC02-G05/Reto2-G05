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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras y artistas

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo.  Por cada artista se indica al
    modelo que debe adicionarlo al catalogo.
    """
    booksfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga todas las obras de arte del archivo e indica al modelo
    que los adicione al catalogo
    """
    tagsfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo

def getMedium(catalog, medium):
    return model.getMedium(catalog, medium)

def getArtistYear(catalog,añoi,añof):
    """
    Retorna los artistas nacidos en el rango de años dado
    """
    return model.getArtistYear(catalog,añoi,añof)

def getArtworkYear(catalog,fechai,fechaf):
    """
    Retorna las obras de arte adquiridas en un rango de fechas dadas
    """
    return model.getArtworkYear(catalog,fechai,fechaf)

def getArtistTecnique(catalog, name):
    """
    Retorna las obras de arte de un artista segun su técnica
    """
    return model.getArtistTecnique(catalog, name)

def getArtistNationality(catalog):
    """
    Retorna las obras de arte de un artista segun su técnica
    """
    return model.getArtistNationality(catalog)

def getTranspCost(catalog, dpto):
    """
    Retorna las obras de un departamento dado y el costo asociado a su transporte
    """
    return model.getTranspCost(catalog, dpto)
