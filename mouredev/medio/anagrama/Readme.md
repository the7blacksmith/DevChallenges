# [Mouredev {Retos de programación}](https://retosdeprogramacion.com/ejercicios/)

![Goal](/Images//mouredev_anagrama.png)


### Algunos comentarios

Interesante ejercicio de nivel intermedio que pone a prueba el pensamiento algorítmico, (yo he acabado echando humo 🤯). No obstante, he encontrado una solución, que aunque no era la más eficiente, sí conseguía resolvía el ejercicio.

### Más fácil de lo que parece 😉

Si se estudia un poco y se conocen las posibilidades del lenguaje (**python**), hay una manera muy sencilla de resolver el ejercicio que es usando la función de python sorted() de la siguiente manera:

def anagrama(palabra_1: str, palabra_2: str) -> bool:
    
    if palabra_1 == palabra_2:
        return False
    return sorted(palabra_1) == sorted(palabra_2)

En mi caso, pese a que he pasado bastantes horas estudiando python, he sido incapaz de llegar a esa conclusión simple, **pero no hay nada como equivocarse para aprender.**

### ChatGPT

Aquí os dejo lo que dice nuestro mejor amigo, ChatGPT, de sorted() y ya de paso del método .sort() para que también podáis sacarle rendimiento.

**sorted()**

sorted() es una función incorporada en Python que sirve para ordenar de manera ascendente o descendente los elementos de una lista, cadena, tupla, o cualquier iterable, y devuelve una nueva lista ordenada.

Aquí tienes un ejemplo simple:

lista = [3, 1, 4, 1, 5, 9]
ordenada = sorted(lista)
print(ordenada)  # Output: [1, 1, 3, 4, 5, 9]
Puedes también usar el parámetro reverse=True para ordenar de forma descendente:

descendente = sorted(lista, reverse=True)
print(descendente)  # Output: [9, 5, 4, 3, 1, 1]

Así que, aunque sorted() es una función, algunos objetos como las listas tienen el método **.sort()**, que ordena la lista en su lugar y no devuelve una nueva.



