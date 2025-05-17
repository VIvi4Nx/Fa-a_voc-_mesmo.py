valorCompra = float(input("Insira o valor total da compra:R$"))
parcela = int(input("Quantas parcelas o cliente deseja parcelar: "))
prestacoes = valorCompra/parcela
print (f"Sua compra:R${valorCompra} Você parcelou de {parcela} vezes.Cada prestação:R$ {prestacoes:.2f}")