# O Twitter é conhecido por limitar as postagens em 280
# caracteres. Conferir se um texto vai caber em um tuíte é o
# desafio.

# Entrada:

# A entrada é uma linha de texto.

# Saída:

# A saída é dada em uma única linha. Ela deve ser TWEET se
# a linha de texto conter até 280 caracteres. Se a entrada da
# linha texto tiver mais 280 caracteres, a saída deve ser "Esse
# texto é maior que o esperado".

tweet = input('O que você está pensando hoje? ')

if len(tweet) <= 280:
  print('TWEET')
else:
  print('Esse texto é maior que o esperado.')