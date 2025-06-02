# ong.py

def factorial(n):
    """
    Calcula el factorial de un entero no negativo.
    """
    if not isinstance(n, int) or n < 0:
        return "Input must be a non-negative integer."
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def productoria(lista):
    """
    Calcula el producto de todos los elementos en una lista.
    """
    if not isinstance(lista, list):
        return "Input must be a list."
    if not lista:
        return 1 
    
    result = 1
    for num in lista:
        if not isinstance(num, (int, float)):
            return f"Error: List for productoria contains non-numeric element: '{num}'."
        result *= num
    return result

def calcular(**kwargs):
    """
    Controla el cálculo de factoriales y productorias.
    Procesa los argumentos 'fact_i' y 'prod_i' e imprime los resultados en el formato especificado.
    Permite cualquier orden y cantidad de argumentos.
    """

    processed_results = []

    sorted_keys = sorted(kwargs.keys(), key=lambda x: (x.split('_')[0], int(x.split('_')[1])) if '_' in x and x.split('_')[1].isdigit() else (x, 0))

    for key in sorted_keys:
        value = kwargs[key]
        if 'fact_' in key: 
            fact_result = factorial(value)
           
            if isinstance(fact_result, str): 
                 processed_results.append(f"Error en factorial para {key}: {fact_result}")
            else:
                 processed_results.append(f"El factorial de {value} es {fact_result}")
        elif 'prod_' in key: 
            prod_result = productoria(value)
  
            if isinstance(prod_result, str):
                processed_results.append(f"Error en productoria para {key}: {prod_result}")
            else:
                processed_results.append(f"La productoria de {value} es {prod_result}")
            
    for result_line in processed_results:
        print(result_line)


calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)