# Para doar sangue é necessário ter:

# Entre 16 e 69 anos;

# Pesar mais 50kg;

# Estar descansado - ter dormido pelo menos 06 hrs
# nas últimas 24 hrs.


idade = int(input('Qual a sua idade? '))
peso = int(input('Quanto você pesa? '))
sono = int(input('Quantas horas você dormiu? '))

if idade >= 16 and idade < 69 and peso >= 50 and sono >= 6:
    print('Parabéns! Você está apto para doar sangue, ajude uma vida!')
else:
    print('Você não cumpre os requesitos para doar sangue, tente uma próxima vez outra hora.')