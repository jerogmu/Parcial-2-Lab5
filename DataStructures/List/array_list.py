# Funciones de TAD Lista tipo Array:
# - Creación, y manipulación.

def new_list():
    """
    Crea una lista vacía basada en arreglo.

    Returns:
        my_list: una nueva lista vacía.
        Ejemplo esperado: new_list() -> {'elements': [], 'size': 0}
    """
    my_list = {
        'elements': [],
        'size': 0
    }
    return my_list


def is_empty(my_list):
    """
    Indica si la lista no tiene elementos.

    Parameters:
        my_list (list): la lista a examinar.
    Returns:
        bool: True si la lista está vacía, False en caso contrario.
    """
    return True if my_list["size"] == 0 else False


def size(my_list):
    """
    Retorna la cantidad de elementos almacenados en la lista.
    """
    return my_list["size"]


def add_first(my_list, element):
    """
    Agrega 'element' al inicio de la lista.

    Parameters:
        my_list (list): la lista sobre la que se agrega.
        element (Any): el elemento a agregar.
    Returns:
        my_list: la lista actualizada.
    """
    actual = None
    new = None
    if size(my_list) == 0:
        my_list["elements"].append(element)
    else:
        for i in range(0,size(my_list)):
            if i > 0:
                actual = my_list["elements"][i]
                my_list["elements"][i] = new
                new = actual
            elif i == 0:
                new = my_list["elements"][i]
                my_list["elements"][0] = element
        my_list["elements"].append(new)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    """
    Agrega 'element' al final de la lista.
    """
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def add_element(my_list, element, pos):
    """
    Inserta 'element' en la posición 'pos', desplazando los
    elementos que estén desde esa posición en adelante.
    """
    actual = None
    new = None
    if size(my_list) == 0:
        my_list["elements"].append(element)
    elif pos == size(my_list):
        my_list["elements"].append(element)
    else:
        for i in range(0,size(my_list)):
            if i == pos:
                new = my_list["elements"][i]
                my_list["elements"][i] = element
            elif i > pos:
                actual = my_list["elements"][i]
                my_list["elements"][i] = new
                new = actual
        my_list["elements"].append(new)
    my_list["size"] += 1
    return my_list


def first_element(my_list):
    """
    Retorna (sin eliminar) el primer elemento de la lista.
    """
    return my_list["elements"][0]


def last_element(my_list):
    """
    Retorna (sin eliminar) el último elemento de la lista.
    """
    return my_list["elements"][-1]


def get_element(my_list, pos):
    """
    Retorna el elemento que está en la posición 'pos' (0-indexada).
    """
    return my_list["elements"][pos]


def delete_first(my_list):
    """
    Elimina y retorna el primer elemento de la lista.
    """
    primer_elemento = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return primer_elemento


def delete_last(my_list):
    """
    Elimina y retorna el último elemento de la lista.
    """
    ult_elemento = my_list["elements"].pop()
    my_list["size"] -= 1
    return ult_elemento


def delete_element(my_list, pos):
    """
    Elimina y retorna el elemento ubicado en la posición 'pos'.
    """
    element = my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list


def is_present(my_list, element, cmp_function):
    """
    Busca 'element' dentro de la lista usando 'cmp_function' para comparar.

    Parameters:
        cmp_function (function): función que recibe (element, elemento_de_la_lista)
            y retorna 0 si son iguales (misma convención que 'cmp' clásico).
    Returns:
        int: la posición (0-indexada) donde se encontró el elemento, o -1
             si no está presente.
    """
    resultado = -1
    for i in range(0,size(my_list)):
        valor = cmp_function(element,my_list["elements"][i])
        if valor == 0:
            resultado = i
            return resultado
    return resultado


def change_info(my_list, pos, new_info):
    """
    Cambia la información almacenada en la posición 'pos' por 'new_info'.
    """
    my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    """
    Intercambia los elementos ubicados en las posiciones 'pos1' y 'pos2'.
    """
    info2 = my_list["elements"][pos2]
    info1 = my_list["elements"][pos1]
    change_info(my_list,pos1,info2)
    change_info(my_list,pos2,info1)
    return my_list


def sub_list(my_list, pos, num_elements):
    """
    Retorna una nueva lista con 'num_elements' elementos de 'my_list',
    comenzando en la posición 'pos'.
    """
    result_list = new_list()
    for i in range(pos, pos + num_elements):
        result_list["elements"].append(my_list["elements"][i])
        result_list["size"] += 1
    return result_list

    # Algoritmos de Ordenamiento Iterativos:

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    # O(N^2)
    n = size(my_list)
    for i in range(0, n):
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
    n = size(my_list)                            # cuántos elementos tiene la lista
    if n > 1:                                    # caso base: con 0 o 1 elemento ya está ordenada, no hace nada
        mid = n // 2                             # punto medio (división entera)
        left = sub_list(my_list, 0, mid)         # copia de la mitad izquierda: mid elementos desde la posición 0
        right = sub_list(my_list, mid, n - mid)  # copia de la mitad derecha: los n - mid elementos restantes
        merge_sort(left, sort_crit)              # ordena la mitad izquierda (recursión)
        merge_sort(right, sort_crit)             # ordena la mitad derecha (recursión)
                                                 # desde aquí, left y right ya están ordenadas: falta mezclarlas

        i = 0                                    # posición actual en left
        j = 0                                    # posición actual en right
        k = 0                                    # posición donde se escribe en my_list
        while i < size(left) and j < size(right):    # mientras queden elementos en AMBAS mitades
            element_l = get_element(left, i)         # candidato de la izquierda
            element_r = get_element(right, j)        # candidato de la derecha
            if sort_crit(element_r, element_l):      # ¿el derecho va estrictamente antes que el izquierdo?
                change_info(my_list, k, element_r)   # sí: escribe el derecho en la posición k
                j += 1                               # avanza en right (ese elemento ya se usó)
            else:                                    # no (o empate): gana el izquierdo, eso lo hace estable
                change_info(my_list, k, element_l)   # escribe el izquierdo en la posición k
                i += 1                               # avanza en left
            k += 1                                   # CORREGIDO: siempre avanza, porque en cada vuelta se escribió un elemento
        while i < size(left):                        # right se acabó: copia lo que sobró de left
            change_info(my_list, k, get_element(left, i))
            i += 1
            k += 1
        while j < size(right):                       # left se acabó: copia lo que sobró de right
            change_info(my_list, k, get_element(right, j))
            j += 1
            k += 1
                                                 # solo uno de los dos while anteriores llega a ejecutarse
    return my_list                               # devuelve la misma lista, ahora ordenada


def quick_sort(my_list, sort_crit):
    quick_sort_recursive(my_list, 0, size(my_list) - 1, sort_crit)  # ordena el rango completo: de 0 a la última posición
    return my_list                                                  # devuelve la misma lista (se ordenó en sitio)


def quick_sort_recursive(my_list, lower, higher, sort_crit):
    if lower >= higher:                          # caso base: rango de 0 o 1 elemento, ya está ordenado
        return my_list
    p = partition(my_list, lower, higher, sort_crit)           # reorganiza el rango y devuelve la posición final del pivote
    quick_sort_recursive(my_list, lower, p - 1, sort_crit)     # ordena los que quedaron a la izquierda del pivote
    quick_sort_recursive(my_list, p + 1, higher, sort_crit)    # ordena los que quedaron a la derecha
                                                               # el pivote (posición p) no se toca más: ya está en su lugar


def partition(my_list, lower, higher, sort_crit):
    pivot = get_element(my_list, higher)         # el pivote es el último elemento del rango
    marker = lower - 1                           # frontera: última posición de "los que van antes del pivote" (aún ninguno)
    for actual in range(lower, higher):          # recorre el rango SIN incluir al pivote
        if not sort_crit(pivot, get_element(my_list, actual)):  # ¿el elemento actual es <= pivote?
            marker = marker + 1                  # sí: la zona de menores crece una casilla
            if actual > marker:                  # si el elemento no está ya en esa casilla...
                exchange(my_list, actual, marker)    # ...lo trae a la zona de menores
    exchange(my_list, marker + 1, higher)        # pone el pivote justo después de la zona de menores
    return marker + 1                            # devuelve la posición donde quedó el pivote
