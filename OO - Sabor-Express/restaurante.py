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
    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
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
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        #Método criado
        '''Quando chamado, o método vai listar automaticamente todos os objetos na lista restaurantes'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
            #Preste atenção. ali no restaurante. ativo, não queremos o true or false. Se colocar o _ativo, ele vai no atributo de instância lá na fonte,
            #e não vai mostrar os emojis. Se colocar ativo, esse é o nome 

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana' )

Restaurante.listar_restaurantes()