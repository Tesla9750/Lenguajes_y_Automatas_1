# Tarea 2.3  Ejercicios de Practica
####  | 			 Benitez Nava Juan de Dios 			 |  21200582  | 16/04/2024  |

- Expresión regular que valide un **Password** fuerte  
  1 minúscula  
1 mayúscula  
1 numero  
1 carácter especial  
8 caracteres de longitud

#### Expresión regular
```python
> ^(?=._?[a-z])(?=._?[A-Z])(?=._?\d)(?=._?[@$!%_?&])[A-Za-z\d@$!%_?&]{8,}$
```
- Expresión Regular que valide un **Nombre de usuario**  
Longitud de 3 a 16 caracteres  
Letra o numero o guion medio o bajo
#### Expresión regular
```python
^[a-zA-Z0-9_-]{3,16}$
```
