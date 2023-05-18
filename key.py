import urllib.parse
import requests
import json
import msvcrt
import time

def millas_a_kilometros(millas):
    kilometros = millas * 1.60934
    return round(kilometros, 1)

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = input("ciudad de origen: ")
if orig.upper() == 'S' or msvcrt.kbhit() and msvcrt.getch() == b'\x1b':
     print("Finalizando codigo")
else:
  dest = input("ciudad de destino: ")
  key = "HltEsktlupGlanvOBH6RN73F8B8U0wM1"
  url = main_api + urllib.parse.urlencode ({"key": key, "from":orig, "to":dest, "locale": "es_ES"})
  json_data = requests.get(url).json()

  duracion = json_data["route"]["formattedTime"]
  horas = int(duracion.split(":")[0])
  minutos = int(duracion.split(":")[1])
  segundos = int(duracion.split(":")[2])
  segundos_a_decimal = round(segundos, 1)

  print(f"Duración del viaje: {horas} horas, {minutos} minutos, {segundos} segundos")

  narrativa = json_data["route"]["legs"][0]["maneuvers"]
  print("\nNarrativa del viaje:")
  for step in narrativa:
    lineas = step["narrative"].split('\n')
    for linea in lineas:
      distancia_a_millas = step ["distance"]
      distancia_a_kilometros = millas_a_kilometros(distancia_a_millas)
      print(f"{linea} - distancia: {distancia_a_kilometros} kilometros")
      time.sleep(1)
    distancia_a_millas = json_data["route"]["distance"]
    distancia_a_kilometros = millas_a_kilometros(distancia_a_millas)
  print(f"\nDistancia: {distancia_a_kilometros} kilometros")
      
  json_redes = json.dumps(json_data, indent=4)
#print(url)

  Salida = input("Ingrese la letra 'S' para terminar el codigo: ")
  if Salida == "S": 
      print("Terminando el codigo de viaje....")