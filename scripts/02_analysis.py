import pandas as pd
import numpy as np
import json

def analyze_results():
    df = pd.read_csv("outputs/simulation_results.csv")
    win_prob = (df["Outcome"] == "Win").mean()
    loss_prob = (df["Outcome"] == "Loss").mean()
    
    stats = {
        "Total Games": len(df),
        "Win Probability": win_prob,
        "Loss Probability": loss_prob,
        "Expected Value": win_prob - loss_prob,
        "Variance": np.var([1 if x == "Win" else 0 for x in df["Outcome"]])
    }
    
    with open("outputs/statistics.json", "w") as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    analyze_results()
