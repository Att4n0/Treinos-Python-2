class Livros:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):

        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = int(ano_publicacao)
        self._disponivel = True
        Livros.livros.append(self)

    def __str__(self):
        disponibilidade = "Disponível" if self._disponivel else "Emprestado"

        return (f'Título: {self._titulo} | '
                f'Autor: {self._autor} | '
                f'Ano: {self._ano_publicacao} | '
                f'Situação: {disponibilidade}')

    @property
    def titulo(self):
        return self._titulo

    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    @property
    def autor(self):
        return self._autor
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        disponiveis = []

        for livro in Livros.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                disponiveis.append(livro)

        return disponiveis
    

livro1 = Livros('1984', 'George Orwell', '1949')
livro2 = Livros('Percy Jackson e o ladrão de raios', 'Rick Riordan', '2005')

livro2.emprestar()

for livro in Livros.livros:
    print (livro)

try:
    ano = int(input('Digite um número inteiro, e o programa listará os livros publicados naquele ano \nque estão disponíveis: '))
    livros_disponiveis = Livros.verificar_disponibilidade(ano)
    if livros_disponiveis:
        for livro in livros_disponiveis:
            print(f'Nome: {livro.titulo} | Autor: {livro.autor}')
    else:
        print("Não há livros disponíveis desse ano.")

except ValueError:
    print("Você deve digitar um ano válido.")
