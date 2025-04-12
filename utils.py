import re

# Número ou ponto
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


# Função para saber quais os botões no intervalo a acima 0-9 ou . para poder
# mudar o style desse botões.
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def converToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


# Verifica se é um número válido convertendo para float
def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


# Verificar sé não é o botão vazio
def isEmpty(string: str):
    return len(string) == 0
