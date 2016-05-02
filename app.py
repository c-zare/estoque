#-*- coding:utf-8 -*-
from estado  import Aberto
from estado  import Cancelado
from estado  import Fechado

from estoque import Historico
from estoque import Item
from estoque import Pedido

def lista():
    print ('\nPedido    : %s\nAndamento : %s\nData      : %s\nTotal     : %.2f\nQuantidade: %s\n'
        %(pedido1.numero,pedido1.estado,pedido1.data,pedido1.total,pedido1.quantidade))
    for item in pedido1.itens:
        print (item.codigo,item.descricao,item.quantidade,item.custo)
    print ('\nPedido    : %s\nAndamento : %s\nData      : %s\nTotal     : %.2f\nQuantidade: %s\n'
            %(pedido2.numero,pedido2.estado,pedido2.data,pedido2.total,pedido2.quantidade))
    for item in pedido2.itens:
        print (item.codigo,item.descricao,item.quantidade,item.custo)

historico = Historico()

item1 = Item(codigo=100,descricao='Placa de rede 1000 kbps',quantidade=20,custo=42.13)
item2 = Item(codigo=101,descricao='Monitor 15 polegadas   ',quantidade=20,custo=800.5)
item3 = Item(codigo=102,descricao='Mouse Optico           ',quantidade=20,custo=15.03)
item4 = Item(codigo=122,descricao='Cpu Intel 7            ',quantidade=5,custo=398.32)
item5 = Item(codigo=132,descricao='Hardisk 1 TB           ',quantidade=11,custo=221.67)

pedido1 = Pedido(numero=1)
pedido2 = Pedido(numero=2)

pedido1.adiciona_item(item1)
pedido1.adiciona_item(item2)
pedido1.adiciona_item(item5)

pedido2.adiciona_item(item3)
pedido2.adiciona_item(item4)

historico.adiciona(pedido1.salva())
historico.adiciona(pedido2.salva())

lista()

pedido1.remove_item(item=item2)
pedido2.remove_item(item=item3)

pedido1.avanca(Fechado())
pedido2.avanca(Cancelado())

historico.adiciona(pedido1.salva())
historico.adiciona(pedido2.salva())

lista()

pedido1 = historico.obten(0)
pedido2 = historico.obten(1)

lista()

pedido1 = historico.obten(2)
pedido2 = historico.obten(3)

lista()
