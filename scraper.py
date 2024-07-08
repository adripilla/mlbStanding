import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL de la página de clasificaciones de MLB
url = 'https://www.mlb.com/standings/'

# Hacer la solicitud a la página web
try:
    response = requests.get(url)
    response.raise_for_status()  # Lanzar error si la solicitud falla
    print("Solicitud HTTP exitosa")
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
    exit()

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la tabla de clasificaciones
standings_table = soup.find('table', class_='tablestyle__StyledTable-sc-wsl6eq-0 cprRUf StandingsTablestyle__DataTableWrapper-sc-1l6jbjt-1 kCeyFZ auto-scroller')

if not standings_table:
    print("No se encontró la tabla de clasificaciones")
    exit()

# Extraer los datos de la tabla
rows = standings_table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all(['th', 'td'])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Guardar los datos en un objeto JSON
json_data = json.dumps(data, indent=4)

# Escribir los datos en un archivo JSON
json_file = 'mlb_standings.json'
with open(json_file, 'w', encoding='utf-8') as file:
    file.write(json_data)

print(f"Datos guardados en {json_file}")
