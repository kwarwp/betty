# betty.ruzwana.main.py


class Agenda:
    def __init__(self):
        self.agenda = {}
        self.senha = input("entre a senha")
        while self.senha != "ratimbum":
            self.senha = input("entre a senha")
        self.menu()
            
    def menu(self, info=""):
        self.acao = input(f"{info}digite 1 para consulta ou 2 para novo nome")
        if self.acao == "1":
            self.consulta_numero()
        else:
            self.novo_numero()
            
    def novo_numero(self):
        self.nome = input("entre o nome")
        self.tel = input("entre o telefone")
        self.agenda.update({self.nome: self.tel})
        self.menu()
            
    def consulta_numero(self):
        self.nome = input("entre o nome")
        self.tel = self.agenda[self.nome]
        self.menu(f"O telefone de {self.nome} é {self.tel}\n")
        
Agenda()
