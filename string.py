def inverter_string(s):
    # Inicializando a string invertida
    string_invertida = ""

    # Iterando sobre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida

# String a ser invertida
string_original = "Python é incrível!"  #alterar este valor conforme necessário

# Invertendo a string
string_invertida = inverter_string(string_original)

# Exibindo os resultados
print("String original:", string_original)
print("String invertida:", string_invertida)