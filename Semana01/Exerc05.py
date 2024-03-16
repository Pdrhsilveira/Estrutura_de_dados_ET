#Implemente uma função que insira elementos sempre ao
#final da lista. Esta função deve ter o protótipo:

#def lista_insere_final(lst, valor):

class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    if lst is None:
        return novo
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = novo
    return lst

def lista_insere_final(lst, valor):
    novo_no = Lista(valor)
    if lst is None:
        return novo_no
    
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = novo_no
    
    return lst

lst = cria_lista()
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)

lst = lista_insere_final(lst, 30)
lst = lista_insere_final(lst, 40)
lst = lista_insere_final(lst, 50)

print("Lista após a inserção final:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox


