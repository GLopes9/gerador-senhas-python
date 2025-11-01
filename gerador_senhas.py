import random
import string
import math

def gerar_senha(tamanho=12, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("você precisa escolher pelo menos um tipo de caractere!")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def calcular_forca_senha(tamanho, tipos_caracteres):
    entropia = math.log2(tipos_caracteres ** tamanho)
    if entropia < 40:
        nivel = "Fraca"
    elif entropia < 80:
        nivel = "Média"
    else:
        nivel = "Forte"
    return entropia, nivel

# usuário interage com o gerador de senhas
print("""╔══════════════════════════╗
║ 🔐 GERADOR DE SENHAS 🔐  ║
╚══════════════════════════╝
""")

tamanho = int(input("Digite o tamanho da senha (recomenda-se um tamanho mínimo de 12 caracteres para maior segurança*): "))
usar_letras = input("Incluir letras? (s/n): ").lower() == 's'
usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
quantidade = int(input("Quantas senhas deseja gerar?: "))

senha_exemplo = gerar_senha(tamanho, usar_letras, usar_numeros, usar_simbolos)
if senha_exemplo:
    tipos = 0
    if usar_letras: tipos += len(string.ascii_letters)
    if usar_numeros: tipos += len(string.digits)
    if usar_simbolos: tipos += len(string.punctuation)
    entropia, nivel = calcular_forca_senha(tamanho, tipos)

    print(f"\nForça estimada: {nivel} (entropia ≈ {entropia:.2f} bits)\n")
    print("suas senhas:")
    for i in range(quantidade):
        print(f"{i+1}. {gerar_senha(tamanho, usar_letras, usar_numeros, usar_simbolos)}")
