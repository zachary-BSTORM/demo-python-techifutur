import random

menu = """
nombre mystère        : 1
FizzBuzz              : 2
Pierre Papier Ciseaux : 3
Quitter               : 4
"""

stop_loop = False

while not stop_loop:
    
    print(menu)
    
    choice = input("Entrez votre choix : ")
    
    match choice:
        # Nombre mystère
        case "1":
            print('mystery')
            mystery = random.randint(0,101)
            victory = False

            while not victory:
                choice = int(input("Entrez un nombre entre 0 et 100 : "))
                
                if choice < mystery:
                    print('le nombre mystere est plus grand')
                elif choice > mystery:
                    print('le nombre mystère est plus petit')
                else:
                    print(f'Bravo vous avez trouver le nombre mystere : {mystery}')
                    victory = True
        # FizzBuzz
        case "2":
            print('FizzBuzz')
            value = int(input("Combien de valeur voulez-vous afficher ? "))

            for i in range(1 , value + 1):
                
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                    
                elif i % 3 == 0:
                    print('Fizz')
                    
                elif i % 5 == 0:
                    print("Buzz")
                    
                else:
                    print(i)
        # Pierre Papier Ciseaux
        case "3":
            print('Pierre papier ciseaux')
            bot_points = 0
            user_points = 0

            bot_win = False
            user_win = False

            indications = """
            Pierre  1
            Papier  2
            Ciseaux 3
            """


            while bot_points < 3 and user_points < 3 :
                bot_choice = random.randint(1,3)
                user_choice = input(indications)
                
                print(f"Bot : {bot_choice} - user : {user_choice}")
                match bot_choice :
                    case 1:# Pierre
                        match user_choice :
                            case "1": # Pierre
                                print("égalité")
                                
                            case "2": # Papier
                                print('Victoire')
                                user_points += 1
                            case "3": # Ciseaux
                                print('Défaite')
                                bot_points += 1
                    case 2 :# Papier
                        match user_choice :
                            case "1":# Pierre
                                print('Défaite')
                                bot_points += 1
                                
                            case "2":# Papier
                                print("égalité")
                                
                            case "3":# Ciseaux
                                print('Victoire')
                                user_points += 1
                    case 3 : # Ciseaux
                        match user_choice :
                            case "1": # Pierre
                                print('Victoire')
                                user_points += 1
                                
                            case "2": # Papier
                                print('Défaite')
                                bot_points += 1
                            case "3": # ciseaux
                                print("égalité")
                
                if user_points == 3:
                    user_win = True
                elif bot_points == 3:
                    bot_win = True
                
                if bot_points == 3 or user_points == 3:
                    if bot_win :
                        print(f'La machine à gagné , vous aviez {user_points} points')
                    if user_win :
                        print(f'Vous avez gagné , La machine avait {bot_points} points')
            
        case "4":
            stop_loop = True
    
    if stop_loop == True:
        print("Merci à bientot")