#coding:utf-8
from datetime import date

class Locadora(object):
    def __init__(self,nome):
        self.nome = nome
        self.socios = []
        self.copias = []
    
    def adicionar_copia_filme(self,filme):
        self.copias.append(filme)
        
    def adicionar_socio(self,socio):
        self.socios.append(socio)
    
    def busca_filme_por_genero(self,genero):
        copias_encontradas = []
        for elemento in self.copias:
            if elemento.genero_do_filme == genero:
                copias_encontradas.append(elemento)
        if copias_encontradas != []:
            return copias_encontradas
        else:
            return None
    
    def busca_filme_por_diretor(self,diretor):
        copias_encontradas = []
        for elemento in self.copias:
            if elemento.diretor_do_filme.nome_diretor == diretor:
                copias_encontradas.append(elemento)
        if copias_encontradas != []:
            return copias_encontradas
        else:
            return None
    
    def busca_filme_por_artistas(self,artista1,artista2):
        copias_encontradas = []
        for elemento in self.copias:
            if elemento.artistas_do_filme[0].nome_artista == artista1 or elemento.artistas_do_filme[1].nome_artista == artista1 or elemento.artistas_do_filme[0].nome_artista == artista2 or elemento.artistas_do_filme[1].nome_artista == artista2:
                copias_encontradas.append(elemento)
        if copias_encontradas != []:
            return copias_encontradas
        else:
            return None

#    def realizar_locacao(self,filmes,codigo_socio):
#        for filme in filmes:

    def lista_todos_os_filmes_por_copia(self):
        copias_gerais = []
        lista_copias_e_quantidade = []
        for elemento in self.copias:
            copias_gerais.append(str(elemento.identificacao_da_fita).split(".")[0])
        copias_unicas = set(copias_gerais)
        for elemento in copias_unicas:
            total_copias_do_filme = 0
            for i in self.copias:
                if str(i.identificacao_da_fita).split(".")[0] == str(elemento):
                    total_copias_do_filme += 1
            lista_copias_e_quantidade.append((self.buscar_copia_por_identificacao(elemento),total_copias_do_filme))
        return lista_copias_e_quantidade



    def buscar_copia_por_identificacao(self,identificacao_da_fita):
        nome_filme = None
        for elemento in self.copias:
            if str(elemento.identificacao_da_fita).split(".")[0] == str(identificacao_da_fita):
                nome_filme = elemento.titulo_do_filme
                return elemento.titulo_do_filme

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




class Diretor(object):
    def __init__(self,nome_diretor,pais_de_origem,data_de_nascimento):
        self.nome_diretor = nome_diretor
        self.pais_de_origem = pais_de_origem
        self.data_de_nascimento = data_de_nascimento



class Artista(object):
    def __init__(self,nome_artista,pais_de_origem,data_de_nascimento):
        self.nome_artista = nome_artista
        self.pais_de_origem = pais_de_origem
        self.data_de_nascimento = data_de_nascimento
