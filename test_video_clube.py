#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from video_clube import Locadora
from video_clube import Socio
from video_clube import Copia

class Test_locadora(unittest.TestCase):

    def test_cadastro_de_locadora(self):
        locadora = Locadora("Video Club Locadora")
        locadora.nome |should| equal_to("Video Club Locadora")
        locadora.socios |should| equal_to([])
        locadora.copias |should| equal_to([])
    
    def test_adicionar_copia_filme(self):
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme("FILME A")
        locadora.adicionar_copia_filme("FILME B")
        locadora.copias |should| equal_to(['FILME A','FILME B'])


class Test_socio(unittest.TestCase):

    def test_cadastro_de_um_socio(self):
        socio = Socio(0001,"Leandro Sousa Azevedo","Rua A. C. de Assis, 48","99517332")
        socio.inscricao |should| equal_to(0001)
        socio.nome |should| equal_to("Leandro Sousa Azevedo")
        socio.endereco |should| equal_to("Rua A. C. de Assis, 48")
        socio.telefone |should| equal_to("99517332")
        
class Test_copia(unittest.TestCase):

    def test_cadastro_de_copia(self):
        copia = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia.identificacao_da_fita |should| equal_to(1.01)
        copia.titulo_do_filme |should| equal_to("Piratas do Caribe")
        copia.duracao_do_filme |should| equal_to("120")
        copia.ano_de_lancamento |should| equal_to("2010")
        copia.genero_do_filme |should| equal_to("Ação")
        copia.diretor_do_filme |should| equal_to("Fulano")
        copia.artistas_do_filme |should| equal_to(('Artista A','Artista B'))
        copia.data_aquisicao_do_filme |should| equal_to(date(2010,12,28))
        copia.estado_da_fita |should| equal_to("B")
        copia.emprestimos |should| equal_to([])
    
    def test_busca_filme_por_genero(self):
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_genero("Ação") |should| equal_to([copia1,copia2])

    def test_busca_filme_por_diretor(self):
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_diretor("Pedrinho") |should| equal_to([copia3])
        
    def test_busca_filme_por_artistas(self):
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_artistas("Artista A","Emma Watson") |should| equal_to([copia1,copia4])
        
unittest.main()
