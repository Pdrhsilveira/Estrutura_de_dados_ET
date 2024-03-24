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

def separa(lst, n):
    atual = lst
    anterior = None
    
    while atual is not None and atual.info != n:
        anterior = atual
        atual = atual.prox
    
    if atual is None:
        return None
    
    if anterior is not None:
        anterior.prox = None
    
    subdivisao = atual.prox
    
    atual.prox = None
    
    return subdivisao

lst = None
lst = insere_lista(lst, 10)
lst = insere_lista(lst, 20)
lst = insere_lista(lst, 30)
lst = insere_lista(lst, 40)
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)

print("Lista original:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox

n = 40
subdivisao = separa(lst, n)

print("Subdivisão:")
atual = subdivisao
while atual is not None:
    print(atual.info)
    atual = atual.prox
