class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        '''No momento da criação(instanciação) de um objeto da classe, o método inicializa os
        atributos e define o estado inicial da instância.
        Com isso, um restaurante não pode ser criado sem definir os atributos ligados somente a ele.
        Os atributos são passados quando o objeto é vinculado à classe, entre os parênteses.
        O self serve para representar e guardar os dados do objeto específico que acabou de ser criado.
        Ele funciona como uma etiqueta que liga os valores que você passa (como nome ou idade)
        àquele objeto exato na memória do computador.
        
        Input:
        - Argumentos
        '''
    
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Basicamente, o __str__  em Python é um método especial que define a representação em texto legível 
        de um objeto, sendo acionado automaticamente pelas funções print() e str().
        Quando der um print que aciona o objeto, ao invés do retorno ser um código falando
        onde ele tá na memória e a classe, vai ser retornado o que tiver em retorno aqui em baixo.
        
        Input:
        - Argumento self

        Output:
        - Uma string

        '''
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        #Método criado
        '''Quando chamado, o método vai listar automaticamente todos os objetos na lista restaurantes'''
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana' )

Restaurante.listar_restaurantes()