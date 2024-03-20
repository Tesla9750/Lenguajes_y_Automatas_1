# Expresiones Regulares (Regex o Regexp)
Las expresiones regulares, también conocidas como regex o regexp, no son mas que secuencias de caracteres que definen patrones de búsqueda dentro de un texto. Con ellas, es posible encontrar, filtrar y manipular cadenas de caracteres de manera eficiente y precisa. 
Ademas
- Pueden incluir caracteres literales y metacaracteres que representan clases de caracteres, repeticiones y otras reglas.

### Ejemplos de Filtrado:
Supongamos que deseamos extraer todas las direcciones de correo electrónico de un texto. Podemos utilizar la siguiente expresión regular para lograrlo:

    \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b

Esta expresión regular busca patrones que coincidan con la estructura típica de una dirección de correo electrónico. Descomponiendo la expresión:

-   `\b`: Marca el inicio de una palabra.
-   `[A-Za-z0-9._%+-]+`: Coincide con uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentaje y signos más y menos antes del símbolo "@".
-   `@`: Coincide con el símbolo "@".
-   `[A-Za-z0-9.-]+`: Coincide con uno o más caracteres alfanuméricos, puntos y guiones bajos después del símbolo "@" (en el dominio).
-   `\.`: Coincide con el símbolo "." antes de la extensión del dominio.
-   `[A-Za-z]{2,}`: Coincide con al menos dos caracteres alfabéticos para la extensión del dominio.
-   `\b`: Marca el final de una palabra.


### Importancia:
  
Las expresiones regulares tienen una importancia significativa en el campo de la informática y la programación debido a su versatilidad y capacidad para realizar operaciones de búsqueda, filtrado y manipulación de texto de manera eficiente y precisa. Teniendo como algunos ejemplos: 
- **Validación de datos**: Útiles para verificar que una cadena cumpla un formato específico.
- - Permiten garantizar que los datos ingresados por los usuarios cumplan con un formato específico, como direcciones de correo electrónico válidas, números de teléfono en un formato determinado, códigos postales válidos, etc.
- **Búsqueda y extracción de información**: Fundamentales en análisis de logs y procesamiento de lenguaje natural. 
- - Esto es crucial en aplicaciones donde se requiere procesar grandes cantidades de datos, como análisis de registros, búsqueda en bases de datos, análisis de texto en tiempo real, etc.
- **Reemplazo de texto**: Permiten reemplazar texto basado en patrones definidos.
- - Esto es útil en aplicaciones donde se requiere procesar y transformar texto de manera automatizada.

### Casos de Uso:
1.  **Validación de Formularios**:
    
    -   En aplicaciones web, se usan para validar datos ingresados por usuarios en formularios (correo electrónico, números de teléfono, contraseñas, etc.).
    -   Ejemplo: La expresión regular  `^\d{5}$`  valida códigos postales de cinco dígitos.
2.  **Análisis de Logs**:
    
    -   En entornos de administración de sistemas, se utilizan para analizar registros de eventos y diagnosticar problemas en servidores y aplicaciones.
    -   Ejemplo: La expresión regular  `ERROR: (.*)`  busca líneas de registro que comiencen con “ERROR:” y captura el mensaje de error.
3.  **Procesamiento de Texto**:
    
    -   Se usan para limpiar datos, transformar texto y analizar datos.
    -   Ejemplo: Reemplazar todas las letras “a” con un guion “-” en una cadena de texto.
4.  **Web Scraping**:
    
    -   Para extraer información específica de la estructura HTML de páginas web.
    -   Ejemplo: La expresión regular  `<a\s+(?:[^>]*?\s+)?href="([^"]*)"`  extrae enlaces.

## Conclusión: 

En general las expresiones regulares son una herramienta poderosa y versátil en el ámbito de la informática y el procesamiento de texto. Su capacidad para definir patrones de búsqueda y manipular texto de manera eficiente las convierte en una herramienta indispensable en una amplia variedad de aplicaciones y escenarios. Su importancia es enorme, ya que permiten buscar en grandes cantidades de datos de forma precisa, superando las limitaciones del típico buscador Ctrl+F. Además, ofrecen una gama de herramientas más amplia y pueden ser utilizadas en entornos más complejos, como el manejo de archivos CSV.

### Bibliografía: 
_Expresiones regulares_. (n.d.). https://cs.famaf.unc.edu.ar/~hoffmann/md18/10.html

Studocu. (n.d.). _Expresiones regulares - INSTITUTO TECNOLÓGICO DE CANCÚN. CARRERA: INGENIERÍA EN SISTEMAS - Studocu_. https://www.studocu.com/es-mx/document/instituto-tecnologico-de-cancun/algoritmos-y-lenguajes-de-programacion/expresiones-regulares/86347848
