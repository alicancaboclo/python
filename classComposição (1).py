class Clientes:                                       ###composição ##criação de classe
    def __init__(self, nome, idade):                  ### função com inicialização __init__ com crição de objetos
        self.nome = nome                              ###objeto passodo com atributo
        self.idade = idade
        self.endereco = []
    def inserir_endereco(self, cidade, estado):       ### crição de função e passando objetos
        self.endereco.append(Endereco(cidade, estado))###passando atributo para compor uma classe
    def list_endereco(self):
        for endereco in self.endereco:
            print('cidade:',endereco.cidade,'Estado:', endereco.estado)
class Endereco:
    def __init__(self,cidade,estado):                ##objetos
        self.cidade = cidade                         ##passando  objetos com atributos
        self.estado = estado
"""
Conwposição é classe em uso de classe para compor outra
o Endereco compoem o Cliente com inserção de objeto e com atributo
"""