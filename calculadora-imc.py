peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))  
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
print(f"Seu IMC é: {imc:.2f}")

print("Classificação do IMC:") 