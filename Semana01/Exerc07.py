#Implemente uma função que altere uma lista, de forma que
#os valores positivos fiquem negativos e os negativos
#fiquem positivos. Esta função deve ter o protótipo:

#def lista_altera(lst):

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

def lista_altera(lst):
    atual = lst
    while atual is not None:
        atual.info = -atual.info
        atual = atual.prox

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, -20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, -40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, -60)

print("Lista original:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox

lista_altera(lst)

print("\nLista após a alteração:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox
