
# Exercicio 1 - Calculo de media
n1 = int(input('Digite o primerio numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
soma = (n1 + n2 + n3) /3
if soma >= 70:
    print('Aprovado')
elif soma >= 40:
    print('Recuperação')
else:
    print('Reprovado')
print(f'Calculando os valores {n1}, {n2} e {n3}  a media é {int(soma)}')