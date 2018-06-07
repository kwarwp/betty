# betty.stacy.main.py
class Templo:
    def __init__(self):
        self._esta_no_templo = False
    def entra(self):
        self._esta_no_templo = True
    def sai(self):
        self.sai = False
        
    def entrou(self):
        return self._esta_no_templo
        
class EntradaDoTemplo(Templo):
    def __init__(self):
        super().__init__()
        self.corredor = CorredorDoTemplo()
    def sai(self):
        Templo.sai(self)
        self.corredor.entra()
        
class CorredorDoTemplo(Templo):
    def __init__(self):
        super().__init__()
    
class SalaDoTemplo(CorredorDoTemplo):
    def __init__(self):
        super().__init__()
    
musica = SalaDoTemplo()
oceano = SalaDoTemplo()
floresta = SalaDoTemplo()
#floresta.entra()
#oceano.entra()
entrada = EntradaDoTemplo()
corredor = CorredorDoTemplo()
corredor = entrada.corredor
entrada.entra()
print("musica:{},oceano:{},floresta:{}, entrada:{}, corredor:{}".format(musica.entrou(),oceano.entrou(),
             floresta.entrou(), entrada.entrou(), corredor.entrou()))
