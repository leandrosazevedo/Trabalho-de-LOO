#coding:utf-8

class Copia(object):
    def __init__(self,identificacao_da_copia,data_aquisicao_copia,estado_da_copia):
        self.identificacao_da_copia = identificacao_da_copia
        self.data_aquisicao_copia = data_aquisicao_copia
        self.estado_da_copia = estado_da_copia
        self.esta_alugado = False
