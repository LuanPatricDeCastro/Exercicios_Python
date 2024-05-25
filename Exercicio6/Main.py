# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raioCirculo = float(input('Informe o raio do circulo em centímetros: '));
while(raioCirculo < 0):
    print('Não existe círculo com raio negativo.');
    raioCirculo = float(input('Informe o raio do circulo: '));

areaCirculo = (3.14 * raioCirculo ** 2);
areaCirculo = round(areaCirculo , 2);
print(f'A área do círculo é: {areaCirculo} cm²')