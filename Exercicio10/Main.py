# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Este programa tem o objetivo de converter uma temperatura em graus Celsius para Fahrenheit.');

temperaturaCelsius = float(input('Informe a temperatura em °C: '));
if(temperaturaCelsius <=  -273.15):
    print('A temperatura informada corresponde ao zero absoluto.');
    print('Na escala Fahrenheit o zero absoluto é: -459,67')

temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;

print(f'A temperatura informada corresponde a: {temperaturaFahrenheit} °F');
