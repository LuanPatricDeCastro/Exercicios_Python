# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

tamanhoarquivo = float(input('Informe o tamanho do arquivo em MB que sera baixado: '));

velocidadedownload = float(input('Informe a velocidade de download em Mbps: '));

tempodownloadsegundos = (tamanhoarquivo * 8) / velocidadedownload;

tempodownloadminutos = tempodownloadsegundos / 60;
tempodownloadminutos = round (tempodownloadminutos, 2);
print(f'O tempo de download é de aproximadamente: {tempodownloadminutos}');

