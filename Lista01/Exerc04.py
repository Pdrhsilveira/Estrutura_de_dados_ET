class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def insere_lista(lst, valor):
    novo_no = Lista(valor)
    novo_no.prox = lst
    return novo_no

def inverte(lst):
    if lst is None or lst.prox is None:
        return lst
    
    anterior = None
    atual = lst
    proximo = None

    while atual is not None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo

    lst = anterior

    return lst

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)

print("Lista Original:")
lista_imprime(lst)

lst_invertida = inverte(lst)

print("Lista invertida:")
lista_imprime(lst_invertida)
