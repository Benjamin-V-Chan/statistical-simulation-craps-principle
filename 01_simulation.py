import random
import pandas as pd

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps_game():
    first_roll = roll_dice()
    
    if first_roll in (7, 11):
        return "Win"
    elif first_roll in (2, 3, 12):
        return "Loss"

    point = first_roll
    while True:
        roll = roll_dice()
        if roll == point:
            return "Win"
        elif roll == 7:
            return "Loss"

def simulate_games(n=10000):
    results = [play_craps_game() for _ in range(n)]
    df = pd.DataFrame({"Outcome": results})
    df.to_csv("outputs/simulation_results.csv", index=False)

if __name__ == "__main__":
    simulate_games(10000)