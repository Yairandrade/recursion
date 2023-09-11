"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Fernando De la Rosa
 *
 """

import config
from DISClib.DataStructures import listnode as node
from DISClib.Utils import error as error
import csv
assert config

"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente RECURSIVA para almacenar una colección de elementos.
  Se definen los algoritmos RECURSIVOS que implementan su funcionalidad.
  Los elementos de una lista se cuentan desde la posición 1.

"""

def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Se inicializan los apuntadores a la primera y ultima posicion en None.
    El tipo de la listase inicializa como RECURSIVE_SINGLE_LINKED
    Args:
        cmpfunction: Función de comparación para los elementos de la lista.
        Si no se provee una función de comparación, se utilizará la función
        de comparación por defecto pero se debe suministrar un valor para key

        key: Identificador que se debe utilizar para la comparación de
        elementos de la lista

        filename: Si se provee este valor, se creará una lista a partir de
        la informacion que se encuentra en el archivo CSV

        delimiter: Si se provee un archivo para crear la lista, indica el
        delimitador a usar para separar los campos del archivo CSV

    Returns:
        Un diccionario que representa la estructura de datos de una lista
        encadanada vacia.

    Raises:

    """
    newlist = {'first': None,
               'size': 0,
               'key': key,
               'type': 'RECURSIVE_SINGLE_LINKED',
               'datastructure': module
               }

    if cmpfunction is None:
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if filename is not None:
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            addLast(newlist, line)
    return newlist

def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, ajusta el apuntador
    al primer elemento e incrementa el tamaño de la lista.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        new_node['next'] = lst['first']
        lst['first'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->addFirst: ')

def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
     el apuntador a la útima posición.
    Se incrementa el tamaño de la lista en 1
    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        lst['first'] = addLastNode(lst['first'], element)  # delegacion al nodo 'first' aplicando Recursion
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->addLast: ')

def isEmpty(lst):
    """ Indica si la lista está vacía
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['first'] is None
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->isEmpty: ')

def size(lst):
    """ Informa el número de elementos de la lista.
    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return sizeNode(lst['first'])       # delegacion al nodo 'first' aplicando Recursion
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->size: ')

def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.
    Se utiliza la función de comparación utilizada durante la creación
    de la lista para comparar los elementos.
    La cual debe retornar cero en caso de que los elementos sean iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        if isEmpty(lst):
            return 0
        else:
            return isPresentNode(lst['first'], element, lst['cmpfunction'])  # delegacion al nodo 'first' aplicando Recursion
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->isPresent: ')

##Practica

def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia de forma recursiva.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        #TODO
        pass
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->lastElement: ')

def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista de forma recursiva.

    Se recorre la lista hasta el elemento pos, el cual  debe ser
    mayor que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        #TODO
        pass
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->getElement: ')

def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista de forma recursiva.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista.
    La lista no puede estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        #TODO
        pass
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->deleteElement: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista recursivamente.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        #TODO
        pass
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->insertElement: ')

def reverseList(lst):
    """ Cambia el sentido de la lista de forma recursiva, invirtiendo el orden de sus elementos
    Args:
        lst: La lista en la que se va a invertir
    Raises:
        Exception
    """
    try:
        #TODO
        pass
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->reverseList: ')

# _____________________________________________________________________
#            Funciones de Recursion
# _____________________________________________________________________
   



def addLastNode(nodo, element):
    """
    Agrega un elemento al final de la lista (algoritmo RECURSIVO).
    Args:
        nodo: nodo de inicio de sublista
        elemento: alemento a agregar al final
    Returns:
        El nodo de inicio de la lista que ya tiene el nuevo elemento
        El nodo que es final de la lista
    Raises:
        Exception
    """
    try:
        if nodo is None:
            return node.newSingleNode(element)
        else:
            nodo['next'] = addLastNode(nodo['next'], element)  # aplicancion de Recursion al nodo['next']
            return nodo
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist:addLastNode')

def sizeNode(nodo):
    """
    Retornar el número de elementos en la a partir un nodo dado (algoritmo RECURSIVO)
    Args:
        nodo: nodo de inicio de la sublista
    Returns:
        El número de elementos en la lista
    Raises:
        Exception
    """
    try:
        if nodo is None:
            return 0
        else:
            return 1 + sizeNode(nodo['next'])  # aplicancion de Recursion al nodo['next']
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist:sizeNode')

def isPresentNode(nodo, element, cmpfunction):
    """
    Buscar si el elemento esta presenta en la lista que empieza en el nodo (algoritmo RECURSIVO).
    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.

    Args:
        nodo: Primer nodo de la lista a recorrer
        element: elemento de busqueda
        cmpfunction: funcion de comparacion de elementos
    """
    try:
        if nodo is None:
            return 0
        elif cmpfunction(nodo['info'], element) == 0:
            return 1
        else:
            pos_sublist = isPresentNode(nodo['next'], element, cmpfunction)  # aplicancion de Recursion al nodo['next']
            if pos_sublist != 0:
                return 1 + pos_sublist
            else:
                return 0
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist:isPresentNode')


def defaultfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1

def compareElements(cmpfunction, key, element, info):
    """ Compara dos elementos

    Se utiliza la función de comparación por defecto si key es None
    o la función provista por el usuario en caso contrario
    Args:
        cmpfunction: funcion de comparacion de los elementos
        element:  El elemento que se esta buscando en la lista
        info: El elemento de la lista que se está analizando

    Returns:  0 si los elementos son iguales

    Raises:
        Exception
    """
    try:
        if key is not None:
            return cmpfunction(element[key], info[key])
        else:
            return cmpfunction(element, info)
    except Exception as exp:
        error.reraise(exp, 'recursivesinglelinkedlist->compareElements')
