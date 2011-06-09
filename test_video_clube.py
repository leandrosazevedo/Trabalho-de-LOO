#coding:utf-8
import unittest
from should_dsl import should
from datetime import date
from video_clube import Socio
from video_clube import Copia

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
        
unittest.main()
