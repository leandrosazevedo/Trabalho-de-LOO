#coding:utf-8

class Locadora(object):
    
    def __init__(self,nome):
        self.nome = nome
        self.socios = []
        self.filmes = []
        self.emprestimos = []
        
    
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


    def lista_todos_os_filmes_e_quantidade_de_copia(self):
        lista_filmes = []
        for elemento in self.filmes:
            lista_filmes.append((elemento.titulo_do_filme,elemento.quantidade_de_copias_do_filme()))
        return lista_filmes

    
    def lista_todos_os_filmes_por_genero(self):
        generos = []
        lista_filmes = []
        lista_filmes_por_genero = []
        for elemento in self.filmes:
            generos.append(elemento.genero_do_filme)
        generos_unicos = set(generos)
        for genero in generos_unicos:
            for i in self.filmes:
                if i.genero_do_filme == genero:
                    lista_filmes.append(i.titulo_do_filme)
            lista_filmes_por_genero.append([genero,lista_filmes])
            lista_filmes = []
        return lista_filmes_por_genero


    def lista_todos_os_filmes_por_diretor(self):
        diretores = []
        lista_filmes = []
        lista_filmes_por_diretor = []
        for elemento in self.filmes:
            diretores.append(elemento.diretor_do_filme.nome_diretor)
        diretores_unicos = set(diretores)
        for diretor in diretores_unicos:
            for i in self.filmes:
                if i.diretor_do_filme.nome_diretor == diretor:
                    lista_filmes.append(i.titulo_do_filme)
            lista_filmes_por_diretor.append([diretor,lista_filmes])
            lista_filmes = []
        return lista_filmes_por_diretor

    def lista_todos_os_filmes_por_artista(self):
        artistas = []
        lista_filmes = []
        lista_filmes_por_artista = []
        for elemento in self.filmes:
            artistas.append(elemento.artistas_do_filme[0].nome_artista)
            artistas.append(elemento.artistas_do_filme[1].nome_artista)
        artistas_unicos = set(artistas)
        for artista in artistas_unicos:
            for i in self.filmes:
                if i.artistas_do_filme[0].nome_artista == artista or i.artistas_do_filme[1].nome_artista == artista:
                    lista_filmes.append(i.titulo_do_filme)
            lista_filmes_por_artista.append([artista,lista_filmes])
            lista_filmes = []
        return lista_filmes_por_artista


    def lista_de_copias_em_mal_estado(self):
        lista_filmes_com_copias_ruins = []
        for filme in self.filmes:
            lista_copias_ruins = []
            if filme.copias != []:
                for copia in filme.copias:
                    if copia.estado_da_copia == "R":
                        lista_copias_ruins.append(str(copia.identificacao_da_copia))
            lista_filmes_com_copias_ruins.append([filme.titulo_do_filme,lista_copias_ruins])
        return lista_filmes_com_copias_ruins













