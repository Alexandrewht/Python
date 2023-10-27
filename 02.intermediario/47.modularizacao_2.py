'''
 Modularização - Entendendo os seus próprios módulos Python.
 O primeiro módulo executado chama-se __main__
 Você pode importar outro módulo inteiro ou parte do módulo.
 O python conhece a pasta onde o __main__ está e as pastas
 abaixo dele.
 Ele não reconhece pastas e módulos acima do __main__ por
 padrão.
 O python conhece todos os módulos e pacotes presentes
 nos caminhos de sys.path
'''
try:
    import sys
    sys.path.append('C:\Dev Python\Python na Udemy com Otavio miranda\02.intermediario\package')
    sys.path.append('C:\Dev Python\Python na Udemy com Otavio miranda')
except:
    print('Erro ao importar sys')
    

import modularizacao_teste

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')

print(modularizacao_teste.variavel_mod)
print(modularizacao_teste.soma(3, 4))

from modularizacao_teste import soma, variavel_mod

print(variavel_mod)
print(soma(2, 3))
