import pandas as pd
import numpy as np

def simulate_strategy(strategy, bankroll=1000, bet=10, n=1000):
    df = pd.read_csv("outputs/simulation_results.csv")
    balance = bankroll
    
    for i in range(n):
        if strategy == "fixed":
            wager = bet
        elif strategy == "martingale":
            wager = bet * (2 ** i if balance < bankroll else 1)
        elif strategy == "anti-martingale":
            wager = bet * (2 ** i if balance > bankroll else 1)
        else:
            raise ValueError("Unknown strategy")

        if balance <= 0:
            break

        outcome = df.iloc[i % len(df)]["Outcome"]
        if outcome == "Win":
            balance += wager
        else:
            balance -= wager

    return balance

def test_strategies():
    strategies = ["fixed", "martingale", "anti-martingale"]
    results = {s: simulate_strategy(s) for s in strategies}

    df = pd.DataFrame.from_dict(results, orient="index", columns=["Final Bankroll"])
    df.to_csv("outputs/strategy_results.csv")

if __name__ == "__main__":
    test_strategies()
