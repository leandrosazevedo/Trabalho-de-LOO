#coding:utf-8
#número de inscrição do sócio, data do empréstimo, codigo da cópia, data da devolução e valor pago.
class Aluguel(object):
    def __init__(self,identificacao_do_aluguel,inscricao_do_socio,data_emprestimo,codigos_das_copias):
        self.identificacao_do_aluguel = identificacao_do_aluguel
        self.inscricao_do_socio = inscricao_do_socio
        self.data_emprestimo = data_emprestimo
        self.codigos_das_copias = codigos_das_copias
        self.data_devolucao = None
        self.valor_pago = None
