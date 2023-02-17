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

ia = random.randint(1,5)

if resposta == ia:
    print('Empate')

elif resposta == 1:
        print('O Adversário escolheu pedra')
    if resposta == 2 or resposta == 4:
        print('Você venceu')
    elif resposta == 3 or resposta == 5:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == 2:
    print('O Adversário escolheu papel')
    if resposta == 3 or resposta == 5:
        print('Você venceu')
    elif resposta == 1 or resposta == 4:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == 3:
    print('O Adversário escolheu tesoura')
    if resposta == 1 or resposta == 4:
        print('Você venceu')
    elif resposta == 2 or resposta == 5:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == 4:
    print('O Adversário escolheu tesoura')
    if resposta == 2 or resposta == 5:
        print('Você venceu')
    elif resposta == 3 or resposta == 1:
        print('Você perdeu')
    else:
        print('Resposta inválida')

elif ia == 5:
    print('O Adversário escolheu tesoura')
    if resposta == 1 or resposta == 3:
        print('Você venceu')
    elif resposta == 4 or resposta == 2:
        print('Você perdeu')
    else:
        print('Resposta inválida')