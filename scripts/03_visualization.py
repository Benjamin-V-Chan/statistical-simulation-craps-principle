import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_results():
    df = pd.read_csv("outputs/simulation_results.csv")
    win_counts = df["Outcome"].value_counts()

    plt.figure(figsize=(6, 4))
    sns.barplot(x=win_counts.index, y=win_counts.values)
    plt.title("Craps Simulation Outcomes")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.savefig("outputs/visualization.png")
    plt.show()

if __name__ == "__main__":
    plot_results()
