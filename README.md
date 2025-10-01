# Primeros, siguientes y predicciones
Este programa en Python analiza gramáticas libres de contexto calculando tres conjuntos fundamentales en el análisis sintáctico predictivo; siendo estos los conjutnos primeros, siguientes y los de predicción que se dan de una serie de reglas y los imprime de acuerdo a la gramatica ingresada.

# Estructura
-main.py

-gramatica1.txt

-gramatica2.txt


Hay un archivo Python "main" que es donde se ejecuta el programa, y 2 archivos de texto "gramatica#", que son los archivos de prueba que contienen las gramaticas a utilizar (de los ejercicios de la presentacion 6).

# Explicación
Al ejecutar el main.py, este nos mostrara un mensaje para ingresar una gramatica, una vez se escriba el nombre del archivo de texto con la gramatica a utilizar, este pasar por una funcion de leer garmatica donde el contenido del archivo de texto se guardara en un diccionario, que sera la gramatica a utilizar, en el archivo de texto esta definida la gramatica con las reglas que sigue de los terminales y los NO terminales, en el diccionario los NO terminales seran las claves y los terminales los valores de esas claves de la misma forma en como se definieron las reglas, y si un NO terminal produce la palabra vacio, esta se tomara como un epsylon ε. (importante que en la gramatica para definir, se escribe tal cual 'vacio' para representar ε).

Una vez ya con la gramatica, se separa su contenido entre simbolo principal o el no terminal que se usara en la primera regla, y los propios no terminales y terminales para usar aparte en los algoritmos a trabajar.

El primer algoritmo por el que se pasa es de primero, utilizando la gramatica y los terminales, calcula los conjuntos de primeros para cada simbolo de la gramatica, estos conjuntos contienen los terminales que pueden aparecer al inicio de la derivación de un No terminal, o el propio terminal si es el primero de un terminal, si uno de los simbolos analizados es un NO terminal, entonces se analiza su producción recursivamente, o si una producción deriva de ε, se añade el ε al conjunto, es importante los conjuntos primeros de cada simbolo para su uso en el proximo algoritmo (Aunque en la salida solo se mostrara los primeros de los NO terminales).

Pasando al segundo, es el algoritmo de los siguientes para cada no terminal, este utiliza los primeros, el simbolo inicial que se definio antes y la propia gramatica, estos contienen todos los simbolos NO terminales que pueden aparecer despues de un NO terminal en algúna derivacion, este simbolo inicial se añade como $ siendo un fin de cadena; el algoritmo va recorriendo producciones buscando no terminales y se actualiza el conjunto segun los simbolos que vienen despues.

El tercer y ultimo a pasar es de las predicciones, utiliza todos los primeros y siguientes NO terminales generados para construir los conjuntos de predicción para cada regla de producción(misma del archivo ingresado), esto ayuda a construir un diccionario donde cada conjunto indica con que simbolos puede empezar esa produccion.

Y finalmente una vez pasado por todos los algoritmos, el programa imprime cada uno de estos , y predecir de esta manera como se puede construir una cadena para dicha gramatica.

# Pruebas y resultados
En las pruebas de este algoritmo, se uso 2 gramaticas diferentes, pero usando NO terminales y terminales iguales, pero con reglas definidas de distintas maneras, y comprobando que la salida mostrara los primeros, siguientes, y predicciones de producción para la gramatica (dependiendo cual se ingresa), ejemplo en parte de la salida generada tiene esta estructura:

 Primeros:
 
  Primero(S)= {'seis', 'ε', 'cinco', 'tres'}

  Primero(B)= {'ε', 'cinco', 'seis'}
  
  |
  
  ....

Siguientes:

  Siguiente(S)= {'$', 'uno'}

  Siguiente(A)= {'$', 'uno', 'dos'}

  |

  ...

Conjuntos de prediccion:

S -> S A uno {'uno', 'seis', 'cinco', 'tres'}

S -> A {'$', 'uno', 'tres', 'cinco', 'seis'}

  |
  
  ...

**EJEMPLO EXTRA**
sin embargo, tambien se probo con otro ejemplo con otra gramatica para comprobar que el programa funciona con cualquier gramatica independiente del contexto, para este nuevo ejemplo se uso una gramatica de operaciones matematicas, esta definida de esta manera

E->E opsuma T

E->T

T->T opmul F

T->F

F->id

F->num

F->pari E pard

y al probar este ejemplo con el programa, la salida fue esta:

>Primeros:
>
>Primero(E)= {'pari', 'num', 'id'}
>
>Primero(T)= {'pari', 'num', 'id'}
>
>Primero(F)= {'pari', 'num', 'id'}

>Siguientes:
>
>Siguiente(E)= {'pard', 'opsuma', '$'}
>
>Siguiente(T)= {'pard', 'opsuma', 'opmul', '$'}
>
>Siguiente(F)= {'pard', 'opsuma', 'opmul', '$'}
>

>Conjuntos de prediccion:
>
>E -> E opsuma T {'pari', 'num', 'id'}
>
>E -> T {'pari', 'num', 'id'}
>
>T -> T opmul F {'pari', 'num', 'id'}
>
>T -> F {'pari', 'num', 'id'}
>
>F -> id {'id'}
>
>F -> num {'num'}
>
>F -> pari E pard {'pari'}


Esto mismo aplicable para gramaticas que tengan recursividad por la derecha o por la izquierda, el programa es apto y funciona para cualquier gramatica siempre y cuando se defina correctamente en el archivo de texto; definiendo la asignación manualmente como -> y el ε como vacio, si no se cumplen con esas condiciones el programa no aceptara la gramatica.
