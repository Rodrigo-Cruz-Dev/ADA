"""x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"
else:
    resp1 = "positivo"
    
if x % 2 ==0:
    resp2 = "par"
else:
    resp2 = "impar"
    

print("O número {} é {} e {}.".format(x, resp1, resp2))"""

"""n = 20
resultado = 0

for cont in range(n):
    resultado += 1 / (2 ** cont)

print(resultado)"""

"""n = 1000
resultado = 0.0

for cont in range(n):
    resultado += 1 / (2 ** cont)
    if cont % 100 == 0:  # Imprimir a cada 100 iterações
        print(f'Intermediário: cont = {cont}, resultado = {resultado}')

print(f'Resultado final: {resultado}')"""

"""n = 1000
resultado = 0.0

for cont in range(n):
    resultado += 1 / (2 ** cont)

print(resultado)"""

"""for _ in "let's code":
  print("Olá, mundo!")"""

animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))
n = int(input("Digite um número: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f'O fatorial de {n} é {fatorial}')