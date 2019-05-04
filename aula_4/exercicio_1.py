##########################################################################################
# Testes usando a metodologia TDD                                                        #
# Cucumbers -> Olhar depois.                                                             #   
##########################################################################################

import datetime

'''
    Quando o usuário passar um ticket válido na catraca,
    a catraca deve liberar e o preço da passagem deve ser
    descontado do saldo do ticket. Um ticket válido
    é um ticket que está dentro do prazo de validade,
    tem saldo suficiente para pegar a passagem e pertence à 
    mesma concessionária do ônibus
'''

##########################################################################################
# Constrantes                                                                            #   
##########################################################################################

PRECO_DA_PASSAGEM = 4.00

##########################################################################################
# Erros                                                                                  #
##########################################################################################

class ErroTicketExpirado(Exception):
    pass

class ErroSaldoInsuficiente(Exception):
    pass

class ErroTicketConcessionaria(Exception):
    pass

##########################################################################################
# Classes                                                                                #
##########################################################################################

class Ticket:

    def __init__(self, validade, saldo, concessionaria):
        self.validade = validade
        self.saldo = saldo
        self.concessionaria = concessionaria

    
class Catraca:

    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'travada'

    def liberar(self, ticket):
        if ticket.validade < datetime.datetime.now():
            raise ErroTicketExpirado

        if ticket.saldo < PRECO_DA_PASSAGEM:
            raise ErroSaldoInsuficiente

        if ticket.concessionaria != self.concessionaria:
            raise ErroTicketConcessionaria

        ticket.saldo = ticket.saldo - PRECO_DA_PASSAGEM
        self.estado = 'liberada'

    def esta_liberada(self):
        
        if self.estado == 'liberada':
            return True
        
        return False

if __name__ == '__main__':

    ##########################################################################################
    # Testes                                                                                 #
    ##########################################################################################

    ##########################################################################################
    # Teste de Ticket vencido                                                                #
    ##########################################################################################
    try:    

        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = PRECO_DA_PASSAGEM + 1.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria = 'sptrans')

        catraca.liberar(ticket)

    except ErroTicketExpirado:
        print('Teste de ticket expirado ok')

    ##########################################################################################
    # Teste de Ticket com saldo insuficiente                                                 #
    ##########################################################################################
    try:    

        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = PRECO_DA_PASSAGEM - 1.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria = 'sptrans')

        catraca.liberar(ticket)

    except ErroSaldoInsuficiente:
        print('Teste saldo insuficiente')

    ##########################################################################################
    # Teste Concessionaria diferente                                                         #
    ##########################################################################################
    try:    

        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = PRECO_DA_PASSAGEM + 1.00
        concessionaria = 'emtu'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria = 'sptrans')

        catraca.liberar(ticket)

    except ErroTicketConcessionaria:
        print('Ticket inválido!')

    ##########################################################################################
    # Teste Catraca liberada                                                                 #
    ##########################################################################################

    validade = datetime.datetime.now() + datetime.timedelta(days=365)
    saldo = PRECO_DA_PASSAGEM + 1.00
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria = 'sptrans')

    catraca.liberar(ticket)

    try:
        
        assert ticket.saldo == ( saldo - PRECO_DA_PASSAGEM )
        assert catraca.esta_liberada()
        
        print('testes de fluxo feliz OK')

    except:
        
        print('Bug Encontrado!!!')