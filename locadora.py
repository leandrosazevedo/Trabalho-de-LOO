#coding:utf-8

class Locadora(object):
    
    def __init__(self,nome):
        self.nome = nome
        self.socios = []
        self.filmes = []
        
    
    def adicionar_filme(self,filme):
        self.filmes.append(filme)
        
    
    def adicionar_socio(self,socio):
        self.socios.append(socio)    
        
    
    def adicionar_copia_a_um_filme(self,id_filme,copia):
        for elemento in self.filmes:
            if elemento.identificacao_do_filme == id_filme:
                elemento.adicionar_copia_filme(copia)
    
    
    def busca_filme_por_genero(self,genero):
        filmes_encontrados = []
        for elemento in self.filmes:
            if elemento.genero_do_filme == genero:
                filmes_encontrados.append(elemento)
        if filmes_encontrados != []:
            return filmes_encontrados
        else:
            return None
        
    
    def busca_filme_por_diretor(self,diretor):
        filmes_encontrados = []
        for elemento in self.filmes:
            if elemento.diretor_do_filme.nome_diretor == diretor:
                filmes_encontrados.append(elemento)
        if filmes_encontrados != []:
            return filmes_encontrados
        else:
            return None  
    
    
    def busca_filme_por_artistas(self,artista1,artista2):
        filmes_encontrados = []
        for elemento in self.filmes:
            if elemento.artistas_do_filme[0].nome_artista == artista1 or elemento.artistas_do_filme[1].nome_artista == artista1 or elemento.artistas_do_filme[0].nome_artista == artista2 or elemento.artistas_do_filme[1].nome_artista == artista2:
                filmes_encontrados.append(elemento)
        if filmes_encontrados != []:
            return filmes_encontrados
        else:
            return None



