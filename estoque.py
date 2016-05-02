#-*- coding:utf-8 -*-

from datetime import date
from estado  import Aberto
from estado  import Cancelado
from estado  import Fechado

class Historico(object):

    def __init__(self):
        self.__historico = []

    def obten(self, indice):
        return self.__historico[indice]

    def adiciona(self, pedido):
        self.__historico.append(pedido)

class Item(object):

    def __init__(self,codigo,descricao,quantidade,custo):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__custo = custo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def custo(self):
        return self.__custo

    @property
    def data(self):
        return self._data

class Pedido(object):

    def __init__(self,numero,data=date.today(),estado=Aberto()):
        self.__numero = numero
        self.__data = data
        self.__itens = []
        self.__estado = estado
        self.__historico = Historico()

    def adiciona_item(self,item):
        self.__itens.append(item)

    def remove_item(self,item):
        self.__itens.remove(item)

    def avanca(self,estado):
        self.__estado = estado

    def salva(self):
        envia = Pedido(numero=self.__numero,data=self.__data,estado=self.__estado)
        for item in self.__itens:
            envia.adiciona_item(item)
        return envia

    @property
    def numero(self):
        return self.__numero

    @property
    def estado(self):
        return self.__estado.estado

    @property
    def data(self):
        return self.__data

    @property
    def itens(self):
        return self.__itens

    @property
    def total(self):
        result = 0
        for item in self.__itens:
            result += item.custo * item.quantidade
        return result

    @property
    def quantidade(self):
        return len(self.__itens)
