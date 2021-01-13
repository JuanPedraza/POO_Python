class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperature='caliente'):
        self._llenar_tanque(temperature)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self, temperature):
        print(f'Llenando el tanque de agua con agua {temperature}')
    
    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()