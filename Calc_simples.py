opcao =0
while opcao!=5:
    print ("[~~~~vBEM-VINDO A CALCULADORAv~~~~]")
    print ("[1]+PARA ADIÇÃO+")
    print ("[2]-PARA SUBTRAÇÃO-")
    print ("[3]xPARA MULTIPLICAÇÃOx")
    print ("4]:PARA DIVISÃO:")
    print ("[0] ...SAIR...")
    opcao = int(input("Escolha uma operação: "))
    if opcao ==1:
        print("+VOCÊ ESCOLHEU ADIÇÃO+")
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        soma = num1+num2
        print (f"{num1} + {num2} = {soma} ")
    elif opcao ==2:
        print("-VOCÊ ESCOLHEU SUBTRAÇÃO-")
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        subtracao = num1-num2
        print (f"{num1} - {num2} = {subtracao} ")
    elif opcao ==3:
        print("xVOCÊ ESCOLHEU MULTIPLICAÇÃOx")
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        multiplicacao = num1*num2
        print (f"{num1} x {num2} = {multiplicacao} ")
    elif opcao ==4:
        print(":VOCÊ ESCOLHEU DIVISÃO:")
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        divisao = num1/num2
        print (f"{num1} : {num2} = {divisao} ")
    elif opcao ==0:
        print("):...VOCÊ ESCOLHEU SAIR...:(")
        break