class lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def cria_lista():
    return lista()

def insere_lista(lst, valor):
    novo = lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def lista_vazia(lst):
    return lst is None

def lista_busca(lst, valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        
        atual = atual.prox

    return False

def remover_lista(lst, valor):
    if lst is None:
        return None
    
    if lst.info == valor:
        return lst.prox
    
    anterior = lst
    atual = lst.prox
    while atual is not None:
        if atual.info == valor:
            anterior.prox = atual.prox
            return lst
        anterior = atual
        atual = atual.prox
    return lst

#atual = lst
#ant = None

#for i in range(0, n):
    #ant = vet[i]
    #if ant == busca:
        #achei

#aux = atual.prox
#atual.prox = aux.prox.prox
#aux.prox = None

lst = cria_lista()
print(lista_vazia(lst))
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)
lst = insere_lista(lst, 80)
print(lista_vazia(lst))
lista_imprime(lst)
busca = lista_busca(lst, 150)
if busca:
    print("ACHEI:{}".format(busca.info))

else:
    print("NAO ACHEI!!!!")

lst = remover_lista(lst, 70)
print("Lista após remover 70:")
lista_imprime(lst)


#lst2 = cria_lista()

#no = lista(100)
#print(no)
#no2 = lista(300)
#print(no2)

