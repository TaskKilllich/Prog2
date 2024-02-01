Semana 1:

      Ejercicio 1
                  Diseñar un programa que, dados dos números enteros, muestre por pantalla uno de los siguientes mensajes,
                  dependiendo de la verificación de la condición que corresponda.
                  • El segundo es el cuadrado exacto del primero.
                  • El segundo es menor que el cuadrado del primero.
                  • El segundo es mayor que el cuadrado del primero.
                  
      Ejercicio 2
                  Escribir un programa que permita evaluar el polinomio x4 + x3 + 2x2 − x. Luego, escribir otro programa que solicite
                  valores de x por teclado y calcule el valor del polinomio para ellos, mostrando el resultado. Es importante tener en
                  cuenta cuál es la modularización adecuada del problema y cuál sería el criterio de parada al ingreso de datos.
                  
      Ejercicio 3
                  Realizar un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes
                  de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.
                  Siempre se debe dar el menor número de billetes posibles (para 100€ entregaría un único billete, no diez de 10€)
                  
      Ejercicio 4
                  Diseñar una función que reciba los tres coeficientes de una ecuación de segundo grado, y devuelva una lista con
                  sus soluciones reales.
                  Si la ecuación sólo tiene una solución real, devuelve una lista con dos copias de la misma. Si no tiene solución real
                  alguna o si tiene infinitas soluciones, devuelve una lista con dos copias del valor None.
                  
      Ejercicio 5
                  Diseñar y escribir una función que determine si un número natural (entero mayor que 1) es o no primo.
                  Luego escribir el programa que lea un número ingresado por teclado y, utilizando la función previamente escrita,
                  determine si es primo o no. El algoritmo deberá continuar pidiendo números, hasta que el usuario ingrese un
                  número 0. En ese caso, se debe confirmar la salida del programa, dando al usuario la posibilidad de seguir
                  ingresando números.
                  
      Ejercicio 6
                  Una palabra es alfabética si todas sus letras están ordenadas alfabéticamente. Por ejemplo: amor, chino e himno
                  son palabras alfabéticas. Diseñar un programa que lea una palabra y nos diga si es alfabética o no.
                  
      Ejercicio 7
                  Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres del alfabeto
                  por otro situado n posiciones más a la derecha. Si n = 2, por ejemplo, sustituiremos la a por la c, la b por la d, y así
                  sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la
                  letra y se sustituirá por la a y la letra z por la b. La sustitución debe aplicarse a las letras minúsculas y mayúsculas
                  y a los dígitos.
                  Diseñar un programa que lea un texto y el valor de n y muestre su versión criptográfica.
                  
      Ejercicio 8
                  Diseñar un programa que lea un texto criptográfico siguiendo la técnica descrita en el ejercicio anterior y el valor
                  de n utilizado al encriptar para mostrar ahora el texto decodificado.
                  
      Ejercicio 9
                  Diseñar una función que reciba una lista de palabras (cadenas) y devuelva, simultáneamente, la primera y la
                  última palabra según el orden alfabético.
                  
       Ejercicio 10
                  Diseñar una función que, dada una lista de nombres y una letra, devuelva una lista con todos los nombres que
                  empiezan por dicha letra.
Semana 2:

       Ejercicio 1
                  La siguiente función implementa recursivamente una comparación entre dos números naturales. ¿Cuál es esa
                  comparación? Escribir el enunciado correspondiente, algo así como: “Escriba una función recursiva que, dados
                  dos números enteros a y b, …...” y corregir el nombre de la función, eligiendo un nombre adecuado según las
                  reglas del código autodocumentado.
                  
        Ejercicio 2
                  Se puede formular recursivamente la suma de los n primeros números naturales. Diseñar una función recursiva en
                  Python que calcule la sumatoria de los n primeros números naturales, según la fórmula:
                  Ejercicio 3
                  A partir del ejercicio anterior, diseñar una función recursiva que, dados a y b, calcule: b∑i=a  i
                  
        Ejercicio 4
                  Escribir un programa que implemente un algoritmo RECURSIVO para determinar el número de bits necesarios
                  para representar un entero sin signo dado.
                  
        Ejercicio 5
                  Suponiendo que la función del Ejercicio 4 se llame cuantos_bits(n), dibujar el árbol de llamadas que muestre paso
                  a paso lo que ocurre al calcular cuantos_bits(63), incluyendo los valores que devuelve cada llamada a la función.
                  
        Ejercicio 6
                  a. Escribir un programa que calcule el máximo común divisor (mcd) de dos números n y m, utilizando el algoritmo
                  de Euclides, un método que se conoce desde la antigüedad y que se suele considerar el primer algoritmo
                  propuesto por el hombre. El algoritmo dice así:
                  Calcula el resto de dividir el mayor de los dos números por el menor de ellos. Si el resto es cero,
                  entonces el máximo común divisor es el menor de ambos números. Si el resto es distinto de cero, el
                  máximo común divisor de n y m es el máximo común divisor de otro par de números: el formado por
                  el menor de n y m y por dicho resto. (Para calcular el resto, se puede utilizar el operador %)
                  b. Hacer una traza de las llamadas a mcd para los números 1847 y 1106.
                  
        Ejercicio 7
                  Implementar las tres variantes del algoritmo para calcular la sucesión de Fibonacci vistas en clase (recursiva,
                  iterativa, por fórmula).
                  Luego escribir una función que pida un número, ejecute las tres versiones del cálculo, y para cada una de ellas
                  mida cuánto tarda la ejecución. Se recomienda calcular valores grandes de números de Fibonacci, n>30
                  Para medir tiempo de ejecución, Python cuenta con varias funciones. Investigue time(), perf_counter() y
                  process_time(), funciones del módulo time que permiten este tipo de cálculos. Elija una, y justifique por qué la
                  eligió.
                  
        Ejercicio 8
                  Definir una función recursiva, cuenta_atras(n), que recibe un número natural y cuenta hacia atrás desde ese
                  número hasta cero. Cuando llega al final de la cuenta, en vez de imprimir el 0, muestra la palabra “Despegando!”

        Ejercicio 9
                  Escriba un algoritmo para calcular los números combinatorios en forma recursiva
                  
        Ejercicio 10
                  La función circle(r) del módulo turtle permite dibujar un círculo de radio r.
                  
        Ejercicio 11 (recursivo o iterativo)
                  Hacer un damero de n x m cuadrados, cada uno de ellos de lado x.
                  Tenga en mente modularizar y utilizar las mejores técnicas vistas
                  hasta ahora.
                  ¿Puede dibujarlos en color rojo? ¿Puede solicitar al usuario de qué
                  color dibujar, dentro de un subconjunto seleccionado de colores?
                  
        Ejercicio 12 (recursivo o iterativo)
                  ¿Puede hacer un dibujo como el anterior… con triángulos? ¿Qué triángulos debería usar?
                  
         Ejercicio 13
                  Escribir el código para dibujar una curva de Koch, utilizando recursión.
                  
         Ejercicio 14
                  Escribir el programa que permita dibujar un copo de Koch.


Semana 3: 

        Ejercicio 1
                Dado un análisis de peor caso para una función que se expresa como 3n² + 10n + 6, determine si son ciertas las
                siguientes afirmaciones para cota superior, inferior y exacta, utilizando notación asintótica (O, Ω y Θ). ). Explique
                brevemente. Grafique, utilizando una planilla de cálculo, las diferentes funciones.
                a) 3n² + 10n + 6 = O(n³) d) 3n² + 10n + 6 = Ω(n³) g) 3n² + 10n + 6 = Θ(n³)
                b) 3n² + 10n + 6 = O(n²) e) 3n² + 10n + 6 = Ω(n²) h) 3n² + 10n + 6 = Θ(n²)
                c) 3n² + 10n + 6 = O(n) f) 3n² + 10n + 6 = Ω(n) i) 3n² + 10n + 6 = Θ(n)
        Ejercicio 2
                Considere el problema de la multiplicación de matrices. Para dos matrices, con dimensiones A (x, y) y B (y, z)
                donde el producto da como resultado una matriz C donde C [i,j] es el producto de la i-ésima fila de A por la j-ésima
                columna de B.
                Diseñe un algoritmo, analícelo y determine su complejidad de tiempo usando notación asintótica. Luego
                codifíquelo en Python, usando listas para las matrices, y determine la cantidad de operaciones para la
                multiplicación de matrices cuadradas (A y B de nxn), en los casos en que n vale 10, 20 y 50. Puede utilizar lineas
                adicionales en el programa para obtener estos valores.
        Ejercicio 3
                Suponga que el siguiente algoritmo se usa para evaluar el polinomio p(x)=anxn+an−1xn−1+…+a1x+a0
                p:=a0;
                xpower:=1;
                for i:=1 to n do
                xpower:=x∗xpower;
                p:=p+ai∗xpower
                end
                Conteste las siguientes preguntas
                1. ¿Cuántas multiplicaciones se hacen en el peor caso? ¿Cuantas sumas?
                2. ¿Cuantas multiplicaciones se hacen en el caso promedio?
                3. ¿Puede mejorar este algoritmo?
        Ejercicio 4
                Liste las funciones que se muestran en orden creciente,
                es decir de aquellas con menor dominación a aquellas
                con mayor dominación (o de las que crecen lento a las
                que crecen muy rápido).
                Si dos o mas son del mismo orden, indique cuales.
                Grafique las funciones usando una planilla de cálculo


        Ejercicio 5
                Para cada una de estar preguntas, responda y explique brevemente:
                a) Si demuestro que un algoritmo es, en el peor caso, O(n²), ¿es posible que sea O(n) para algunos datos?
                b) Si demuestro que un algoritmo es, en el peor caso, O(n²), ¿es posible que sea O(n) para todos los datos?
                c) Si demuestro que un algoritmo es Θ(n²) en el peor caso, es posible que sea O(n) para algunos datos?
                d) Si demuestro que un algoritmo es Θ(n²) en el peor caso, es posible que sea O(n) para todos los datos?
                e) La función f(n), definida como sigue, ¿es de orden Θ(n²)?
                f(n) =
                Algorítmica y Programación II TP Nº 3 - 2/2
                100n² si n es par
                20n²-nlog2n si n es impar

Semana 4:

        Ejercicio 1
                Una letra significa apilar() y un asterisco, desapilar() en la siguiente secuencia. Si se parte de una estructura vacía,
                ¿cómo quedará la pila luego de aplicar dicha secuencia? Y si desapilamos los valores que quedan, cuales son las
                cadenas de caracteres que se forman?
                (a) E * S U N * * A * P I Ñ * * * A , * P A * T * O
                (b) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * *
              
        Ejercicio 2
                Implementar una función que, usando el TAD Pila, devuelva una nueva pila invertida. Es decir que el elemento que
                estaba en el tope de la pila original, ahora estará abajo de todo.
              
        Ejercicio 3
                Escribir un programa que lea una secuencia de caracteres y los imprima en orden inverso, usando el TAD Pila. La
                secuencia termina al ingresar un * (asterisco).
                Analizar la eficiencia del algoritmo resultante, buscando la función que representa el código y la cota superior (peor
                caso).
              
        Ejercicio 4
                Escribir un programa que chequee si un string ingresado es un palíndromo o no, usando una pila. Nota: un
                palíndromo es una palabra o expresión que se lee igual de izquierda a derecha que de derecha a izquierda.
                Ejemplos de palíndromos
                Palabras aviva-azuza-Neuquen-sedes-salas.
                Frases Ella te da detalle - Isaac no ronca así – Añora la roña - Dábale arroz a la zorra el abad.
              
        Ejercicio 5
                Escribir un programa que valide los paréntesis de una expresión usando una pila, y devuelva “correcta” en caso de
                que los paréntesis estén correctamente utilizados, e “incorrecta” para aquellos casos en que haya un error.
                Ejemplo Resultado
                - Correcta (la expresión vacía está bien formada)           - (() Incorrecta
                - () Correcta                                               - ()) Incorrecta
                - (()(())) Correcta                                         - ((2+x)*23)/(6+x) Correcta
                - )( Incorrecta                                             - 2x+101)/12 Incorrecta
              
      Ejercicio 6
                Se les solicita escribir una función max(s) que acepta una pila de enteros s y devuelve su mayor elemento, es decir
                el entero mayor en la pila. ¿Qué hay que tener en cuenta para resolver este ejercicio?
                Resolver y calcular el orden de complejidad de la función max(s) resultante.
      Ejercicio 7
                En la siguiente secuencia, una letra significa encolar() y un asterisco, desencolar(). Mostrar la secuencia de
                valores que devuelve el método desencolar() para todos los elementos restantes de la cola, una vez que se aplicó
                la secuencia de operaciones a una cola vacía.
                (a) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * * D E L B A Ñ O * * * * * *
                (b) P A * S O P * * O * R T * U C * * A S * A *
      Ejercicio 8
                Escribir una función espejo(q) que acepte una cola de letras como parámetro y que agregue los elementos al final
                de la cola en orden inverso, formando un string “capicúa”:
                Ejemplo: a b c d → a b c d d c b a
                Considere usar una pila como estructura auxiliar.
      Ejercicio 9
                Escriba un método espejo() para extender el TAD Cola, que agregue los elementos al final de la cola en orden
                inverso, formando una cola “capicúa”.
                Resuelva y calcule el orden de complejidad de la función espejo() resultante.
                Ejemplos: a l → a l l a
                1 123 casa ( → 1 123 casa ( ( casa 123 1
                Juan Ana Paula → Juan Ana Paula Paula Ana Juan
      Ejercicio 10
                La veterinaria “No tengo hijos pero si mascotas” agrupa a un conjunto de 4 veterinarios donde se atienden
                pequeños animales. De los tres veterinarios, uno se dedica a animales exóticos y los otros, a mascotas en general.
                a) Escribir un TAD ColaDeBichitos, con los métodos nuevo_paciente, que recibe el nombre de la mascota y del
                dueño y lo encola, y un método proximo_paciente que devuelva la siguiente mascota que debe ser atendida, y la
                quite de la cola.
                b) Escribir un TAD Recepción, que contenga un diccionario con las colas correspondientes a cada veterinario, y los
                métodos nuevo_paciente que reciba el nombre de la mascota, de su dueño y del especialista, y proximo_paciente
                que reciba el nombre del veterinario que terminó de atender y devuelva el próximo paciente que está esperando a
                ese profesional.
                c) Escribir un programa que permita al usuario ingresar nuevas mascotas o indicar que un veterinario se ha
                liberado y en ese caso imprima el próximo paciente que lo está esperando.
                
Semana 5:

      Ejercicio 1
              Modificar el TAD ListaEnlazada visto en la teoría, de tal forma que:
              1. No tenga la longitud de la lista en la cabecera (quitar el atributo len)
              2. Tenga un atributo ult_nodo, que sea una referencia al último nodo de la lista. ¿Cuales son las ventajas y
              desventajas de agregar este atributo?
              3. Tenga por lo menos los siguientes métodos: __str__ , __len__ , agregar(x), indice(x)

      Ejercicio 2
              Creá un método imprimir() que extienda la clase ListaEnlazada y que imprima la lista siguiendo el mismo formato
              de las listas de Python. Utilizá para ello el método imprimeLista(nodo) definido en la teoría.
              >>> print(L1)
              [] # Si L1 está vacía
              >>> print(L1)
              [0, 2, 123] # Imprimir los valores entre corchetes, separados con comas.
              
      Ejercicio 3
              Escribí un método iguales(). Dos listas enlazadas se consideran iguales si contienen los mismos nodos (no el
              mismo objeto nodo, sino nodos con los mismos datos), en el mismo orden. Utilizá el siguiente algoritmo:
              1. Comparar el tamaño de las dos listas, si no tienen la misma longitud, es imposible que sean iguales.
              2. Si las listas son de la misma longitud, comparar cada nodo de una lista con el de la misma posición
              relativa de la otra lista.
              3. Si cualquiera de los nodos es diferente, este método debe devolver “False”.
              4. Si se terminó de chequear todos los nodos y todos son iguales, el método debe devolver “True”.
              
      Ejercicio 4
              Crear un programa que, usando el TAD definido en el Ejercicio 1, permita a un usuario administrar una lista de
              tareas pendientes. Dá la opción de elegir entre las operaciones: agregar tareas, borrar tareas o listar las tareas de
              la lista.
              Considerá lo siguiente:
              • Las tareas se agregan al final de la lista, y llevan un número de ítem de lista y una
              descripción. El número se genera automáticamente a partir del número del último elemento
              de la lista + 1.
              • Se puede borrar una tarea de cualquier lugar de la lista, utilizando el número de ítem.
              • La opción de listar muestra todas las tareas pendientes que están en la lista, en el orden en que se
              agregaron.


      Ejercicio 5
              Usando el TAD ListaEnlazada, escribí una función para intercambiar el elemento x con el elemento siguiente en la
              lista. Si x es el último elemento, la lista debe permanecer sin modificaciones.
              Ejercicio 6
              Escribí una función para mezclar dos listas enlazadas. Las listas de entrada tienen sus elementos en orden
              creciente, de menor a mayor. La lista de salida también debe quedar ordenada, pero de mayor a menor (orden
              decreciente).
              El algoritmo debería tomar tiempo lineal, según la longitud de la lista de salida, que es la suma de la longitud de
              las dos listas.
              L1 = [1, 12, 45, 46]
              L3 = [100, 80, 60, 46, 45, 40, 20, 12, 1, 0]
              L2 = [0, 20, 40, 60, 80, 100]
      Ejercicio 7
              En el Aula Virtual está definido un Tipo Abstracto de Datos llamado ListaDeAlumnos, que implementa una Lista
              Doblemente Enlazada de Alumnos, con los siguientes datos:
              Nº de Alumno, DNI, Apellido, Nombre, Código de carrera que cursa, y los finales que tiene rendidos (código de
              materia, fecha, nota).
              Se definen e implementan las siguientes operaciones para las listas de alumnos:
              • Crear una lista de alumnos, inicialmente vacía. La lista mantiene la cantidad de alumnos en un invariante.
              • Insertar un alumno en la lista, manteniendo el orden por número de alumno (legajo).
              • Borrar de la lista y devolver un alumno (el objeto), utilizando para ello el número de alumno.
              • Imprimir la lista, con los datos básicos de cada alumno
              Por otro lado, para los alumnos se definen las operaciones de creación y manejo de punteros (próximo, siguiente)
              y la impresión del alumno, incluyendo los finales que ha rendido.
              También se incluye el programa ListaDeAlumnos_carga que muestra algunas formas posibles de utilizar los
              nuevos tipos definidos.
              a) Amplía la implementación de tal manera que se pueda agregar una nueva nota de examen final (código de
              materia, fecha, nota), utilizando un método y no accediendo a la estructura, como se hace en el programa
              carga de ejemplo. Se debe validar la nota (0 -10) y que la materia exista en el diccionario de materias.
              b) Escribí un programa que, dado el TAD definido previamente, solicite un numero de alumno e imprima sus datos,
              incluyendo los exámenes rendidos y las notas obtenidas. Se debe informar si el alumno no existe en la lista.
              Para resolver los ejercicios, se puede extender el TAD con los métodos que consideres necesarios.



Semana 6:

      Ejercicio 1
              Dado el árbol de la figura, responda las siguientes preguntas:
              1. ¿Qué nodos son hojas?                 5. ¿Qué nodos son ancestros de E?
              2. ¿Cuál nodo es la raíz?                6. ¿Qué nodos son descendientes de E?
              3. ¿Quién es el padre del nodo C?        7. ¿Cual es la profundidad del nodo C?
              4. ¿Que nodos son hijos de C?            8. ¿Cual es la altura del nodo C?
             
      Ejercicio 2
            Escriba una función recursiva que devuelva la cantidad de hojas de un árbol binario.
            
      Ejercicio 3
            Escriba dos métodos NO recursivos que encuentren:
            (a) El mínimo de un ABB
            (b) El máximo de un ABB
            
      Ejercicio 4
            Dado un árbol binario, se desea determinar si es de búsqueda o no. Implemente una función que lo recorra y
            devuelva False si no es un ABB, y True si realmente lo es.
            
      Ejercicio 5
            Implemente un método para borrar un nodo de un ABB. Puede seguir los pasos de la Teoría. Cargue el árbol del
            ejemplo y verifique que el algoritmo funciona correctamente para cada uno de los tres casos.
            
      Ejercicio 6
            Escriba una función recursiva llamada imprimirRango que, dado un ABB, un valor_bajo y un valor_ alto, imprima
            en forma ordenada todos los nodos cuyos valores estén entre valor_bajo y valor_alto. La función debería visitar la
            menor cantidad de nodos posibles en el ABB.
            
      Ejercicio 7
            Escriba un programa que reciba una operación matemática, del tipo: 3+4*(6/7), en formato string, y que la cargue
            en un árbol de expresión y devuelva el resultado de dicha expresión. Para esto, deberá agregar a la clase Árbol de
            Expresión un método recursivo, llamado Evaluar.
            
      Ejercicio 8
            Implemente, usando el TAD Árbol, un programa que arme el árbol genealógico de una persona, partiendo de esa
            persona (raíz) y preguntando quién es su madre/padre. Deberá terminar con una persona cuando la respuesta, en
            cada caso, sea “no sé”. Una vez cargado el árbol, imprímalo. Puede usar el módulo que imprime árboles
            gráficamente, con las adaptaciones necesarias para que “entren” los nombres.

Semana 7: 

      Ejercicio 1
              Implementar la clase grafo, utilizando matrices de adyacencia, con los mismos métodos que se incluyeron
              para la implementación con listas de adyacencia.
              
      Ejercicio 2
              Implementar el recorrido de grafos BFS con el TAD del Ejercicio 1. ¿Se puede hacer cambiando el TAD
              solamente, sin modificar el código del BFS original? Es decir, en vez de importar del TAD grafos con listas,
              importar del TAD grafos con matriz?
              
      Ejercicio 3
              Implementar un algoritmo que calcule el grado de entrada y el grado de salida de un vértice. Calcular el
              orden de complejidad para cada uno de los programas en el TAD que utiliza listas adyacentes y para el TAD
              que utiliza matrices de adyacencia.
              Grado de salida de un vértice: es el número de aristas que empiezan en el vértice.
              Grado de entrada de un vértice: es el número de aristas que terminan en el vértice.
              
      Ejercicio 4
              Listar los vértices de un grafo que tienen grado de salida 0. Estos vértices se llaman sumideros.
              Listar los vértices del grafo que tienen grado de entrada 0. ¿Puede hacer algún comentario respecto a
              estos vértices?
              
      Ejercicio 5
              Implementar un algoritmo que convierta un grafo representado con matriz de adyacencia a un grafo
              representado con listas de adyacencia.
              
      Ejercicio 6
              Implementar un algoritmo que convierta un grafo representado con listas de adyacencia a un grafo
              representado con matriz de adyacencia.
              
      Ejercicio 7
              Transcribir el algoritmo de Dijkstra cuyo código se encuentra en la teoría, y verificar que NO funciona para
              grafos con peso negativo. Hacer una traza que muestre cual es el comportamiento del algoritmo.
              
      Ejercicio 8
              Usar el algoritmo de Floyd Warshall con el mismo grafo del Ejercicio 7, y verificar que funciona
              correctamente. Luego buscar un grafo con un ciclo negativo y verificar que NO funciona. Hacer una traza
              que muestre cual es el comportamiento del algoritmo.
              
      Ejercicio 9
              Implementar el método TopSort visto en clase en alguno de los TAD implementados para grafos (con lista de
              adyacencia o con matriz de adyacencia).
              Luego, escribir un programa que cargue los datos correspondientes al plan de estudios de la carrera APU y
              ejecute el método TopSort. El orden resultante del algoritmo, ¿es similar al estado de sus cursadas? ¿Hay
              alguna forma de variar el orden del resultado, según la carga de los datos?
              
    Ejercicio 10
            Podemos representar naturalmente las ciudades de un mapa caminero con un grafo, y hacer cálculos de
            distancia y selección de caminos, a partir de este grafo.
            Dado el plano de ciudades del noroeste del Chubut de la figura, y las dos tablas de distancias,
            (a) Usando el TAD grafo, cargar los datos correspondientes.
            (b) Ejecutar el algoritmo de Dijkstra del Ejercicio 7 e imprimir una tabla que muestre las
            distancias de Esquel a todas las otras ciudades o puntos del camino.
            (c) Ejecutar el algoritmo de Floyd Warshall del Ejercicio 8 e imprimir una tabla que muestre las
            distancias de Esquel a todas las otras ciudades o puntos del camino.
            (d) Escribir un programa que solicite una ciudad cualquiera e imprima las distancias hasta las
            otras ciudades o puntos del mapa.




