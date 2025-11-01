# Gerador de Senhas Python

Um gerador de senhas **seguro e personalizável** em Python. Crie senhas fortes com letras, números e símbolos em segundos!

## Funcionalidades

- Defina o tamanho da senha.
- Escolha incluir letras, números e símbolos.
- Gere múltiplas senhas de uma vez.
- Receba a **força estimada da senha** (Fraca, Média, Forte).

## Como usar

1. Execute o script:
   ```bash
   python gerador_senhas.py
Siga as instruções para escolher tamanho, caracteres e quantidade de senhas.

Veja suas senhas geradas com a força estimada.

 Força da senha:
 A força é calculada usando entropia, considerando o tamanho e variedade de caracteres:

Fraca: entropia < 40 bits

Média: 40 ≤ entropia < 80 bits

Forte: entropia ≥ 80 bits

 Tecnologias:
Python 3 (bibliotecas padrão: random, string, math)

Copiar código
Exemplo:

Digite o tamanho da senha: 12
Incluir letras? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): s
Quantas senhas deseja gerar?: 3

Força estimada: Forte (entropia ≈ 78 bits)

Senhas:
1. fG7#kL9@aB2!
2. L8m#Q2v!R1p@
3. zP3#N7b!C6q%

📄 Licença
Projeto open-source, livre para usar e modificar.
