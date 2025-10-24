#percorre os números de 1 a 5 e divide por 1 2 e 3 se sobrar resto na divisao do mesmo ele escreve a soma do i+j
def alinea1A():
     for i in range (1,6):
        for j in range (1,4):
            if ( i % j) == 1:
                print ( i + j)
#se i e 20 vai correr todos os numeros maiores que 5 ate 20 vai multiplicar por 4 vai escrever o resultado e no fim subtrair por 2
def alinea1B():
        i= 20
        while i> 5:
            print ( 4 * i )
            i = i -2
# temos 3 conjuntos de números no qual ele soma o i+j e verifica se e par
def alinea1C():
    for i in range(1):
        for j in range(3, 5):
            for k in range(5, 1, -2):
                if (i + j) % 2 == 0:
                    print(i, j, k)
#comeca no 20 e vai subtraindo de 2 ate chegar a 2 apos isso soma 1 ao resultado da subtração
def alinea2():
    soma=0
    for soma in range(20,0,-2):
        soma= soma +1
        print("Soma=", soma)
#filtra_pares que recebe um tuplo contendo algarismos, verificando a correção do seu argumento, e devolve o tuplo contendo apenas os algarismos pares
def alinea3():
