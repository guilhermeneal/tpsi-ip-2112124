#exercicio 1
def alinea1 ():
    print("Vamos calcular o teorema de pitágoras")
    x=float(input("Escreva o valor do primeiro cateto: "))
    y=float(input("Escreva o valor do segundo cateto: "))
    resultado=((x**2)+(y**2))**0.5
    print("O valor da hipotenusa é: ", resultado)
def alinea2 ():
    print("Escreva as suas duas notas para eu calcular se estas aprovado ou reprovado")
    x=float(input("Escreva a sua primeira nota:"))
    y=float(input("Escreva a sua segunda nota:"))
    resultado=(x+y)/2
    if resultado>=9.5:
        print("Aprovado.")
    else:
        print("Reprovado.")
    print("Com média de: ", resultado)
def alinea3 ():
    print("Pense em dois valores diferentes e irei dizer qual e o maior")
    x=float(input("Diz o primeiro número que estas a pensar: "))
    y=float(input("Diz o segundo número que estas a pensar: "))
    if x>y:
        print("o valor ",x, "é maior que ",y)
    else:
        print("o valor ",y, "é maior que ",x)
def alinea4 ():
    print("Pense num número inteiro entre 1 e 15")
    x=int(input("Escreva o número que esta a pensar: "))
    if 1<= x <15:
        while x<=15:
            print(f"n={x}")
            x +=1
    else:
        print("Número invalido.Por favor escolha outro número entre 1 e 15")
def alinea5 ():
    print("Pense num número inteiro entre 1 e 15")
    x = int(input("Escreva o número que esta a pensar: "))
    if 1 <= x < 15:
        soma=0
        while x <= 15:
            print(f"n={x}")
            soma += x
            x+=1
        print(f"Soma dos números apresentados é:{soma}" )
    else:
        print("Número invalido.Por favor escolha outro número entre 1 e 15")
def alinea6 ():
    soma = 0
    contador = 0
    print("Pense num número inferior a 100")
    while soma<500:
        número=int(input("Insira um número inferior a 100: "))
        if número<=100:
            soma+=número
            contador+=1
            print(f"Somatorio atual é:{soma} ")
        else:
            print("O valor do seu somatorio ultrapassou 500")
def alinea7 ():
    preco_unidade = float(input("Introduza o valor do produto por unidade: "))
    quantidade_produto = int(input("Introduza a quantidade que deseja do produto: "))
    total = preco_unidade * quantidade_produto

    desconto1 = 0.05  # mais de 500
    desconto2 = 0.08  # mais de 1000

    if quantidade_produto >= 1000:
        desconto = desconto2
    elif 500 <= quantidade_produto < 1000:
        desconto = desconto1
    else:
        desconto = 0

    valor_desconto = total * desconto
    final = total - valor_desconto

    print(f"Desconto aplicado: {desconto * 100:.0f}%")
    print(f"Valor do desconto: {valor_desconto:.2f}€")
    print(f"O montante a pagar é: {final:.2f}€")
alinea7()
if __main__=="__main__":