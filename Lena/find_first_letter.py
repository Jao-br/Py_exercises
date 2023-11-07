# Split and captalize Program 


def capitalize_first_letters(frase):
    str = frase.split()
    first_letters = [str[0].upper() for str in str]
    return first_letters

frase = input("Digite a frase: ")
result = capitalize_first_letters(frase)
print(f"As letras iniciais são: {result}")