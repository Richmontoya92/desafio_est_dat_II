import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios_dict, umbral, operacion="mayor"):
    """
    Filtra los productos de un diccionario según un umbral de precio.

    Args:
        precios_dict (dict): Diccionario con nombres de productos como claves y precios como valores.
        umbral (float): El umbral de precio para la comparación.
        operacion (str, optional): La operación de filtrado. 
                                   Puede ser "mayor" (por defecto) o "menor".

    Returns:
        dict: Un diccionario con los productos que cumplen la condición.
              Retorna un string de error si la operación no es válida.
    """
    productos_filtrados = {}
    if operacion == "mayor":
        for producto, precio in precios_dict.items():
            if precio > umbral: 
                productos_filtrados[producto] = precio
    elif operacion == "menor":
        for producto, precio in precios_dict.items():
            if precio < umbral:
                productos_filtrados[producto] = precio
    else:
        return "Operación no válida" 
        
    return productos_filtrados

# 1. Validar el número de argumentos
if not (2 <= len(sys.argv) <= 3):
    print("Uso: python filtro.py <umbral> [mayor|menor]")
    sys.exit(1) 

# 2. Obtener el umbral
try:
    umbral_venta = float(sys.argv[1])
except ValueError:
    print("Error: El umbral debe ser un número.")
    sys.exit(1)

# 3. Determinar la operación
operacion_filtro = "mayor" 
if len(sys.argv) == 3:
    operacion_parametro = sys.argv[2].lower()
    if operacion_parametro in ["mayor", "menor"]:
        operacion_filtro = operacion_parametro
    else:
        print("Lo sentimos, no es una operación válida")
        sys.exit()

productos_cumplen = filtrar_productos(precios, umbral_venta, operacion_filtro)

if isinstance(productos_cumplen, str): # Si la función retornó un mensaje de error 
    print(productos_cumplen)
elif not productos_cumplen: # Si el diccionario de resultado está vacío
    print(f"No hay productos que cumplan la condición '{operacion_filtro}' que {umbral_venta}.")
else:
    nombres_productos = ", ".join(productos_cumplen.keys()) 
    if operacion_filtro == "mayor":
        print(f"Los productos mayores al umbral son: {nombres_productos}")
    else: 
        print(f"Los productos menores al umbral son: {nombres_productos}")