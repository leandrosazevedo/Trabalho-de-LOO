#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from video_clube import Locadora
from video_clube import Socio
from video_clube import Diretor
from video_clube import Artista
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

    def test_busca_filme_por_genero_none(self):
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_genero("policial") |should| equal_to(None)

    def test_busca_filme_por_diretor(self):
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        diretor4 = Diretor("Mariazinha","Brasil",date(1980,12,28))
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação",diretor1,("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação",diretor2,("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção",diretor3,("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção",diretor4,("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_diretor("Pedrinho") |should| equal_to([copia3])
    
    def test_busca_filme_por_diretor_none(self):
        diretor1 = Diretor("Ninguem","Brasil",date(1980,12,28))
        diretor2 = Diretor("Alguem","Brasil",date(1980,12,28))
        diretor3 = Diretor("Pedrinho","Brasil",date(1980,12,28))
        diretor4 = Diretor("Mariazinha","Brasil",date(1980,12,28))
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação",diretor1,("Artista A","Artista B"),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação",diretor2,("Artista C","Artista D"),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção",diretor3,("Artista E","Artista F"),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção",diretor4,("Emma Watson","Artista G"),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_diretor("Leandro") |should| equal_to(None)
        
    def test_busca_filme_por_artistas_encontrando_2_artistas(self):
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        artista7 = Artista("Artista G","Brasil",date(1990,11,10))
        artista8 = Artista("Artista H","Brasil",date(1990,11,10))
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",(artista1,artista2),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",(artista4,artista3),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",(artista5,artista6),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",(artista8,artista7),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_artistas("Artista A","Artista E") |should| equal_to([copia1,copia3])
        
    def test_busca_filme_por_artistas_encontrando_1_artista(self):
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        artista7 = Artista("Artista G","Brasil",date(1990,11,10))
        artista8 = Artista("Artista H","Brasil",date(1990,11,10))
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",(artista1,artista2),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",(artista4,artista3),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",(artista5,artista6),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",(artista8,artista7),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_artistas("Artista A","Leandro") |should| equal_to([copia1])

    def test_busca_filme_por_artistas_encontrando_nenhum_artista(self):
        artista1 = Artista("Artista A","Brasil",date(1990,11,10))
        artista2 = Artista("Artista B","Brasil",date(1990,11,10))
        artista3 = Artista("Artista C","Brasil",date(1990,11,10))
        artista4 = Artista("Artista D","Brasil",date(1990,11,10))
        artista5 = Artista("Artista E","Brasil",date(1990,11,10))
        artista6 = Artista("Artista F","Brasil",date(1990,11,10))
        artista7 = Artista("Artista G","Brasil",date(1990,11,10))
        artista8 = Artista("Artista H","Brasil",date(1990,11,10))
        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",(artista1,artista2),date(2010,12,28),"B",[])
        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",(artista4,artista3),date(2010,12,28),"B",[])
        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",(artista5,artista6),date(2011,06,15),"B",[])
        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",(artista8,artista7),date(2011,10,13),"B",[])
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_copia_filme(copia1)
        locadora.adicionar_copia_filme(copia2)
        locadora.adicionar_copia_filme(copia3)
        locadora.adicionar_copia_filme(copia4)
        locadora.busca_filme_por_artistas("Marcos","Jose") |should| equal_to(None)
    
    def test_adicionar_socio(self):
        socio = Socio(0001,"Leandro Sousa Azevedo","Rua A. C. de Assis, 48","99517332")
        locadora = Locadora("Video Club Locadora")
        locadora.adicionar_socio(socio)
        
#    def test_realizar_locacao(self):
#        copia1 = Copia(1.01,"Piratas do Caribe","120","2010","Ação","Fulano",("Artista A","Artista B"),date(2010,12,28),"B",[])
#        copia2 = Copia(2.01,"Karate Kid","100","2011","Ação","Joaozinho",("Artista C","Artista D"),date(2010,12,28),"B",[])
#        copia3 = Copia(3.01,"X-man Primeira Classe","120","2011","Ficção","Pedrinho",("Artista E","Artista F"),date(2011,06,15),"B",[])
#        copia4 = Copia(4.01,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"B",[])
#        copia5 = Copia(4.02,"Harry Pother","120","2011","Ficção","Mariazinha",("Emma Watson","Artista G"),date(2011,10,13),"R",[])
#        locadora = Locadora("Video Club Locadora")
#        locadora.adicionar_copia_filme(copia1)
#        locadora.adicionar_copia_filme(copia2)
#        locadora.adicionar_copia_filme(copia3)
#        locadora.adicionar_copia_filme(copia4)
#        locadora.adicionar_copia_filme(copia5)
#        socio = Socio(0001,"Leandro Sousa Azevedo","Rua A. C. de Assis, 48","99517332")
#        locadora.adicionar_socio(socio)
#        locadora.realizar_locacao([copia1,copia4],0001)    

    def test_adicionar_diretor(self):
        diretor = Diretor("João da Silva","Brasil",date(1980,12,28))
        diretor.nome_diretor |should| equal_to ("João da Silva")
        diretor.pais_de_origem |should| equal_to("Brasil")
        diretor.data_de_nascimento |should| equal_to(date(1980,12,28))
        
    def test_adicionar_artista(self):
        artista = Artista("Raíla","Brasil",date(1990,11,10))
        artista.nome_artista |should| equal_to ("Raíla")
        artista.pais_de_origem |should| equal_to("Brasil")
        artista.data_de_nascimento |should| equal_to(date(1990,11,10))
        
    def test_cadastro_de_copia_artista_e_diretor_oo(self):
        diretor = Diretor("João da Silva","Brasil",date(1980,12,28))
        artista1 = Artista("Raíla","Brasil",date(1990,11,10))
        artista2 = Artista("Leandro","Brasil",date(1987,07,05))
        copia = Copia(1.01,"Piratas do Caribe","120","2010","Ação",diretor,(artista1,artista2),date(2010,12,28),"B",[])
        copia.identificacao_da_fita |should| equal_to(1.01)
        copia.titulo_do_filme |should| equal_to("Piratas do Caribe")
        copia.duracao_do_filme |should| equal_to("120")
        copia.ano_de_lancamento |should| equal_to("2010")
        copia.genero_do_filme |should| equal_to("Ação")
        copia.diretor_do_filme |should| equal_to(diretor)
        copia.artistas_do_filme |should| equal_to((artista1,artista2))
        copia.data_aquisicao_do_filme |should| equal_to(date(2010,12,28))
        copia.estado_da_fita |should| equal_to("B")
        copia.emprestimos |should| equal_to([])        
        
unittest.main()
