'''
Author : Philippe Correia
Script para mudar os nomes de qualquer arquivo
dentro de uma pasta para maiúsculo.
Rodar: 
1. Colocar este arquivo dentro da pasta;
2. renomear para change.py;
3. Windows clean: abrir terminal e escrever => python change.py;
	3.1. Sublime: só apertar CTRL+B, o script roda só.
'''

import os

nomes = os.listdir(".")
# print(nomes)

for nome in nomes:
	os.rename(nome, nome.upper())


# print(os.listdir("."))