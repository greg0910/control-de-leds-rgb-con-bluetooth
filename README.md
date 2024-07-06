# Control de RGB LED con Bluetooth
Este código es un ejemplo de cómo controlar un LED RGB mediante una conexión Bluetooth utilizando el módulo gpiozero, bluedot y la librería de Python time.

## Requisitos
- Raspberry Pi con conexión a Bluetooth
- LED RGB conectado a los pines GPIO 27 (rojo), 17 (verde) y 22 (azul)
- Dispositivo móvil con sistema operativo Android y la aplicación [MIT App Inventor Bluetooth Client](https://gallery.appinventor.mit.edu/?galleryid=7f10877f-c4ae-490e-91d0-147fe4064b90) instalada
## Instalación
1. Asegúrate de tener Python 3 y las librerías gpiozero, bluedot y time instaladas en tu Raspberry Pi.
2. Descarga el código en un archivo .py en tu Raspberry Pi.
3. Ejecuta el código con el comando python `nombre_del_archivo.py` en la terminal.
4. En tu dispositivo móvil, abre la aplicación RGB.apk y conéctate al servidor Bluetooth de tu Raspberry Pi.
## Uso
Una vez conectado, enviando cualquiera de las siguientes letras a través de la aplicación RGB.apk, el LED RGB cambiará su color:

- R: Rojo completo
- G: Verde completo
- B: Azul completo
- C: Cian
- M: Magenta
- Y: Amarillo
- W: Blanco
- S: Apagado
- RA: Cambia entre los colores rojo, azul, magenta, amarillo, cian y blanco antes de apagarse.
## Notas
Asegúrate de tener los pines del LED RGB conectados correctamente según el código, de lo contrario no funcionará correctamente.
