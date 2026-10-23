import requests
import pandas as pd

lista_prospectos = []

print("Iniciando recolección masiva de prospectos...")

for viaje in range(5):
    respuesta = requests.get("https://randomuser.me/api/")
    paquete_datos = respuesta.json()
    
    nombre = paquete_datos["results"][0]["name"]["first"]
    apellido = paquete_datos["results"][0]["name"]["last"]
    email = paquete_datos["results"][0]["email"]
    
    contacto = {"Nombre": nombre, "Apellido": apellido, "Email": email}
    lista_prospectos.append(contacto)
    
    print("Prospecto capturado con éxito:", nombre, apellido)

tabla_final = pd.DataFrame(lista_prospectos)

tabla_final.to_csv("pipeline_prospectos.csv", index=False)

print("\nPipeline finalizado. Revisa tu barra lateral, se creó el archivo pipeline_prospectos.csv")