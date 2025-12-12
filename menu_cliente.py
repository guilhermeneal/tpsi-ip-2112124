import time
from operator import truediv
from queue import PriorityQueue

from carros import carros

historico=[]

#visualizar os carros disponiveis
def mostrar_carros():
    print("--------𝑪𝒂𝒓𝒓𝒐𝒔 𝑫𝒊𝒔𝒑𝒐𝒏𝒊𝒗𝒆𝒊𝒔-------")
    if not carros:
        print("𝐍𝐚̃𝐨 𝐓𝐞𝐦𝐨𝐬 𝐂𝐚𝐫𝐫𝐨𝐬 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐯𝐞𝐢𝐬")
    else:
        for c in carros:
            print(f"{c['id']} - {c['modelo']}")
    print()

#alugar os carros

def alugar_carros():
    mostrar_carros()
    if not carros:
        return
    try:
        print("𝐄𝐬𝐜𝐨𝐥𝐡𝐚 𝐚 𝐂𝐥𝐚𝐬𝐞 𝐝𝐨 𝐂𝐚𝐫𝐫𝐨")
    except:
        print("𝐈𝐃 𝐈𝐧𝐯𝐚𝐥𝐢𝐝𝐨")
        return
    for c in carros:
        if ["id"]==escolha:
            print(f"Alugou o carro: {c['modelo']}")
            inicio = time.time()
            print("Introduza a data que quer devolver o carro: ")
            fim=time.time()
            duracao=round(fim-inicio, 2)
            historico.append({
                "modelo": c["modelo"],
            })
            carros.remove(c)
            print(f"Carro devolvido! Tempo de utilização foi: {duracao}")
            return
    print("ID naão encontrado! \n")
def ver_historico():
    print("\n-----𝐇𝐢𝐬𝐭𝐨́𝐫𝐢𝐜𝐨 𝐝𝐞 𝐀𝐥𝐮𝐠𝐮𝐞𝐫𝐞𝐬-----")
    if not historico:
        print("Ainda não alugou nenhum carro!")
        return
    for i, h in enumerate(historico,1):
        print(f"{i}, {h['modelo']}-{h['tempo']}")
    print(f"\nTotal de carros alugados: {len(historico)}\n")

def menu():
    while true:
        