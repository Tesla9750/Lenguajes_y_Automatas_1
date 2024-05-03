# Tarea 3.2 Caso practico Autómata Finito
Los autómatas finitos son modelos matemáticos que representan sistemas computacionales o de control con un número finito de estados y transiciones entre ellos.

### Introducción - Relación de los autómatas finitos en los videojuegos:
En relación con los videojuegos, los autómatas finitos se encuentras presentes y juegan un papel fundamental dentro del diseño, desarrollo e implementación de distintas mecánicas de juego, la IA utilizada para personajes no jugadores(PNJ), sistemas de comportamiento, movimientos como saltar, correr, golpear, etc. 

Dentro de esto, en algunos videojuegos el numero de movimientos realizados por uno o varios personajes es numerosa y suele contar con distintas combinaciones, siendo que programar el comportamiento de los personajes sea cada vez mas complicado a medida que aumenta el numero de acciones realizadas. La gestión de todos los movimientos realizados es posible gracias a la implementación  de autómatas finitos. 

![-](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/399a7112e1a6d1e0013097a7f6ea1b61d2e1929c/assets/smash.jpg)

Siendo así, analizaremos el siguiente diagrama de estado que representa el patrón de comportamiento de un enemigo.
![-](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/399a7112e1a6d1e0013097a7f6ea1b61d2e1929c/assets/diagramaestadoenemigo.png)

### Estados de transición:
1.  **Buscar ayuda (find aid)**: Este es el estado inicial en el que la entidad busca ayuda médica. Cuando encuentra la ayuda, se activa la transición “found aid” y la entidad pasa al estado “wander”.
    
2.  **Vagar (wander)**: En este estado, la entidad se mueve sin un objetivo específico. Hay tres transiciones posibles desde este estado:
    
    -   Si el jugador está fuera de la vista, la entidad continúa en el estado “wander”.
    -   Si el jugador está cerca, se activa la transición “player is near” y la entidad pasa al estado “attack”.
    -   Si los puntos de salud de la entidad son bajos, se activa la transición “healthpoints are low” y la entidad vuelve al estado “find aid”.
3.  **Atacar (attack)**: En este estado, la entidad ataca al jugador. Hay dos transiciones posibles desde este estado:
    
    -   Si el jugador está inactivo, la entidad continúa en el estado “attack”.
    -   Si el jugador contraataca, se activa la transición “attacking back” y la entidad pasa al estado “evade”.
4.  **Evadir (evade)**: En este estado, la entidad intenta evitar al jugador. Desde este estado, la entidad vuelve al estado “wander” sin ninguna condición específica.

Diagrama del movimiento del PJ del jugador en un videojuego de lucha:

![-](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/399a7112e1a6d1e0013097a7f6ea1b61d2e1929c/assets/diagramajuegolucha.png)

## Conclusión: 

  
Con el análisis realizado, queda claro que los autómatas finitos son herramientas versátiles que encuentran aplicaciones en numerosos campos, incluidos los videojuegos. Su capacidad para representar sistemas con un número finito de estados y transiciones los convierte en una elección natural para gestionar una variedad de movimientos, comportamientos y mecánicas dentro del contexto interactivo de los videojuegos. Desde la implementación de IA para PNJ hasta la creación de sistemas de control de juego, los autómatas finitos desempeñan un papel fundamental en la creación de experiencias de juego ricas y dinámicas para los jugadores.
