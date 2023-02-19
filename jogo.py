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

if resposta == ia:
    print('Empate')

if resposta == 1:
    print('O Adversário escolheu pedra')
    if resposta == papel or resposta == spoky:
        print('Você venceu')
    elif resposta == tesoura or resposta == lagarto:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif resposta == 2:
    print('O Adversário escolheu papel')
    if resposta == tesoura or resposta == lagarto:
        print('Você venceu')
    elif resposta == pedra or resposta == spoky:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == 3:
    print('O Adversário escolheu tesoura')
    if resposta == pedra or resposta == spoky:
        print('Você venceu')
    elif resposta == papel or resposta == lagarto:
        print('Você Perdeu')
    else:
        print('Resposta inválida')

elif ia == 4:
    print('O Adversário escolheu tesoura')
    if resposta == papel or resposta == lagarto:
        print('Você Venceu')
    elif resposta == tesoura or pedra:
        print('Você Perdeu')
    else:
        print('Resposta inválida')

elif ia == 5:
    print('O adversário escolheu lagarto')
    if resposta == pedra or tesoura:
        print('Você venceu')
    elif resposta == spoky or resposta == papel:
        print('Você perdeu')
    else:
        print('Resposta inválida')
