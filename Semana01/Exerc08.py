#Implemente uma função que remova o elemento anterior a
#um elemento de valor v. Esta função deve ter o protótipo:

#def lista_retira_ant(lst, v):

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

def lista_retira_ant(lst, v):
    if lst is None or lst.prox is None:
        return lst

    if lst.info == v:
        return lst

    atual = lst
    while atual.prox is not None:
        if atual.prox.info == v:
            atual.prox = atual.prox.prox
            return lst
        atual = atual.prox
    
    return lst

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)

print("Lista original:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox

v = 30
lst = lista_retira_ant(lst, v)

print("Lista após remover o elemento anterior a", v)
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox
