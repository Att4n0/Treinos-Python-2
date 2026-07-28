class Restaurante:
    def __init__(self, nome, categoria):
        '''No momento da criação(instanciação) de um objeto da classe, o método inicializa os
        atributos e define o estado inicial da instância.
        Com isso, um restaurante não pode ser criado sem definir os atributos ligados somente a ele.
        Os atributos são passados quando o objeto é vinculado à classe, entre os parênteses.'''
    
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana' )

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))