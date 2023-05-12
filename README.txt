# Final
Pato, Axel y Eri

Después de entender el funcionamiento del MQTT visto en clase de esta semana Tec, primero iniciamos una instancia desde la AWS (Amazon Web Services), activamos el mosquitto y creamos un tópico en el cual se podrán comunicar los usuarios por texto. Después de tenerlo habilitado, descargamos el MQTT Explorer desde la web para poder conectarnos a la instancia, agregamos la dirección IP dada por la instancia. Finalmente dimos de alta un nombre al tópico que lo ocuparemos durante todo el proyecto para mantener la comunicación.

Este es un programa de Python que implementa un cliente de chat que se conecta a un servidor MQTT, lo que permite a los usuarios comunicarse entre sí. El programa importa las bibliotecas threading y paho.mqtt.client.

El programa en primer lugar esta configurando el número de puerto en 1883 y el nombre del tema en "conversacionTeletubbies". El usuario es bienvenido al chat, se le solicita que ingrese su nombre y la primera letra de su nombre.

Después el programa define dos funciones, on_connect() y on_message(), que se utilizan para conectarse al servidor MQTT y recibir mensajes de él. La primera es función on_connect() se llama cuando el cliente se conecta con éxito al servidor y se suscribe al tema y la función on_message() se llama cuando se recibe un mensaje del tema suscrito.La función receive_messages() se usa para recibir continuamente mensajes del servidor MQTT. Se implementa mediante un bucle infinito que llama al método client.loop_forever().El programa crea un cliente MQTT y establece sus devoluciones de llamada on_connect() y on_message() a las funciones definidas anteriormente. Luego, el cliente se conecta al servidor MQTT con la dirección IP "44.203.147.25" y el número de puerto 1883. Se crea un subproceso para ejecutar la función receive_messages() en segundo plano.

Finalmente, el programa ingresa a un ciclo infinito que solicita al usuario que ingrese un mensaje y lo publica en el servidor MQTT utilizando el método client.publish(). Finalmente, el programa detiene el bucle del cliente y se desconecta del servidor.
