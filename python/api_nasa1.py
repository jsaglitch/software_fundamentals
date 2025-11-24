'''
    API: Aplication Programing Interface
    Nasa API: https://api.nasa.gov/
    API_KEY_NASA: YOUR NASA API_key
    Developer: Jaider S. Arcos
    DATE 09/11/2025
    SCRIPT DESCRIPTION: GET AND READ DATA FROM NASA API ABOUT COMENTS AND OTHERS
    https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}
'''

import requests
import os 

os.system('cls')

def get_nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"

    #Realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status() #=> Valida si se presenta algún error en la petición
    data = response.json() #convertir la respuesta a formato JSON (JS Object Notation)

    print(data)

API_KEY_NASA = 'tncRyRaGQMrRkcrkbHnKT7DR4gGs77moCR0CXBec'
