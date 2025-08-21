n1 = float (input("Digite o primeiro numero? "))
op = input ("Digite a operação ( + , - , * , /)")
n2 = float (input("Digite o segundo número? "))



match op:
    case '+': 
        print (n1+n2)
    case '-':
        print (n1-n2)
    case '*' :
        print (n1*n2)
    case '/':
        if n2 == 0:
            print("nao existe divisao por 0")
        else:
            print ("o resultado é {:.1f}".format(n1/n2))
    case _:
        print ("=============")
    
