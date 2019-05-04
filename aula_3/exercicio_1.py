
class Lampada:

    def __init__(self, estado='apagado'):
        self.estado = estado

    def esta_apagada(self):
        if self.estado == 'apagado':
            return True
        return False

    def pressionar_interruptor(self):
        if self.estado == 'apagado':
            self.estado = 'aceso'
        else:
            self.estado = 'apagado'

lampada_1 = Lampada(estado='aceso')
lampada_2 = Lampada()

lampada_1.pressionar_interruptor()

print(lampada_2.esta_apagada())



























