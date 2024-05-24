# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Esse programa irá calcular a média do aluno: As provas valem 100 pontos.')
nota1 = float(input('Informe a 1ª nota: '));
nota2 = float(input('Informe a 2ª nota: '));
nota3 = float(input('Informe a 3ª nota: '));
nota4 = float(input('Informe a 4ª nota: '));

mediafinal = (nota1 + nota2 + nota3 + nota4) / 4;
print(f'A sua média é: {mediafinal}');
if(mediafinal >= 70):
    print('Parabéns! Você foi aprovado!');
elif(mediafinal < 70 and mediafinal >= 40):
    print('Você está de recuperação')
else:
    print('Você foi reprovado.');