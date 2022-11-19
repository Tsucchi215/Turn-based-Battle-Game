import gameCharacter
import random

player_units = []
ai_units = []

units_choices = ['w', 't']
ai_names = []
index_a = 0
# generate AI name
while index_a < 3:
    # choose from random
    tmp_name = f'AI{random.randint(11,99)}'
    # if same nam, skip
    if (tmp_name not in ai_names):
        ai_names.append(tmp_name)
        index_a += 1
        
def main():
    rounds = 1
    game_over = False
    for num in range(3):
        complete = False
        while not complete:
            unit_type = input("Enter unit type [w/t]: ")
            if (unit_type  in units_choices):
                unit_name = input("Enter unit name: ")
                player1 = gameCharacter.GameCharacter(unit_type, unit_name)
                player_units.append(player1)
                complete = True
            else:
                print("Please select the correct choice!")
    
        ai_player = gameCharacter.GameCharacter(random.choice(units_choices), ai_names[num])
        ai_units.append(ai_player)

    while not game_over:
        print("Round", rounds)
        print('')
        # show the list of charaters
        for index, unit in enumerate(player_units):
            print(f'{index+1}.Name: {unit.unit_name}, Type: {unit.unit_type}, Hp: {unit.hp}, Attack: {unit.ak}, Defence: {unit.df}, Experience: {unit.xp},  Level: {unit.rk}')
        for index, unit in enumerate(ai_units):
            print(f'{index+1}.Name: {unit.unit_name}, Type: {unit.unit_type}, Hp: {unit.hp}, Attack: {unit.ak}, Defence: {unit.df}, Experience: {unit.xp},  Level: {unit.rk}')
        print('---------------------------------**--------------------------------------')
        # Player turn
        if rounds % 2 == 1: 
            for index, unit in enumerate(player_units):
                print(f'{index+1}.Name: {unit.unit_name}, Type: {unit.unit_type}, Hp: {unit.hp}, Attack: {unit.ak}, Defence: {unit.df}, Experience: {unit.xp},  Level: {unit.rk}')
            # ask user to choose char
            correct = False
            while not correct:
                try:
                    result = int(input("Please Choose your charater: "))
                    if (result <1 or result >len(player_units)):
                        print("Please select the correct character")
                    else:
                        selected_char = player_units[result-1]
                        correct = True
                except Exception:
                    print("Please select Numerical value")

            for index, unit in enumerate(ai_units):
                print(f'{index+1}.Name: {unit.unit_name}, Type: {unit.unit_type}, Hp: {unit.hp}, Attack: {unit.ak}, Defence: {unit.df}, Experience: {unit.xp},  Level: {unit.rk}')
            # ask user to choose Ai char to attack
            choice = False
            while not choice:
                try:
                    target = int(input("Please Choose enemy to attack: "))
                    if (target <1 or target >len(ai_units)):
                        print("Please select the correct character")
                    else:
                        selected_enemy = ai_units[target-1]
                        choice = True
                except Exception:
                    print("Please select Numerical value")

            # Attack the selected char
            selected_char.attack(selected_enemy)
        # AI turn
        else: 
            selected_ai = ai_units[random.randint(0,len(ai_units)-1)]
            selected_player = player_units[random.randint(0,len(player_units)-1)]
            selected_ai.attack(selected_player)

        for unit in player_units:
            if (unit.hp < 0):
                player_units.remove(unit)

        for unit in ai_units:
            if (unit.hp < 0):
                ai_units.remove(unit)

        rounds += 1
        if len(ai_units) == 0:
            print("Congratulations")
            game_over = True
        elif len(player_units) == 0:
            print("You lose")
            game_over = True

main()