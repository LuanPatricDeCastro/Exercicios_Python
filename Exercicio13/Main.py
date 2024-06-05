# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#     1. Para homens: (72.7*h) - 58
#     2. Para mulheres: (62.1*h) - 44.7

altura = float(input('informe sua altura em metros: '));
sexo = (input('Informe seu sexo = f (feminino) ou m (masculino): '));
while(sexo != 'f' and sexo != 'm'):
    print('Informe o sexo corretamente: ')
    sexo = (input('f (feminino) ou m (masculino):  '));
opcaosexo = sexo.upper();

if(opcaosexo == 'F'):
    pesoideal = (62.1 * altura) - 44.7;
    pesoideal = round(pesoideal, 2);
    print(f'Com base na altura o peso ideal da mulher é: {pesoideal} kg');
elif(opcaosexo == 'M'):
    pesoideal = (72.7 * altura) - 58;
    pesoideal = round(pesoideal, 2);
    print(f'Com base na altura o peso ideal do homem é: {pesoideal} kg');