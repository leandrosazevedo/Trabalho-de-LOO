#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from locadora import Locadora
from socio import Socio
from diretor import Diretor
from artista import Artista
from filme import Filme
from copia import Copia

class Test_locadora(unittest.TestCase):

    def test_cadastro_de_locadora(self):
        locadora = Locadora("Video Club Locadora")
        locadora.nome |should| equal_to("Video Club Locadora")
        locadora.socios |should| equal_to([])
        locadora.filmes |should| equal_to([])
        locadora.emprestimos |should| equal_to([])
    
    def test_adicionar_filme(self):
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_filme("FILME A")
        locadora.adicionar_filme("FILME B")
        locadora.filmes |should| equal_to(['FILME A','FILME B'])

    def test_adicionar_socio(self):
        locadora = Locadora("Video Club Locadora")
        socio = Socio(0001,"Leandro Sousa Azevedo","Rua A. C. de Assis, 48","99517332")
        locadora.adicionar_socio(socio)
    
    def test_adicionar_copia_a_um_filme(self):
        locadora = Locadora("Video Club Locadora")
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção","Mariazinha",("Artista C","Artista D"))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        copia1 = Copia(1.01,date(2010,12,28),"B")
        copia2 = Copia(1.02,date(2010,12,28),"R")        
        locadora.adicionar_copia_a_um_filme(1,copia1)
        locadora.adicionar_copia_a_um_filme(1,copia2)
        
    def test_busca_filme_por_genero(self):
        locadora = Locadora("Video Club Locadora")
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção","Mariazinha",("Artista C","Artista D"))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_genero("Ficção") |should| equal_to([filme2,filme3])

    def test_busca_filme_por_genero_none(self):
        locadora = Locadora("Video Club Locadora")
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção","Mariazinha",("Artista C","Artista D"))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_genero("Policial") |should| equal_to(None)
    
    def test_busca_filme_por_diretor(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,("Artista C","Artista D"))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,("Artista E","Artista F"))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_diretor("Pedrinho") |should| equal_to([filme3])

    def test_busca_filme_por_diretor_none(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,("Artista C","Artista D"))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,("Artista E","Artista F"))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_diretor("Mariazinha") |should| equal_to(None)
    
    def test_busca_filme_por_artistas_encontrando_2_artistas(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_artistas("Artista A","Artista F") |should| equal_to([filme1,filme3])

    def test_busca_filme_por_artistas_encontrando_1_artista(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_artistas("Artista C","Artista H") |should| equal_to([filme2])


    def test_busca_filme_por_artistas_encontrando_nenhum_artistas(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.busca_filme_por_artistas("Artista H","Artista I") |should| equal_to(None)

    def test_lista_todos_os_filmes_e_quantidade_de_copia(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        copia1 = Copia(1.01,date(2010,12,28),"B")
        copia2 = Copia(1.02,date(2010,12,28),"R")        
        locadora.adicionar_copia_a_um_filme(1,copia1)
        locadora.adicionar_copia_a_um_filme(1,copia2)
        locadora.lista_todos_os_filmes_e_quantidade_de_copia() |should| equal_to([("Piratas do Caribe",2),("Harry Pother",0),("X-man Primeira Classe",0)])

    def test_lista_todos_os_filmes_por_genero(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.lista_todos_os_filmes_por_genero() |should| equal_to([["Ficção",["Harry Pother","X-man Primeira Classe"]],["Ação",["Piratas do Caribe"]]])
        
        
    def test_lista_todos_os_filmes_por_diretor(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor2,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        locadora.lista_todos_os_filmes_por_diretor() |should| equal_to([["Ninguem",["Piratas do Caribe"]],["Alguem",["Harry Pother","X-man Primeira Classe"]]])


    def test_lista_todos_os_filmes_por_artista(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista2,artista3))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.lista_todos_os_filmes_por_artista() |should| equal_to([["Artista C",["Harry Pother"]],["Artista B",["Piratas do Caribe","Harry Pother"]],["Artista A",["Piratas do Caribe"]]])
    
    
    def test_lista_de_copias_em_mal_estado(self):
        locadora = Locadora("Video Club Locadora")
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação",diretor1,(artista1,artista2))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção",diretor2,(artista3,artista4))
        filme3 = Filme(3,"X-man Primeira Classe","120","2011","Ficção",diretor3,(artista5,artista6))
        locadora.adicionar_filme(filme1)
        locadora.adicionar_filme(filme2)
        locadora.adicionar_filme(filme3)
        copia1 = Copia(1.01,date(2010,12,28),"B")
        copia2 = Copia(1.02,date(2010,12,28),"B")
        copia3 = Copia(1.03,date(2010,12,28),"R")
        copia4 = Copia(1.04,date(2010,12,28),"R")
        copia5 = Copia(1.05,date(2010,12,28),"R")
        copia6 = Copia(2.01,date(2010,12,28),"B")
        copia7 = Copia(2.02,date(2010,12,28),"R")
        copia8 = Copia(2.03,date(2010,12,28),"R")
        locadora.adicionar_copia_a_um_filme(1,copia1)
        locadora.adicionar_copia_a_um_filme(1,copia2)
        locadora.adicionar_copia_a_um_filme(1,copia3)
        locadora.adicionar_copia_a_um_filme(1,copia4)
        locadora.adicionar_copia_a_um_filme(1,copia5)
        locadora.adicionar_copia_a_um_filme(2,copia6)
        locadora.adicionar_copia_a_um_filme(2,copia7)
        locadora.adicionar_copia_a_um_filme(2,copia8)
        locadora.lista_de_copias_em_mal_estado() |should| equal_to([["Piratas do Caribe",["1.03","1.04","1.05"]],["Harry Pother",["2.02","2.03"]],["X-man Primeira Classe",[]]])


class Test_socio(unittest.TestCase):

    def test_cadastro_de_um_socio(self):
        socio = Socio(0001,"Leandro Sousa Azevedo","Rua A. C. de Assis, 48","99517332")
        socio.inscricao |should| equal_to(0001)
        socio.nome |should| equal_to("Leandro Sousa Azevedo")
        socio.endereco |should| equal_to("Rua A. C. de Assis, 48")
        socio.telefone |should| equal_to("99517332")

        
class Test_filme(unittest.TestCase):
    
    def test_cadastro_de_um_filme(self):
        filme = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme.identificacao_do_filme |should| equal_to(1)
        filme.titulo_do_filme |should| equal_to("Piratas do Caribe")
        filme.duracao_do_filme |should| equal_to("120")
        filme.ano_de_lancamento_do_filme |should| equal_to("2010")
        filme.genero_do_filme |should| equal_to("Ação")
        filme.diretor_do_filme |should| equal_to("Fulano")
        filme.artistas_do_filme |should| equal_to(("Artista A","Artista B"))
        filme.copias |should| equal_to([])
    
    def test_adicionar_copia_filme(self):
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção","Mariazinha",("Artista C","Artista D"))
        copia1 = Copia(1.01,date(2010,12,28),"B")
        copia2 = Copia(1.02,date(2010,12,28),"R")
        filme1.adicionar_copia_filme(copia1)
        filme1.adicionar_copia_filme(copia2)
        filme1.copias |should| equal_to([copia1,copia2])
    
    def test_quantidade_de_copias_do_filme(self):
        filme1 = Filme(1,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"))
        filme2 = Filme(2,"Harry Pother","120","2011","Ficção","Mariazinha",("Artista C","Artista D"))
        copia1 = Copia(1.01,date(2010,12,28),"B")
        copia2 = Copia(1.02,date(2010,12,28),"R")
        filme1.adicionar_copia_filme(copia1)
        filme1.adicionar_copia_filme(copia2)
        filme1.quantidade_de_copias_do_filme() |should| equal_to(2)

class Test_copia(unittest.TestCase):

    def test_cadastro_de_copia(self):
        copia = Copia(1.01,date(2010,12,28),"B")
        copia.identificacao_da_copia |should| equal_to(1.01)
        copia.data_aquisicao_copia |should| equal_to(date(2010,12,28))
        copia.estado_da_copia |should| equal_to("B")
        copia.esta_alugado |should| equal_to(False)


class Test_diretor(unittest.TestCase):

    def test_adicionar_diretor(self):
        diretor = Diretor("João da Silva","Brasil",date(1980,12,28))
        diretor.nome_diretor |should| equal_to ("João da Silva")
        diretor.pais_de_origem |should| equal_to("Brasil")
        diretor.data_de_nascimento |should| equal_to(date(1980,12,28))


class Test_artista(unittest.TestCase):
        
    def test_adicionar_artista(self):
        artista = Artista("Raíla","Brasil",date(1990,11,10))
        artista.nome_artista |should| equal_to ("Raíla")
        artista.pais_de_origem |should| equal_to("Brasil")
        artista.data_de_nascimento |should| equal_to(date(1990,11,10))


unittest.main()
