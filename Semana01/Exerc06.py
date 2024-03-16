#Implemente uma função que calcule a média aritmética
#dos valores armazenados. Esta função deve ter o
#protótipo:

#def lista_calcula_media(lst):

class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return None

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

def lista_calcula_media(lst):
    if lst is None:
        return None

    total = 0
    contador = 0
    atual = lst
    while atual is not None:
        total += atual.info
        contador += 1
        atual = atual.prox

    if contador == 0:
        return None

    return total / contador

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 25)
lst = insere_lista(lst, 35)
lst = insere_lista(lst, 45)
lst = insere_lista(lst, 95)

media = lista_calcula_media(lst)
if media is not None:
    print("Média dos valores na lista:", media)
else:
    print("A lista está vazia.")
