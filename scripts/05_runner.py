import os
from scripts import simulation, analysis, visualization, strategy

def main():
    os.makedirs("outputs", exist_ok=True)
    
    print("Running Craps Simulation...")
    simulation.simulate_games(10000)

    print("Analyzing Results...")
    analysis.analyze_results()

    print("Generating Visualization...")
    visualization.plot_results()

    print("Testing Betting Strategies...")
    strategy.test_strategies()

    print("Simulation Completed.")

if __name__ == "__main__":
    main()
