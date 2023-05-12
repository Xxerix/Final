#Integrantes: Edgar Olalde, Erika Garcia y Axel Godoy
#Descripcion: Este programa es un chat que se conecta a un servidor MQTT y permite a los usuarios comunicarse entre si


#Importaciones
import threading
import paho.mqtt.client as mqtt

# Variables
port = 1883   # se establece el puerto 1883
topic = "conversacionTeletubbies"  # Establecemos el topico

print("Sean bienvenidos al chat")   # Da la bienvenida al chat
nombre = input("Ingresa tu nombre: ")  # Pide el nombre del usuario
nombre = nombre.capitalize() # Convierte la primera letra en mayuscula


def on_connect(client, userdata, flags, rc): # Se conecta al servidor
    print("Conectado con resultado:", rc) # Muestra el resultado de la conexion
    client.subscribe(topic) # Se suscribe al topico
    client.publish(topic, f"{nombre} ha entrado al chat") # Publica el mensaje de entrada al chat

def on_message(client, userdata, msg): # Se conecta al servidor
    print(msg.topic, str(msg.payload)) # Muestra el topico y el mensaje


def receive_messages(client): # Recibe los mensajes
    client.loop_forever() # Se mantiene en un loop infinito

client = mqtt.Client() # Se crea el cliente
client.on_connect = on_connect # Se conecta al servidor
client.on_message = on_message # Se conecta al servidor con el mensaje

client.connect("44.203.147.25", port, 60) # Se conecta al servidor con la ip y el puerto.