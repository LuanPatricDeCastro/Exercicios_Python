# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#    1. salário bruto.
#    2. quanto pagou ao INSS.
#    3. quanto pagou ao sindicato.
#    4. o salário líquido.
#    5. calcule os descontos e o salário líquido, conforme a tabela abaixo: Obs.: Salário Bruto - Descontos = Salário Líquido.


horastrabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '));
while(horastrabalhadas < 0):
    horastrabalhadas = float(input('Informe novamente: '));

salariohora = float(input('Qual o seu salário hora? '));
while(salariohora < 0):
    print('Não existe salário negativo.');
    horastrabalhadas = float(input('Informe novamente seu salário hora: '));

salariobruto = salariohora * horastrabalhadas;
impostoderenda = 0.11 * salariobruto;
descontoinss = 0.08 * salariobruto;
descontosindicato = 0.05 * salariobruto;
salarioliquido = salariobruto - (impostoderenda + descontoinss + descontosindicato);

print(f'O salário bruto do mês foi de: R$ {salariobruto}.');
print(f'Você pagou R$ {descontoinss} de INSS.');
print(f'Sua contribuição sindical foi de R$ {descontosindicato}.');
print(f'Seu desconto em folha de imposto de renda foi de R${impostoderenda}.');
print(f'Seu salário líquido foi de R$ {salarioliquido}.');