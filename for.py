"""for variavel in range(10):
    print(variavel)"""

"""for variavel in range(1,11):
    print(variavel)"""

"""for variavel in range(1, 12, 3):
    print(variavel)"""
soma = 0

for i in range (1,4):
    nota = float(input(f'Informe a sua nota {i}:'))

    soma = soma + nota

media = soma /3
print(f'A media é: {media:.2f}')
