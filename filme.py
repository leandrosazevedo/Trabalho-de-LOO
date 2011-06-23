#coding:utf-8
class Filme(object):
    def __init__(self,identificacao_do_filme,titulo_do_filme,duracao_do_filme,ano_de_lancamento_do_filme,genero_do_filme,diretor_do_filme,artistas_do_filme):
        self.identificacao_do_filme = identificacao_do_filme
        self.titulo_do_filme = titulo_do_filme
        self.duracao_do_filme = duracao_do_filme
        self.ano_de_lancamento_do_filme = ano_de_lancamento_do_filme
        self.genero_do_filme = genero_do_filme
        self.diretor_do_filme = diretor_do_filme
        self.artistas_do_filme = artistas_do_filme
        self.copias = []

    def adicionar_copia_filme(self,copia):
        self.copias.append(copia)
