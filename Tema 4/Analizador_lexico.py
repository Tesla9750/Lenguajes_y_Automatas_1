import re

# Definición de las expresiones regulares para cada tipo de token
tokens_regex = [
    ('PALABRA_CLAVE', r'\b(Define|Imprime|Prueba|Excepcion|Entero|Caracter|Entonces|Finalmente)\b'),
    ('ASIGNACION', r'='),
    ('VALOR', r'\b[0-9]+\b'),
    ('OPERADOR', r'[+\-*/]'),
    ('SIMBOLO_ESPECIAL', r'[();{}]'),
    ('COMENTARIO_LINEA', r'\/\/.*'),
    ('COMENTARIO_MULTILINEA', r'\/\*[\s\S]*?\*\/'),
    ('IDENTIFICADOR', r'\b[a-zA-Z]+\b')
]


# Función para tokenizar una cadena de entrada
def tokenizar(input_str):
    tokens = []
    pos = 0

    # Ignorar espacios en blanco al principio
    while pos < len(input_str) and input_str[pos] in [' ', '\n']:
        pos += 1

    while pos < len(input_str):
        match = None
        for token_nombre, token_regex in tokens_regex:
            regex = re.compile(token_regex)
            match = regex.match(input_str, pos)
            if match:
                valor = match.group(0)
                tokens.append((token_nombre, valor))
                pos = match.end(0)
                break
        if not match:
            raise SyntaxError('No se pudo tokenizar la entrada en la posición {}: {}'.format(pos, input_str[pos:]))

    return tokens

# Ejemplo de uso
if __name__ == "__main__":
    entrada = """
Define x = 10;
Imprime x;
""".strip()

    tokens = tokenizar(entrada)
    for token in tokens:
        print(token)
