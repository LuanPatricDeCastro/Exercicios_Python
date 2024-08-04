# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areapintura = float(input('Informe o tamanho da área que será pintada: '));

quantidadelitros = areapintura / 3;
quantidadelatas = (quantidadelitros // 18) + 1;
precototal = quantidadelatas * 80;
precototal = round(precototal , 2);

print(f'A quantidade de latas necessárias: {quantidadelatas}');
print(f'Valor gasto: R$ {precototal}');
