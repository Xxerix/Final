# Final
Edgar Patricio Olalde Sepulveda A01424082
Axel Godoy Barios A01425316
Erika Nohemi Garcia Martinez A01425330
​​Este es un programa de Python que implementa un cliente de chat que se conecta a un servidor MQTT, lo que permite a los usuarios comunicarse entre sí. El programa importa las bibliotecas threading y paho.mqtt.client.

El programa en primer lugar esta configurando el número de puerto en 1883 y el nombre del tema en "conversacionTeletubbies". El usuario es bienvenido al chat, se le solicita que ingrese su nombre y la primera letra de su nombre.

Después el programa define dos funciones, on_connect() y on_message(), que se utilizan para conectarse al servidor MQTT y recibir mensajes de él. La primera es función on_connect() se llama cuando el cliente se conecta con éxito al servidor y se suscribe al tema y la función on_message() se llama cuando se recibe un mensaje del tema suscrito.La función receive_messages() se usa para recibir continuamente mensajes del servidor MQTT. Se implementa mediante un bucle infinito que llama al método client.loop_forever().El programa crea un cliente MQTT y establece sus devoluciones de llamada on_connect() y on_message() a las funciones definidas anteriormente. Luego, el cliente se conecta al servidor MQTT con la dirección IP "44.203.147.25" y el número de puerto 1883. Se crea un subproceso para ejecutar la función receive_messages() en segundo plano.

Finalmente, el programa ingresa a un ciclo infinito que solicita al usuario que ingrese un mensaje y lo publica en el servidor MQTT utilizando el método client.publish(). Finalmente, el programa detiene el bucle del cliente y se desconecta del servidor.
