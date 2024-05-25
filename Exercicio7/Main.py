# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

ladoQuadrado = float(input('Informe o valor do lado do quadrado em centímetros: '));
while(ladoQuadrado < 0):
    print('Não existe valor negativo para o lado de uma figura geometrica.');
    ladoQuadrado = float(input('Informe o valor do lado do quadrado em centímetros: '));

valorAreaEmDobro = (ladoQuadrado * ladoQuadrado) * 2;
valorAreaEmDobro = round(valorAreaEmDobro, 2);
print(f'o dobro do valor da area é: {valorAreaEmDobro} cm²');