#calculadora basica em python

#print de boas vindas
print(" ____________________________________________")
print("(ola seja bem vindo, vamos calcular juntos!!!)")
print(" (__________________________________________)")
print("┻┳┻┳|       V")
print("┻┳┻┳|―-∩")
print("┳┻┻┳|　　ヽ")
print("┻┳┻┳|　●   |")
print("┳┻┻┳|▼) _ノ")
print("┻┳┻┳|￣　)")
print("┳┻┳ﾐ(￣  ／")
print("┻┳┻┳")
print("┻┳┻┳T￣")
print("┻┳┻┳|")
print(" ")
print(" ")

#def é um comando de função, no exemplo a baixo foi criado uma função chamada menu com opcoes de +-*/
def menu():
    print(" ")
    print("~~~~menu~~~~")
    
    print("1| para somar")
    print("2| para subtrair")
    print("3| para multiplicar")
    print("4| para dividir")
    print(" ")
    #nessa variavel a baixo estamos deixando o usuario escolher a opção desejada
    var=int(input("digite o numero correspondente á opção escolhida: "))
    print(" ")
#if(se) elif(vai depois do primeiro if) e else(se não) o sinal == é um comparativo
#é como dizer se var for igual a 1 chame a função soma, se for igual a 2 chame a função subtrair e assim por diante
    if var==1:
        soma()
    elif var==2:
        subtrair()
    elif var==3:
        multiplicar()
    elif var==4:
        dividir()    
    else:
        print("opção invalida")

#essa é a função soma, ela que ira somar os dois numeros digitados anteriormente
def soma():
    num1=float(input("escolha o primeiro numero: "))    
    num2=float(input("escolha o primeiro numero: "))
    resultado=str(num1+num2)
    print("o resultado é: " + resultado)
#apos o resultado deixamos o usuario decidir se quer voltar ao menu, encerrar o programa ou fazer uma nova soma
#esse conceito aqui mostrado sera repertido em todos os calculos seguintes
    x=int(input("digite 1 para voltar ao menu, 2 para refazer o calculo ou 3 para sair do programa "))
    if x==1:
        menu()
    elif x==2:
        soma()
    else:
        print("programa encerrado, obrigado por usar nossa calculadora")

def subtrair():
    num1=float(input("escolha o primeiro numero: "))    
    num2=float(input("escolha o primeiro numero: "))
    resultado=str(num1-num2)
    print("o resultado é: " + resultado)
    x=int(input("digite 1 para voltar ao menu, 2 para refazer o calculo ou 3 para sair do programa "))
    if x==1:
        menu()
    elif x==2:
        subtrair()
    else:
        print("programa encerrado, obrigado por usar nossa calculadora")

def multiplicar():
    num1=float(input("escolha o primeiro numero: "))    
    num2=float(input("escolha o primeiro numero: "))
    resultado=str(num1*num2)
    print("o resultado é: " + resultado)
    x=int(input("digite 1 para voltar ao menu, 2 para refazer o calculo ou 3 para sair do programa "))
    if x==1:
        menu()
    elif x==2:
        multiplicar()
    else:
        print("programa encerrado, obrigado por usar nossa calculadora")

def dividir():
    num1=float(input("escolha o primeiro numero: "))    
    num2=float(input("escolha o primeiro numero: "))
    resultado=str(num1/num2)
    print("o resultado é: " + resultado)
    x=int(input("digite 1 para voltar ao menu, 2 para refazer o calculo ou 3 para sair do programa "))
    if x==1:
        menu()
    elif x==2:
        dividir()
    else:
        print("programa encerrado, obrigado por usar nossa calculadora")

#nesse caso estamos chamando o menu para que se inicie o programa, o software ira ler todas as linhas anteriores e quando chegar aqui ira iniciar o menu
menu()