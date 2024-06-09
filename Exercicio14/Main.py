# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
#  peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesopeixes = float(input('Informe o peso dos peixes pescados:'));
while(pesopeixes < 0):
    print('Não é possível pescar uma quantidade negativa:')
    pesopeixes = float(input('Informe o peso novamente:'));
if(pesopeixes <= 50):
    print('A quantidade pescada não é passível de multa.');
else:
    excessoKg = (pesopeixes - 50);
    multa = excessoKg * 4;
    print(f'A quantidade de quilos excedentes é: {excessoKg} kg');
    print(f'O valor da multa é: R$ {multa}');