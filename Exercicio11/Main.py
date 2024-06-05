# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    1. o produto do dobro do primeiro com metade do segundo .
#    2. a soma do triplo do primeiro com o terceiro.
#   3. o terceiro elevado ao cubo.

numerointeiro1 = int(input("Informe o primeiro número inteiro: "));
numerointeiro2 = int(input("Informe o segundo número inteiro: "));
numeroreal = float(input("Informe terceiro número (Pode ser um número real): "));

print("Escolha uma das operações a seguir: ");
print(" 1 = o produto do dobro do primeiro com metade do segundo")
print(" 2 = a soma do triplo do primeiro com o terceiro")
print(" 3 = o terceiro elevado ao cubo")
escolha = int(input("Escolha uma opção: "));
if(escolha == 1):
    operacao1 = (numerointeiro1 * 2) * (numerointeiro2 / 2);
    print(f"O resultado é: {operacao1}");
elif(escolha == 2):
    operacao2 = (numerointeiro1 * 3) + numeroreal;
    print(f"O resultado é: {operacao2}");
elif(escolha == 3):
    operacao3 = numeroreal ** 3;
    operacao3 = round(operacao3, 2)
    print(f"O resultado é: {operacao3}");
else:
    print("opção inválida");