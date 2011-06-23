#coding:utf-8
#número de inscrição do sócio, data do empréstimo, codigo da cópia, data da devolução e valor pago.
class Aluguel(object):
    def __init__(self,inscricao_do_socio,data_emprestimo,codigo_da_copia):
        self.inscricao_do_socio = inscricao_do_socio
        self.data_emprestimo = data_emprestimo
        self.codigo_da_copia = codigo_da_copia
        self.data_devolucao = None
        self.valor_pago = None
