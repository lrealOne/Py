"""
Criando arquivos com python

Open = serve para abrirmos um arquivo .py, ele pode ou não existir.

Modos: r(leitura), w(escrita), x(criação),
       a(escreve ao final), b (binario),
       t(modo texto), + (leitura e escrita).

Content manager - with (abre e fecha)

Métodos uteis:
    write, read (escrever e ler)
    writelines (escrever varias linhas)
    seek (move o cursor)
    readline (ler linha)
    readlines (ler linhas)

Modulo OS:
    os.remove ou unlinkl - apaga o arquivo
    os.rename - troca o nome ou move o arquivo

Modulo JSON:
    json.dump = gera arquivo json
    json.load
"""

loc_archive = r"C:\Users\luanl\Documents\Estudos"
loc_archive += "AulaTeste.txt"

with open(loc_archive, "w") as archive:
    print("Hello world")
    print("closening")