class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo

def copia(lst):
    if lst is None:
        return None
    
    nova_lista = Lista(lst.info)
    atual_original = lst.prox
    atual_nova = nova_lista

    while atual_original is not None:
        novo_no = Lista(atual_original.info)
        atual_nova.prox = novo_no
        atual_nova = atual_nova.prox
        atual_original = atual_original.prox
    
    return nova_lista

lst = cria_lista()
lst = insere_lista(lst, "10")
lst = insere_lista(lst, "20")
lst = insere_lista(lst, "30")
lst = insere_lista(lst, "40")
lst = insere_lista(lst, "50")

copia_lst = copia(lst)

print("Lista Original:")
atual = lst
while atual is not None:
    print(atual.info)
    atual = atual.prox

print("Lista Cópia:")
atual = copia_lst
while atual is not None:
    print(atual.info)
    atual = atual.prox
