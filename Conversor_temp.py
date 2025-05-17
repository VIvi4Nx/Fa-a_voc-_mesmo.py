print ("####CONVERSOR DE TEMPERATURA PARA CELSIUS####")
celsius = float(input("Insira a temperatura em celsius: "))
opcao = 0
print("[1] PARA FAHREINHEIT^^")
print("[2] PARA KELVIN^^")
opcao = int(input("Escolha em qual temperatura você deseja converter: "))
if opcao ==1:
    print("você escolheu Fahreinheit^^^")
    fahreinheit = (celsius*9/5)+32
    print (f"({celsius}x 9 : 5) +32 = {fahreinheit:.2f}")
elif opcao ==2:
    print ("VOCÊ ESCOLHEU KELVIN^^^^")
    kelvin = (celsius+273.15)
    print (f"{celsius} + 273.15 = {kelvin:.2f}")