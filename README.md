# robotica-lab2
## 1. Diagrama del robot Phantom X y sus parámetros DH
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
### Procedimiento
### Análisis
## Conclusiones
## Referencias
[5] [Python for fun: Get Key Pressed in Python](http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html)
