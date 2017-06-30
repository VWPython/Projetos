"""
Jogo simples de ataque e cura
"""

import random


def saving(player_life, player_sp, enemies):
    """
    Function that save the game
    """
    JUMP_LINE = '\n'
    ID = 0
    LIFE = 1

    save = open('memory_card.txt', 'w')

    save.write('Player')
    save.write(JUMP_LINE)
    save.write('Vida = {0}'.format(player_life))
    save.write(JUMP_LINE)
    save.write('SP = {0}'.format(player_sp))
    save.write(JUMP_LINE)
    save.write(JUMP_LINE)
    save.write('Enemies:')
    save.write(JUMP_LINE)

    for enemy in enemies:
        save.write(str(enemy[ID]) + ' - ' + str(enemy[LIFE]))
        save.write('\n')


def loading():
    """
    Function that load the game
    """
    END_OF_FILE = ''
    LIFE = 1
    SP = 1
    ID = 0

    load = open('memory_card.txt', 'r')

    load.readline()

    # Get the player life and player sp from the memory card file
    player_life = int(load.readline().split(' = ')[LIFE])
    player_sp = int(load.readline().split(' = ')[SP])

    load.readline()
    load.readline()

    enemies = []
    line = load.readline()

    # Get all the enemies from memory card file
    while line != END_OF_FILE:
        enemy_id = int(line.split(' - ')[ID])
        enemy_life = int(line.split(' - ')[LIFE])
        enemies.append([enemy_id, enemy_life])
        line = load.readline()

    return player_life, player_sp, enemies


def select_option():
    """
    Receive a valid input about what the user wants to do
    """

    get_option = False

    while not get_option:
        option = input("Deseja carregar um jogo(c) ou iniciar um novo jogo(n)? (c/n): ").lower()

        if option.startswith('n') or option.startswith('c'):
            return option
        else:
            print('Opção invalida, digite novamente')


def new_game():
    """
    Create a new game
    """

    player_life = 500
    player_sp = 100

    enemy_life = 50
    enemies = __create_enemies(enemy_life)

    return player_life, player_sp, enemies


def __create_enemies(enemy_life):
    # Function that will create a list of n enemies selected by the user

    number_of_enemies = int(input("digite o número de inimigos: "))

    enemies = []

    for enemy_id in range(number_of_enemies):
        enemies.append([enemy_id + 1, enemy_life])

    return enemies


def print_info_player(HP, SP):
    """
    Prints the player's life and sp on screen
    """

    print("Vida: ", HP)
    print("SP:", SP)


def what_to_do():
    """
    Function that ensures that the user enters a valid option
    """

    get_choose = False

    while not get_choose:
        choose = input("Deseja atacar(a), curar(c), salvar(s) ou desistir(d)? (a/c/s/d): ").lower()

        if not choose.isalpha():
            print("Digite apenas letras.")
        elif not choose.startswith('a') and \
             not choose.startswith('c') and \
             not choose.startswith('s') and \
             not choose.startswith('d'):
            print("digite uma opção válida (a/c/s/d)")
        else:
            return choose


def attack(enemies):
    """
    Function performs operations related to the player's choice to attack
    """

    ID = 0
    LIFE = 1

    enemy = random.choice(enemies)

    damage = random.randint(10, 15)

    print("Causou", damage, "de dano ao inimigo", enemy[ID], "!")

    enemy[LIFE] -= damage

    if enemy[LIFE] <= 0:
        print("Inimigo", enemy[ID], "morreu!")
        enemies.remove(enemy)


def cure(player_life, player_sp):
    """
    Function performs operations related to the choice of player to heal
    """

    if player_sp >= 10:
        cure = random.randint(10, 15)
        print("Você recebeu", cure, "de vida!")
        player_life += cure
        player_sp -= 10
    else:
        print("SP insuficiente!")

    return player_life, player_sp


def battle(player_life, player_sp, enemies):
    """
    Perform calculations and attacks after the player has chosen an action
    """

    player_life = __enemy_attack(player_life, enemies)

    if player_sp < 100:
        player_sp += 3

    if player_sp > 100:
        player_sp = 100

    game = __verify_if_the_game_is_over(player_life, enemies)

    return player_life, player_sp, game


def __enemy_attack(player_life, enemies):
    # Enemy's turn to attack

    ID = 0

    for enemy in enemies:
        # Enemy has 75% chance to hit
        hit = random.choice([True, True, True, False])

        if hit:
            damage = random.randint(1, 3)
            print("Inimigo", enemy[ID], "causou", damage, "de dano!")
            player_life -= damage
        else:
            print("Inimigo", enemy[ID], "errou o ataque!")

    return player_life


def __verify_if_the_game_is_over(player_life, enemies):
    # Check if the game is over, watching the player's life and the number of enemies

    GAME_IS_OVER = False
    PLAYING = True

    if player_life <= 0:
        print("Você foi derrotado!")
        return GAME_IS_OVER

    if len(enemies) == 0:
        print("Parabéns você ganhou o jogo!")
        return GAME_IS_OVER

    return PLAYING


def main():
    """
    Main functionality of game
    """

    option = select_option()

    if option.startswith('n'):
        player_life, player_sp, enemies = new_game()
    else:
        player_life, player_sp, enemies = loading()

    is_playing = True

    while is_playing:

        print_info_player(player_life, player_sp)

        choice_of_turn = what_to_do()

        if choice_of_turn.startswith('a'):
            attack(enemies)
            player_life, player_sp, is_playing = battle(player_life, player_sp, enemies)
        elif choice_of_turn.startswith('c'):
            player_life, player_sp = cure(player_life, player_sp)
            player_life, player_sp, is_playing = battle(player_life, player_sp, enemies)
        elif choice_of_turn.startswith('s'):
            saving(player_life, player_sp, enemies)
        else:
            is_playing = False


if __name__ == '__main__':
    main()
