class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor inserido passou o limite da sua conta.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):  
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self): # Se não colocar o @property, deverá colocar na função def get_limite
        return self.__limite

    @limite.setter
    def limite(self, limite): # Se não colocar o @def.setter, deverá colocar na função def set_lmite
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
        
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}