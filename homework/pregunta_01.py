'''
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
'''
import pandas as pd
import re

def pregunta_01():
    # Leer el archivo línea por línea
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Extraer las columnas de la primera línea
    columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
    
    # Lista para almacenar las filas procesadas
    data = []
    
    # Variables temporales para construir filas
    current_cluster = None
    current_cantidad = None
    current_porcentaje = None
    current_keywords = ""
    
    # Patrón para detectar números
    number_pattern = re.compile(r'\d+')
    
    # Procesar las líneas
    for line in lines[4:]:  # Omitimos las primeras 4 líneas que son el encabezado
        line = line.rstrip()
        if not line:
            continue
        
        parts = line.split()
        
        # Si la primera parte es un número, es el inicio de un nuevo cluster
        if number_pattern.match(parts[0]):
            # Guardamos el cluster anterior si ya hay datos acumulados
            if current_cluster is not None:
                data.append([
                    current_cluster,
                    current_cantidad,
                    current_porcentaje,
                    current_keywords.strip().strip('.').lstrip('% ')
                ])
            
            # Nuevo cluster
            current_cluster = int(parts[0])
            current_cantidad = int(parts[1])
            current_porcentaje = float(parts[2].replace(',', '.').replace('%', ''))
            current_keywords = " ".join(parts[3:])
        else:
            # Continuación de las palabras clave
            current_keywords += " " + " ".join(parts)
    
    # Agregar la última fila
    if current_cluster is not None:
        data.append([
            current_cluster,
            current_cantidad,
            current_porcentaje,
            current_keywords.strip().strip('.').lstrip('% ')
        ])
    
    # Crear el DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Limpiar espacios múltiples en las palabras clave y remover cualquier punto final o caracteres extraños
    df["principales_palabras_clave"] = df["principales_palabras_clave"].apply(lambda x: re.sub(r'\s+', ' ', x))
    
    return df

# Ejecutar la función y mostrar el DataFrame
resultado = pregunta_01()
print(resultado)



