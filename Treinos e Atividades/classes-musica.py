class Musica:
    nome = ''
    artista = ''
    duracao = int

# Nome e artista são int, duracao é int em segundos



musica1 = Musica()
musica1.nome = 'Age of Worry'
musica1.artista = 'John Mayer'
musica1.duracao = 159

musica2 = Musica()
musica2.nome = '15 Step'
musica2.artista = 'Radiohead'
musica2.duracao = 237

musica3 = Musica()
musica3.nome = 'The Box'
musica3.artista = 'Roddy Rich'
musica3.duracao = 216

musicas =[musica1, musica2, musica3]

for m in musicas:
    print(f"Música: {m.nome} | Artista: {m.artista} | Duração: {m.duracao}s")