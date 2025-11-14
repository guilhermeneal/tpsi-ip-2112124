import random


def agrupa_por_chaves(lista_pares):
    resultado={}
    for k, v in lista_pares:
        if k not in resultado:
            resultado[k]= []
        resultado[k].append(v)
    return resultado

def baralho_cartas_todos():
    naipe=['espadas','copas','ouros','paus']
    numeros=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    baralho=[]

    for n in naipe:
        for v in numeros:
            carta= {'np':n, 'vlr':v}
            baralho.append(carta)
    return baralho

def baralhado(baralho):
    for i in range(len(baralho)):
        j=random.randint(0,len(baralho)-1)
        baralho[i], baralho[j] = baralho[j], baralho[i]
    return baralho

def conta_palavras(texto):
    palavras = texto.split()
    dicionario = {}
    for p in palavras:
        if p not in dicionario:
            dicionario[p] = 0
        dicionario[p] += 1
    return dicionario

def livro_mais_velho(livro):

    mais
if __name__ == '__main__':

    pares = [('a', 1), ('b', 2), ('a', 3)]
    print(agrupa_por_chaves(pares))

    print(baralho_cartas_todos())

    baralho = baralho_cartas_todos()
    s_baralho = baralhado(baralho)
    print(s_baralho)

    print("Contagem de palavras:", conta_palavras('Hello World!'))




'''
    def create_dictionary(original_dictionary):
        dictionary[v] = [key]

    else:
    dictionary[v].append[key]
    return dictinary'''