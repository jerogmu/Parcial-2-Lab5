# Funciones de TAD Lista tipo Lista Simplemente Enlazada:
# - Creación, y manipulación.

from DataStructures.List.list_node import new_single_node


def new_list():
    """
    Crea una lista vacía basada en nodos encadenados.

    Returns:
        my_list: {'size': 0, 'first': None, 'last': None}
    """
    my_list = {
        "size":0,
        "first":None,
        "last":None
    }
    return my_list

def is_empty(my_list):
    """
    Indica si la lista no tiene elementos.
    """
    return my_list["size"] == 0

def size(my_list):
    """
    Retorna la cantidad de elementos de la lista.
    """
    return my_list["size"]

def add_first(my_list, element):
    """
    Agrega 'element' al inicio de la lista (nuevo primer nodo).
    """
    new_element = new_single_node(element)
    if not is_empty(my_list):
        actual = my_list["first"]
        my_list["first"] = new_element
        my_list["first"]["next"] = actual
    else:
        my_list["first"] = new_element
        my_list["last"] = new_element
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega 'element' al final de la lista (nuevo último nodo).
    """
    new_element = new_single_node(element)
    if not is_empty(my_list):
        my_list["last"]["next"] = new_element
        my_list["last"] = new_element
    else:
        my_list["first"] = new_element
        my_list["last"] = new_element
    my_list["size"] += 1
    return my_list

def add_element(my_list, element, pos):
    """
    Inserta 'element' en la posición 'pos' (0-indexada), recorriendo la
    lista nodo a nodo hasta llegar a esa posición.
    """
    element_node = new_single_node(element)
    if pos > size(my_list):
        return IndexError("Position out of range.")
    elif pos == 0:
        return add_first(my_list,element)
    elif pos == size(my_list):
        my_list["last"]["next"] = element_node
        my_list["last"] = element_node
        return my_list
    else:
        actual_node = my_list["first"]
        change_next = None
        for i in range(0,my_list["size"]):
            if i == pos - 1:
                change_next = actual_node
            elif i == pos:
                element_node["next"] = actual_node
                change_next["next"] = element_node
            actual_node = actual_node["next"]
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    """
    Retorna (sin eliminar) el primer elemento de la lista.
    """
    return my_list["first"]["info"]

def last_element(my_list):
    """
    Retorna (sin eliminar) el último elemento de la lista.
    """
    return my_list["last"]["info"]

def get_element(my_list, pos):
    """
    Retorna el elemento ubicado en la posición 'pos'.
    """
    if pos >= size(my_list):
        raise IndexError("Position out of range.")
    node = my_list["first"]
    i = 0
    found = False
    respuesta = None
    while i in range(0,size(my_list)) and not found:
        if i == pos:
            respuesta = node["info"]
            found = True
        node = node["next"]
        i += 1
    return respuesta

def delete_first(my_list):
    """
    Elimina y retorna el primer elemento de la lista.
    """
    if my_list["size"] == 0:
        raise IndexError("Position out of range.")
    elif my_list["size"] == 1:
        elemento = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None
    else:
        elemento = my_list["first"]
        my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return elemento.pop("info")

def delete_last(my_list):
    """
    Elimina y retorna el último elemento de la lista.
    """
    if size(my_list) == 0:
        raise IndexError("Position out of range.")
    elif size(my_list) == 1:
        elemento = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1
        return elemento.pop("info")
    else:
        element = None
        node = my_list["first"]
        previous = None
        for i in range(0,size(my_list)):
            if i == size(my_list) - 2:
                previous = node
            elif i == size(my_list) - 1:
                element = node
                my_list["last"] = previous
                previous["next"] = None
            node = node["next"]
        my_list["size"] -= 1
    return element.pop("info")

def delete_element(my_list, pos):
    """
    Elimina y retorna el elemento ubicado en la posición 'pos'.
    """
    if size(my_list) == 0:
        raise IndexError("Position out of range.")
    elif pos >= size(my_list):
        raise IndexError("Position out of range.")
    elif size(my_list) == 1:
        elemento = my_list["first"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1
        return elemento.pop("info")
    elif pos == 0:
        return delete_first(my_list)
    del_element = None
    node = my_list["first"]
    i = 0
    found = False
    previous = None
    while i in range(0,size(my_list)) and not found:
        if i == pos - 1:
            previous = node
        elif i == pos:
            del_element = node
            previous["next"] = node["next"]
            found = True
        i += 1
        node = node["next"]
    my_list["size"] -= 1
    return del_element.pop("info")

def is_present(my_list, element, cmp_function):
    """
    Busca 'element' recorriendo la lista y usando 'cmp_function' para
    comparar. Retorna la posición (0-indexada) o -1 si no está presente.
    """
    resultado = -1
    node = my_list["first"]
    for i in range(0,size(my_list)):
        if cmp_function(element,node["info"]) == 0:
            resultado = i
            return resultado
        node = node["next"]
    return resultado

def change_info(my_list, pos, new_info):
    """
    Cambia la información del nodo ubicado en la posición 'pos'.
    """
    if size(my_list) == 0:
        raise IndexError("Position out of range.")
    elif pos >= size(my_list):
        raise IndexError("Position out of range.")
    i = 0
    found = False
    node = my_list["first"]
    while i in range(0,size(my_list)) and not found:
        if i == pos:
            node["info"] = new_info
            found = True
        node = node["next"]
        i += 1
    return my_list

def exchange(my_list, pos1, pos2):
    """
    Intercambia la información de los nodos en las posiciones 'pos1' y
    'pos2'.
    """
    if size(my_list) == 0:
        raise IndexError("Position out of range.")
    elif size(my_list) == 1:
        raise IndexError("Position out of range.")
    node = my_list["first"]
    for i in range(0,size(my_list)):
        if i == pos1:
            change1 = node
        if i == pos2:
            change2 = node
        node = node["next"]
    temp = change1["info"]
    change_info(my_list,pos1,change2["info"])
    change_info(my_list,pos2,temp)
    return my_list

def sub_list(my_list, pos, num_elements):
    """
    Retorna una nueva lista encadenada con 'num_elements' elementos de
    'my_list', comenzando en la posición 'pos'.
    """
    new = new_list()
    node = my_list["first"]
    for i in range(0,size(my_list)):
        if i >= pos and i < pos + num_elements:
            element = node["info"]
            add_last(new,element)
        node = node["next"]
    return new

    # Algoritmos de Ordenamiento Iterativos:

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    n = size(my_list)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            element_j = get_element(my_list, j)
            element_min = get_element(my_list, min_index)
            if sort_crit(element_j, element_min):
                min_index = j
        exchange(my_list, i, min_index)
    return my_list

def insertion_sort(my_list, sort_crit):
    # O(N^2)
    n = size(my_list)
    for i in range(0, n):
        j = i
        if i > 0:
            k = i - 1
            is_sorted = False
            while is_sorted is False and k != -1:
                element = get_element(my_list, j)
                comparison = get_element(my_list, k)
                if sort_crit(element, comparison):
                    exchange(my_list, j, k)
                    j -= 1
                    k -= 1
                else:
                    is_sorted = True
    return my_list

def shell_sort(my_list, sort_crit):
    # O(NLogN)
    n = size(my_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = get_element(my_list, i)
            j = i
            while j >= gap and sort_crit(temp, get_element(my_list, j - gap)):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2
    return my_list

    # Algoritmos de ordenamiento recursivo.

def merge_sort(my_list, sort_crit = default_sort_criteria):
    n = size(my_list)
    if n > 1:
        mid = n // 2
        left = sub_list(my_list, 0, mid)
        right = sub_list(my_list, mid, n - mid)
        merge_sort(left, sort_crit)
        merge_sort(right, sort_crit)
        
        i = 0
        j = 0
        k = 0
        while i < size(left) and j < size(right):
            element_l = get_element(left, i)
            element_r = get_element(right, j)
            if sort_crit(element_r, element_l):
                change_info(my_list, k, element_r)
                j += 1
            else:
                change_info(my_list, k, element_l)
                k += 1
                i += 1
        while i < size(left):
            change_info(my_list, k, get_element(left, i))
            i += 1
            k += 1
        while j < size(right):
            change_info(my_list, k, get_element(right, j))
            j += 1
            k += 1
    return my_list
def quick_sort(my_list, sort_crit):
    quick_sort_recursive(my_list, 0, size(my_list) - 1, sort_crit)
    return my_list

def quick_sort_recursive(my_list, lower, higher, sort_crit):
    if lower >= higher:
        return my_list
    p = partition(my_list, lower, higher, sort_crit)
    quick_sort_recursive(my_list, lower, p - 1, sort_crit)
    quick_sort_recursive(my_list, p + 1, higher, sort_crit)
    
def partition(my_list, lower, higher, sort_crit):
    pivot = get_element(my_list, higher)
    marker = lower - 1
    for actual in range(lower, higher):
        if not sort_crit(pivot, get_element(my_list, actual)):
            marker = marker + 1
            if actual > marker:
                exchange(my_list, actual, marker)
    exchange(my_list, marker + 1, higher)
    return marker + 1