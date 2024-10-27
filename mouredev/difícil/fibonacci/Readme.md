# [Mouredev {Retos de programación}](https://retosdeprogramacion.com/ejercicios/)

![Goal](/Images/fibonacci.png)

### Algunos comentarios

 Ejercicio que ya he visto varias veces desde que empecé a estudiar Python y aunque siempre tengo una ligera idea de como encararlo, siempre tengo dudas y lo tengo que pelear. Pero primero vamos a saber un poquito más sobre esta famosa secuencia:

 Según Wikipedia:

" *En matemáticas, la sucesión de Fibonacci es una sucesión infinita de números naturales como la siguiente:*

*0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,1597...*

*La sucesión comienza con dos números naturales (dependiendo de la referencia, con 0 y 1 en ciertos casos, otras inician con 1 y 1) y a partir de estos, «cada término es la suma de los dos anteriores», es la relación de recurrencia que la define.*

*Esta sucesión fue descrita en Europa por Leonardo de Pisa, matemático italiano del siglo XIII también conocido como Fibonacci. Tiene numerosas aplicaciones en ciencias de la computación, matemática, tendencias bursátiles y teoría de juegos. También aparece en configuraciones biológicas, como por ejemplo en las ramas de los árboles, en la disposición de las hojas en el tallo, en las flores de alcachofas y girasoles, en las inflorescencias del brécol romanesco, en la configuración de las piñas de las coníferas, en la reproducción de varias especies, en la estructura espiral del caparazón de algunos moluscos, como el nautilus, dinámica de los huracanes, organización de las galaxias, proporciones del cuerpo humano, sus partes y subpartes y en cómo el ADN codifica el crecimiento de las formas orgánicas complejas.* "

Como podéis ver, la sucesión tiene cierta gracia y misterio. Tool, por ejemplo, en su canción Lateralus, usa un ritmo que sigue la sucesión Fibonacci. Parecería algo intrascendente pero, sin embargo, hay cientos de páginas que hablan sobre este disco y lo que la canción quiere decir...

Pero vamos con lo que nos interesa, que es el código:

Tengo dos versiones:

1. La función imprime una lista con la sucesión.

Como programador amateur o, al menos, como iniciado no hace mucho tiempo, la verdad es que me gusta más esta opción, la de hacer una lista. Desde mi punto de vista, la función tiene una simplicidad mayor y cierta naturalidad (supongo que la programación trata de eficiencia y de datos objetivos y no de simplicidad o naturalidad).

Mouredev, en su página, considera a este ejercicio "difícil", pero la verdad es que a mí no me parece mucho más difícil que otros ejercicios que él considera "fáciles", como en "anagrama" o en "fizz_buzz". Eso sí, aunque en los otros problemas tienes que conocer y saber utilizar conceptos básicos de programación y sintáxis, como los "loops" o el "if, else", aquí, la complejidad viene dada en la concepción del algoritmo. Tienes que pensar como se construye la secuencia y eso te obliga a usar la pizarra, aunque sea mental.

Cuando ya tenía una idea, el único desafío que me encontré fue saber parar la lista antes de que la sucesión llegue o supere el 50.  Por eso es importante poner el "break" antes que el "append(x)" y que la sucesión se ajuste a lo que se pide en el ejercicio. Así, el último número de la sucesión Fibonacci es el 34.

2. La función imprime la sucesión:

En la opción 2, la función imprime una sucesión fibonacci dejando un espacio de 0.5 segundos entre un número y el siguiente. Esto me lleva a hablar sobre la librería time y su uso time.sleep().
En Python, es básico conocer sus librerías ya que pueden facilitarnos mucho la vida; y time es una de las más importante. No porque lo diga yo, sino porque desde que empecé a estudiar, la he utilizado en varias ocasiones. Muchas para medir la eficiencia de una función.

Por eso, esto dice ChatGPT de time y particularmente de time.sleep().

" *La librería time en Python es un módulo que proporciona diversas funciones relacionadas con la manipulación del tiempo. Permite realizar tareas como medir el tiempo de ejecución de un código, obtener la fecha y hora actuales, y trabajar con temporizadores. Este módulo es útil para aplicaciones que requieren un control preciso sobre el tiempo, como la programación de eventos y la creación de intervalos de espera* 

**time.sleep()**

*La función time.sleep(segundos) es una de las funciones más utilizadas de la librería time. Su propósito es pausar la ejecución del programa durante el número de segundos especificado. Esto es especialmente útil cuando deseas introducir retrasos entre acciones, como en animaciones, pruebas, o en situaciones donde necesites esperar por recursos externos (por ejemplo, la espera entre solicitudes de red).*

*Uso básico:*

import time #Muy importante importarlo.

print("Iniciando la espera...")
time.sleep(2)  # Pausa la ejecución durante 2 segundos
print("¡Continuando después de la pausa!")

*Características de time.sleep():*

- *Precisión: El argumento puede ser un número entero o un número de punto flotante, lo que permite pausas de tiempo exactas, incluso en fracciones de segundo (por ejemplo, time.sleep(0.5) para medio segundo).*
- *Interrumpibilidad: La pausa puede ser interrumpida si el programa recibe una señal, pero la implementación de este comportamiento puede variar según el sistema operativo.*

*En resumen, time.sleep() es una herramienta muy práctica para gestionar la temporización en tus programas de Python.*"

Para terminar diré que aunque esta segunda versión que he hecho me parece más artificial y no me gusta tanto, cumple con el objetivo.

Eso sí, no olvides:

"Over thinking, over analyzing separates the body from the mind."

