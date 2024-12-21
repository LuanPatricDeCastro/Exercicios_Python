# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#    - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    - comprar apenas latas de 18 litros;
#    - comprar apenas galões de 3,6 litros;
#    - misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

import math;

area = float(input("Informe o valor em metros da área a ser pintada: "));

areacomfolga = area * 1.1;

tintanecessaria = areacomfolga / 6;

lata_litros = 18;
galao_litros = 3.6;
preco_lata = 80;
preco_galao = 25;

latas = math.ceil( tintanecessaria / lata_litros );
preco_latas = latas * preco_lata;

galoes = math.ceil( tintanecessaria / galao_litros );
preco_galoes = galoes * preco_galao;

latas_mistura = math.floor( tintanecessaria / lata_litros );
tintarestante = tintanecessaria - latas_mistura * lata_litros;
galoes_mistura = math.ceil( tintarestante / galao_litros );
precomistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao);

print("\nOpção 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {latas} latas")
print(f"Preço: R$ {preco_latas:.2f}")

print("\nOpção 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões: {galoes} galões")
print(f"Preço: R$ {preco_galoes:.2f}")

print("\nOpção 3: Mistura de latas e galões (menor desperdício)")
print(f"Quantidade de latas: {latas_mistura} latas")
print(f"Quantidade de galões: {galoes_mistura} galões")
print(f"Preço: R$ {precomistura:.2f}")


