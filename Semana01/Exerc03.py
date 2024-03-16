#Implemente uma função que tenha como valor de retorno a
#referência do último nó de uma lista encadeada. Esta
#função deve obedecer ao protótipo:

#def ultimo(lst):

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

def ultimo(lst):
    if lst is None:
        return None
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    return atual

lst = cria_lista()
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)

ultimo_no = ultimo(lst)
print("Último nó da lista:", ultimo_no.info)  
