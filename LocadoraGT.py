print ("Bem vindo a locadora GRAU T!!!!")
km_rodado = float(input("Insira os quilômetros percorridos:"))
dias = int(input("Quantos dias que o carro foi alugado? "))
valor_t = (km_rodado*0.20)+(dias*90)
print (f"Seu carro foi alugado por {dias} dias,percorreu {km_rodado} km.O valor total foi de: R$ {valor_t:.2f}")



