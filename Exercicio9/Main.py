# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# - C = 5 * ((F-32) / 9).

temperaturaFahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '));

temperaturaCelsius = 5 * ((temperaturaFahrenheit - 32) / 9);
temperaturaCelsius = round(temperaturaCelsius, 2);
if(temperaturaCelsius < -273.15):
    print('A temperatura corresponde a 273.15 °C. Zero absoluto.');
else:
    print(f'A temperatura corresponde a: {temperaturaCelsius} °C');
