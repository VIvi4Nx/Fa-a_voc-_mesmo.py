nome = (input("Nome do vendedor(a): "))
salarioFixo = 2000
vendas = int(input(f"Quantas vendas o vendedor(a) {nome} fez esse mês? "))
bonus = (vendas*0.15)
if vendas >=20: 
    salarioFinal = salarioFixo+bonus
    print (f"Parabéns {nome}! Você atingiu a meta.Fez {vendas} vendas,você recebeu R$ {salarioFinal} com o bônus de R${bonus}")
else :
    print (f"{nome} Você recebeu R${salarioFixo},esse mês você não bateu a meta de vendas...")