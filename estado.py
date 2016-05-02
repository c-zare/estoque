#-*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class estado(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def estado(self):
        pass

class Aberto(estado):

    def __init__(self):
        self.__estado = 'ABERTO'

    @property
    def estado(self):
        return self.__estado

class Cancelado(estado):

    def __init__(self):
        self.__estado = 'CANCELADO'

    @property
    def estado(self):
            return self.__estado

class Fechado(estado):

    def __init__(self):
        self.__estado = 'FECHADO'

    @property
    def estado(self):
        return self.__estado
