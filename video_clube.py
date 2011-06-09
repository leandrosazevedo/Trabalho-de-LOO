#coding:utf-8
from datetime import date

class Socio(object):
    def __init__(self,inscricao,nome,endereco,telefone):
        self.inscricao = inscricao
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Copia(object):
    def __init__(self,identificacao_da_fita,titulo_do_filme,duracao_do_filme,ano_de_lancamento,genero_do_filme,diretor_do_filme,artistas_do_filme,data_aquisicao_do_filme,estado_da_fita,emprestimos):
        self.identificacao_da_fita = identificacao_da_fita
        self.titulo_do_filme = titulo_do_filme
        self.duracao_do_filme = duracao_do_filme
        self.ano_de_lancamento = ano_de_lancamento
        self.genero_do_filme = genero_do_filme
        self.diretor_do_filme = diretor_do_filme
        self.artistas_do_filme = artistas_do_filme
        self.data_aquisicao_do_filme = data_aquisicao_do_filme
        self.estado_da_fita = estado_da_fita
        self.emprestimos = emprestimos
