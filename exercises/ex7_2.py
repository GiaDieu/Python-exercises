#!/usr/bin/env python3

'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''
import random
class Weapon():
    def __init__(self, name, dam):
        self.name = name
        self.dam = dam

    def __str__(self):
        return "%s %s dam" % (self.name, self.dam)

gun = Weapon("Gun", 70)
sword = Weapon("sword", 20)
weapons = [gun, sword]

class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
        self.weapon = random.choice(weapons)

    def __str__(self):
        return "%s - %s: %d HP" % (self.name, self.weapon, self.HP)

    def attack(self, opponent):
        opponent.HP -= self.weapon.dam


def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
    result = None
    print(player1)
    print(player2)

    while True:
        player = random.choice([player1, player2])
        if player is player1:
            print("%s is attacking %s" % (player, player2))
            player.attack(player2)
            if player2.HP <= 0:
                break

        else:
            print("%s is attacking %s" % (player, player1))
            player.attack(player1)
            if player1.HP <= 0:
                break

    if player1.HP > 0:
        result = (player1.name, player1.HP)
    else:
        result = (player2.name, player2.HP)

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp

    player1 = Fighter("MayWeather", 100)

    player2 = Fighter("McGonner", 100)

    print(solve(player1, player2))


if __name__ == "__main__":
    main()