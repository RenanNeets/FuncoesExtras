#lista= [4,5,66,32,3,2,441,12,4]
#lista.sort()
lista = [
    {'nome':'Jorge','sobrenome':'Anfisa'},
    {'nome':'Jorge5','sobrenome':'Anfisa5'},
    {'nome':'Jorge4','sobrenome':'Anfisa4'},
    {'nome':'Jorge3','sobrenome':'Anfisa3'},
    {'nome':'Jorge2','sobrenome':'Anfisa2'},
]
"""
# A key lambda faz isso daqui

def ordena(item):
    #print(item)
    return item['nome']
"""
"""
def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
exibir(l1)
exibir(l2)
"""

def executa(funcao,*args):
    return funcao(*args)

def some(x,y):
    return x+y
"""
Essa função aqui é o grosso da função "Aqui2"
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
"""
duplica = executa( #Aqui2
    lambda m : lambda n : n*m,
    2
)
print(duplica(2))
print(
    executa(
        lambda x, y:x+y,
        2,3
    )
)
print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7
    )
)