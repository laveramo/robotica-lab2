# robotica-lab2
## 1. Diagrama del robot Phantom X y sus parámetros DH
A continuación podemos observar el diagrama del Phantom X donde podemos observar las medidas, se tuvo en cuenta además una distancia de 45mm entre la primera y segunda articulación (De abajo hacia arrabo)

![Diagrama](diagrama-1.png "Diagrama")

A continuación podemos observar los marcos coordenados para los parametros de Denavit-Hartenber.

![Marcos](robot-dh.png "Marcos")

Donde se obtienen la siguiente tabla con los parametros de Denavit-Hartenvber y su respectivo ploteo en Matlab

![Tabla](tabla-dh.png "Tabla")

## 2. Conexión con ROS
### Procedimiento
1. Se realizó el script *mov_px.py* ubicado en *px_robot/scripts/* permite mover las juntas del robot de la siguiente forma:
- La tecla 'w' permite seleccionar la siguiente junta: si se está en la junta 1 (waist) se pasa a la junta 2 (elbow).
- La tecla 's' permite seleccionar la junta anterior.
- La tecla 'a' lleva la junta seleccionada a su posición de home.
- La tecla 'd' lleva la junta seleccionada a una posición deseada (ingresada por consola), la cual está en enteros donde 0 es el valor mínimo y 1023 la posición máxima del motor.

2. Para lograr la lectura de las teclas se crea la función getKey() tomada de [5].
3. Se creó la función `actions()` la cual decide la acción a realizar según la tecla oprimida.
4. Para el movimiento de las juntas se importó la función `jointCommand()` del script *jointSrv.py* el cual permite llamar al servicio *dynamixel_command*. De esta forma se puede usar `jointCommand()` para
###Análisis
## 3. Uso del TCP
### Procedimiento
### Análisis

## 4. MATLAB + ROS + TCP


Video demostrativo: https://youtu.be/5YeRemsvWN0
### Procedimiento
### Análisis
## Conclusiones
## Referencias
[5] [Python for fun: Get Key Pressed in Python](http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html)
