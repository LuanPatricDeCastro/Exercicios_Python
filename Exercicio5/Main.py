# Faça um Programa que converta metros para centímetros.

print('O objetivo deste programa é converter metros');
metros = float(input('Informe o valor em metros: '));
while(metros < 0):
    print('Não existe quantidade em metros negativa: ');
    metros = float(input('Informe o valor em metros: '));

conversaoCentimetros = metros * 100;
conversaoCentimetros = round(conversaoCentimetros, 2);
print(f'O valor em metros corresponde a: {conversaoCentimetros} centimetros');