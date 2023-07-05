import random


class NoHayMonedasParaPremioException(Exception):
    pass


class NoHayMonedaException(Exception):
    pass


class Tragamonedas:
    def __init__(self):
        self.monedas = 0
        self.monedas_tirada = 0

    def insertar_moneda(self):
        if (self.monedas_tirada + 1) * 10 > self.monedas:
            raise NoHayMonedasParaPremioException()
        self.monedas += 1
        self.monedas_tirada += 1

    def tirar(self):
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
        numero1 = random.randint(1, 10)
        numero2 = random.randint(1, 10)
        numero3 = random.randint(1, 10)
        if numero1 == numero2 == numero3:
            premio = self.monedas_tirada * numero1
            self.monedas -= premio
        else:
            premio = 0
        self.monedas_tirada = 0
        return premio
