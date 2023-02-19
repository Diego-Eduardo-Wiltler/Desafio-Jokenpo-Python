import random

pedra = 1
papel = 2
tesoura = 3
spoky = 4
lagarto = 5

resposta = int(input(

    '''
[1] Pedra
[2] Papel
[3] Tesoura
[4] Spoky
[5] Lagarto
Escolha um dos três para jogar:
 '''
))

print("=====================================")

ia = random.randint(1, 5)

if ia == pedra:
    print('O Adversário escolheu pedra')
    if resposta == pedra:
        print('Empate')
    elif resposta == papel or resposta == spoky:
        print('Você venceu')
    elif resposta == tesoura or resposta == lagarto:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == papel:
    if resposta == papel:
        print('Empate')
    elif resposta == tesoura or resposta == lagarto:
        print('Você venceu')
    elif resposta == pedra or resposta == spoky:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == tesoura:
    print('O Adversário escolheu tesoura')
    if resposta == tesoura:
        print('Empate')
    elif resposta == pedra or resposta == spoky:
        print('Você venceu')
    elif resposta == papel or resposta == lagarto:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == spoky:
    print('O Adversário escolheu spoky')
    if resposta == spoky:
        print('Empate')
    elif resposta == papel or resposta == lagarto:
        print('Você venceu')
    elif resposta == tesoura or resposta == pedra:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == lagarto:
    print('O Adversário escolheu tesoura')
    if resposta == lagarto:
        print('Empate')
    elif resposta == pedra or resposta == tesoura:
        print('Você venceu')
    elif resposta == spoky or resposta == papel:
        print('Você perdeu')
    else:
        print('Resposta inválida')
