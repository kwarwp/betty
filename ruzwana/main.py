# betty.ruzwana.main.py


class Agenda:
    def __init__(self):
        self.agenda = {}
        self.senha = input("entre a senha")
        while self.senha != "ratimbum":
            self.senha = input("entre a senha")
        self.nome = input("entre o nome")
        self.tel = input("entre o telefone")
        self.agenda.update({self.nome: self.tel})
        
Agenda()
