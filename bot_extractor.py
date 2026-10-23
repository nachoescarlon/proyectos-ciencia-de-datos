import requests

url = "https://randomuser.me/api/"

respuesta = requests.get(url)

paquete_datos = respuesta.json()

nombre = paquete_datos["results"][0]["name"]["first"]
apellido = paquete_datos["results"][0]["name"]["last"]
pais = paquete_datos["results"][0]["location"]["country"]
email = paquete_datos["results"][0]["email"]

print("Extracción de internet completada")
print("======================================")
print("Nuevo prospecto capturado:")
print("- Nombre completo:", nombre, apellido)
print("- País de residencia:", pais)
print("- Correo electrónico:", email)