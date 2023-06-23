import random


#Listet die möglichen optionen #
# Erstellt random choice für computer 
def get_choices():
    player_choice = input("Stein, Schere oder Papier?:")
    options = ["Stein", "Papier", "Schere"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

#Überprüft ob siegesconditions für spieler oder computer existieren
#Printet relevanten output für jedes scenario
def check_win(player, computer):
    print(f"Du hast {player} und ich habe {computer} gewaehlt")
    if player == computer:
        return f"Du und der Gegner habt beide {player}!"

    elif player == "stein":
        if computer == "schere":
            return "Stein zerbricht Schere ;) Du gewinnst!"
        else:
            return "Papier bedeckt Stein. Du verlierst"
        
    elif player == "papier":
        if computer == "schere":
            return "Schere schneidet Papier. Du verlierst"
        else:
            return "Papier bedeckt Stein :) Du gewinnst!"

    elif player == "schere":
        if computer == "stein":
            return "Stein zerbricht Schere :( Du verlierst"
        else:
            return "Schere schneidet Papier:) Du gewinnst!"
    
    else:
        return "Quatsch"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



