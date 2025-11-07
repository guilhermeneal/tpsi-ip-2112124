def remove_multiplos(values,value):
    resultado = []
    for e in values:
        if e % value != 0:
            resultado.append(e)
    return resultado
def junta_ordenadas(list1,list2):
    full_list = list1 + list2
    return sorted(full_list)
def duplica_elementos(list3):
    lista_duplicada = []
    for v in list3:
        lista_duplicada.append(v)
        lista_duplicada.append(v)
    return lista_duplicada
def cria_lista_multiplos(list4,value):
    lista_multiplos = []
    for j in list4:
        if j < 10:
            if j % value == 0:
                lista_multiplos.append(j)
    return lista_multiplos
def substitui(list5,velho, novo):
    resultado = []
    for k in list5:
        if k == velho:
            resultado.append(novo)
        else:
            resultado.append(k)
    return resultado
def remove_repetidos(lista6):
    sem_repetidos = []
    for i in lista6:
        if i not in sem_repetidos:
            sem_repetidos.append(i)
    return sem_repetidos

def posicoes_lista(list7,indice):
    posicoes=[]
    for i in range(len(list7)):
        if list7[i]==indice:
            posicoes.append(i)
    return posicoes


if __name__== '__main__':

    lista=[2,3,5,9,12,33,34,45]
    print(remove_multiplos(lista,3))

    x=[ 2, 5, 90]
    y=[ 3, 5, 6, 12]
    sorted_list =junta_ordenadas(x, y)
    print(sorted_list)

    list3=( ['a', ['b', 'c'], 5])
    print(duplica_elementos(list3))

    list4=[0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
    print(cria_lista_multiplos(list4,6))

    list5 = [1, 2, 3, 2, 4]
    print(substitui(list5, 2, 'a'))

    list6= [2, 4, 3, 2, 2, 2, 3]
    print(remove_repetidos(list6))

    list7= ['a', 2, 'b', 'a']
    print(posicoes_lista(list7, 'a'))



