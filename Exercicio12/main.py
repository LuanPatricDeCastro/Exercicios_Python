# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58


print("Este programa irá calcular seu peso ideal. ");
altura = float(input("Informe sua altura em metros: "));
pesoatual = float(input("Informe seu peso atual em Kg: "));

pesoideal = (72.8 * altura) - 58;
pesoideal = round(pesoideal, 2)

print(f"O seu peso ideal é: {pesoideal}");
if(pesoatual > pesoideal):
    diferencapeso = pesoatual - pesoideal;
    diferencapeso = round(diferencapeso, 2);
    print(f"Você está com um sobrepeso de {diferencapeso} kg ");
else:
    diferencapeso = pesoideal - pesoatual;
    diferencapeso = round(diferencapeso, 2);
    print(f'Você pode engordar {diferencapeso} kg')