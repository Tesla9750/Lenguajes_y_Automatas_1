# Tarea 3.1 Ejercicios AFN  

  
Realizar los ejercicios acordados en clase de la  **página 49**, del libro  **Teoría de la computación de Carrión Viramontes**



## Ejercicios Tema 3 :
- **3.2 -** Para los siguientes ejercicios, construya el diagrama de transición del AFD que
acepta a cada uno de los lenguajes sobre el alfabeto Σ = { a, b }:
### a) El lenguaje donde toda cadena tiene exactamente dos bs.
|  | a | b |  
|--|--|--|
| q0 |q0 | q1 |
| q1 | q1 | q2 |
| q2 | q3 | q2 |
| q3 | q3 | q3 |
![ a ) ](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/a.png)
### b) El lenguaje de las cadenas no vacías, donde toda a está entre dos bs.
![b )](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/b.png)
|  | a | b |  
|--|--|--|
| q0 |q0  | q1 |
| q1 | q0 | q1 |
| q2 | q0 | q2 |
### c) El lenguaje donde toda cadena contiene el sufijo aba.
![c )](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/c.png)
|  | a | b |  
|--|--|--|
| q0 |q1 | q0 |
| q1 | q1 | q2 |
| q2 | q3 | q0 |
| q3 | q1 | q2 |
### d) El lenguaje donde ninguna cadena contiene las subcadenas aa ni bb.
![d ) ](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/d.png)
|  | a | b |  
|--|--|--|
| q0 |q1 | q0 |
| q1 | q3 | q2 |
| q2 | q3 | q0 |
| q3 | q3 | q0 |
### e) El lenguaje donde toda cadena contiene la subcadena baba.
![e ) ](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/e.png)
|  | a | b |  
|--|--|--|
| q0 |q1 | q0 |
| q1 | q3 | q2 |
| q2 | q3 | q0 |
| q3 | q3 | q0 |
### f) El lenguaje donde toda cadena contiene por separado a las cadenas ab y ba. *
![f ) ](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/f.png)
### g) Toda cadena es de longitud impar y contiene una cantidad par de as.*
![g )](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/7a3f908136545974e86e623a2b3fd7a6892d3089/assets/g.png)

