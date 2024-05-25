# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

print('O programa irá calcular seu salário bruto no mês: ');
mes = input('Informe o mês vigente: ');
salarioHora = float(input('Informe o valor da sua hora de trabalho: '));
while(salarioHora < 0):
    print('Não é possível receber valores negativos.');
    salarioHora = float(input('Informe o valor da sua hora de trabalho: '));

horasTrabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '));
while(horasTrabalhadas < 0):
    print('Não é possível ter horas negativas de trabalho.');
    horasTrabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '));

salarioMes = salarioHora * horasTrabalhadas;
salarioMes = round (salarioMes, 2);

print(f'No mês de {mes} você recebeu R$ {salarioMes} de salário');