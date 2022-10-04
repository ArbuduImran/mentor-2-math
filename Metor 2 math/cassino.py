import random


class Casino:
    balanse = 1000
    print("Добро пожаловать")
    print(f"ваш баланс = {balanse}$")

    def Local_casino(self):
        while True:
            choice = random.randint(1, 31)
            money = int(input("выберите сумму ставки\n"))
            if money > self.balanse:
                print('У вас не достаточно средств')
            else:
                pass
            player = int(input("Выберите число от 1 до 30\n"))
            if player == casino:
                self.balanse += money
                print(f"вы выиграли - {money * 2}$ \n"
                      f"ваш баланс = {self.balanse}$")
            elif player != Casino:
                self.balanse -= money
                print(f"вы проиграли - {money}$\n"
                      f"ваш баланс = {self.balanse}$")
            else:
                print("вы что то не правильно ввели")


casino = Casino()
casino.Local_casino()
