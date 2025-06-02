velocidades_muestra = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4,
    2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
] 

def identificar_velocidades_sobre_promedio(lista_velocidades):
    """
    Calcula el promedio de una lista de velocidades y devuelve los índices
    de las velocidades que están por encima de ese promedio. 

    Args:
        lista_velocidades (list): Una lista de números (velocidades).

    Returns:
        list: Una lista de los índices donde la velocidad supera el promedio.
              Retorna una lista vacía si la lista de entrada está vacía.
    """
    if not lista_velocidades:
        return []

    suma_total_velocidades = 0
    for velocidad in lista_velocidades:
        suma_total_velocidades += velocidad
    
    promedio = suma_total_velocidades / len(lista_velocidades)

    indices_sobre_promedio = []
    for indice, velocidad in enumerate(lista_velocidades):
        if velocidad > promedio:
            indices_sobre_promedio.append(indice)
            
    return indices_sobre_promedio

if __name__ == "__main__":
    posiciones_alertas = identificar_velocidades_sobre_promedio(velocidades_muestra)
    
    print(posiciones_alertas)