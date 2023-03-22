import random


class Jokenpo:
    def __init__(self, options=["pedra", "papel", "tesoura", "lagarto", "spock"]):
        self.options = options
        self.player_score = 0
        self.computer_score = 0
        self.game_on = True
        self.rules = {
            "pedra": ["lagarto", "tesoura"],
            "papel": ["pedra", "spock"],
            "tesoura": ["papel", "lagarto"],
            "lagarto": ["papel", "spock"],
            "spock": ["tesoura", "pedra"]
        }

    def play(self):
        while self.game_on:
            print("Digite sua jogada! (pedra, papel, tesoura, lagarto ou spock) ou 'sair' para encerrar o jogo:")
            player_choice = input().lower().strip()
            while player_choice not in self.options and player_choice != "sair":
                print(
                    "Jogada inválida. Tente novamente ou digite 'sair' para encerrar o jogo.")
                player_choice = input().lower().strip()
            if player_choice == "sair":
                self.game_on = False
            else:
                computer_choice = random.choice(self.options)
                print(
                    f"Você escolheu {player_choice} e o computador {computer_choice}.")
                if player_choice == computer_choice:
                    print("Empate!")
                elif computer_choice in self.rules[player_choice]:
                    print("Você venceu!")
                    self.player_score += 1
                else:
                    print("Você perdeu!")
                    self.computer_score += 1

    def show_score(self):
        print(
            f"Placar: Jogador {self.player_score} x {self.computer_score} Computador")


jogo = Jokenpo()
jogo.play()
jogo.show_score()
