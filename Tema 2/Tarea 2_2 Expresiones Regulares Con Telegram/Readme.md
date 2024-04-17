
# Tarea 1.1. Historia y evolución de La Teoría de Autómatas y Lenguajes Formales
####  | 			 Benitez Nava Juan de Dios 			 |  21200582  | 16/04/2024  |
 Después de haber realizado sus practicas con el ejemplo de expresiones regulares y como crear un bot en telegram.
> -  Crear un hibrido de las dos practicas y modificar su bot de telegram e implementar alguna de las preguntas u opciones que tienen en el ejemplo de expresiones regulares (De preferencia crear una nueva expresión regular propuesta por ustedes).

Deben publicar su código en GitHub y documentar en el Readme con pantallas del resultado del bot.
> 
## Evidencias

 - ### Inicio - Expresiones base
	![A1](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/8cfb7911d5946492ee4269635c0390b1c6a40e14/assets/IMG-20240416-WA0005.jpg)
```python
saludo_expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
```
La primer expresión regular detecta los saludos de "hello|hi|hey|hola" para responder a ellos, además de preguntarte como te sientes mediante las expresiones : 
```python
bien_expresion_regular = re.compile(r"bien|good", re.IGNORECASE)

mal_expresion_regular = re.compile(r"mal|bad", re.IGNORECASE)
```
Ademas de una expresion para enviar un mensaje de bienvenida mediante las palabras " Conversion|conversion|convertir|conver".
```python
mensaje_conversion = re.compile(r"Conversion|conversion|convertir|conver", re.IGNORECASE)
```
 - ### Conversiones
Las expresiones que añadi fueron las siguientes :
```python
conversion_temperatura_CAF_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(celsius|c)", re.IGNORECASE)

conversion_temperatura_FAC_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(fahrenheit|f)", re.IGNORECASE)

  

conversion_distancia_KMAM_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(kilometros|km)", re.IGNORECASE)

conversion_distancia_MAKM_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(millas|mi)", re.IGNORECASE)

  

conversion_peso_KGALB_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(kilogramos|kg)", re.IGNORECASE)

conversion_peso_LBAKG_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(libras|lbs)", re.IGNORECASE)

  

conversion_velocidad_KMHAMPH_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(km/h|kph)", re.IGNORECASE)

conversion_velocidad_MPHAKMH_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(mph)", re.IGNORECASE)
```
Las cuales convierten distintas unidades de medida como lo son, Grados (Celsius y Fahrenheit), Kilómetros y Millas, Kilogramos y Libras, además de km/h y mph

![a](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/8cfb7911d5946492ee4269635c0390b1c6a40e14/assets/IMG-20240416-WA0002.jpg)
![a](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/8cfb7911d5946492ee4269635c0390b1c6a40e14/assets/IMG-20240416-WA0003.jpg)	
![e](https://github.com/Tesla9750/Lenguajes_y_Automatas_1/blob/8cfb7911d5946492ee4269635c0390b1c6a40e14/assets/IMG-20240416-WA0004.jpg)
 ## Conclusiones
En conclusión, esta practica me permitió practicar mi entendimiento y compresión de Python, además de múltiples herramientas como lo pueden ser REGEX, para la creación de las distintas expresiones regulares, además de que la implementación mediante un bot de Telegram representa un cambio dentro de las actividades que solemos tener regularmente, lo cual pudo ocasionar algunos desafíos para la creación y funcionamiento de este, sin embargo, me pareció una buena practica. 
