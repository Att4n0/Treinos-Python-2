class Livros:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):

        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livros.livros.append(self)

    def __str__(self):
        return 
    
