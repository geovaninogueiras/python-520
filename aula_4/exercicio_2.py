import datetime
import unittest

import exercicio_1 as scooby

class CatracaTeste(unittest.TestCase):
    
    def test_ticket_vencido(self):
        
        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        
        saldo = scooby.PRECO_DA_PASSAGEM + 1.00

        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria = 'sptrans')

        with self.assertRaises(scooby.ErroTicketExpirado):
            catraca.liberar(ticket)

    def test_saldo_insuficiente(self):
        
        validade = datetime.datetime.now() + datetime.timedelta(days=365)

        saldo = scooby.PRECO_DA_PASSAGEM - 1.00

        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria = 'sptrans')

        with self.assertRaises(scooby.ErroSaldoInsuficiente):
            catraca.liberar(ticket)

    def test_concessionaria(self):
        
        validade = datetime.datetime.now() + datetime.timedelta(days=365)

        saldo = scooby.PRECO_DA_PASSAGEM + 1.00

        concessionaria = 'emtu'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria = 'sptrans')

        with self.assertRaises(scooby.ErroTicketConcessionaria):
            catraca.liberar(ticket)

    def test_fluxo_feliz(self):
        
        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        
        saldo = scooby.PRECO_DA_PASSAGEM + 1.00
        
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria = 'sptrans')

        catraca.liberar(ticket)

        self.assertTrue(ticket.saldo == ( saldo - scooby.PRECO_DA_PASSAGEM ))

        self.assertTrue(catraca.esta_liberada())
        
if __name__ == '__main__':
    unittest.main()

