# statistical-simulation-craps-principle

# Craps-Based Statistical Simulation

## 1. Project Overview

This project is a **statistical simulation of a craps-based game**, designed to analyze probabilities, expected values, and various betting strategies. Using **Monte Carlo methods**, this simulation estimates long-term player outcomes by running thousands of game iterations and applying different betting strategies.

### **Mathematical Background**

#### **1.1 Probability of Winning in Craps**
In craps, the probability of winning depends on two stages:
- The **Come-Out Roll**: The first roll of two dice, where immediate wins (7, 11) and immediate losses (2, 3, 12) occur.
- The **Point Phase**: If no immediate decision occurs, the game continues until the player re-rolls the point number or rolls a 7.

We calculate the probability of winning:

**Instant win probability:**
$$ P_{win} = P(7) + P(11) = \frac{6}{36} + \frac{2}{36} = \frac{8}{36} $$

**Instant loss probability:**
$$ P_{loss} = P(2) + P(3) + P(12) = \frac{1}{36} + \frac{2}{36} + \frac{1}{36} = \frac{4}{36} $$

The remaining outcomes establish a **point**. Let \( x \) be the probability of rolling a given point before rolling a 7.

For any point \( k \), we model the recurrence equation:
$$ P_k = \frac{k-1}{36} \cdot \frac{1}{1 - \frac{6}{36}} $$
where \( k-1 \) represents the number of successful rolls for a given point.

The total probability of winning the game is:
$$ P_{total} = P_{win} + \sum_{k=4}^{10} P_k \cdot P(point=k) $$

#### **1.2 Expected Value Analysis**
We analyze the **expected value (EV)** per bet, which is calculated as:
$$ EV = P_{win} \cdot (+1) + P_{loss} \cdot (-1) $$
where each win earns +1 unit and each loss loses -1 unit.

After numerical evaluation, the expected value is found to be slightly negative:
$$ EV \approx -0.014 $$
indicating that craps is a **negative expected value game** for the player.

#### **1.3 Betting Strategy Evaluation**
We compare strategies such as **Martingale** (doubling after losses) and **Anti-Martingale** (increasing after wins). The bankroll fluctuation follows a geometric progression, modeled as:
$$ B_n = B_0 \cdot (2^n) $$
for Martingale, and:
$$ B_n = B_0 \cdot (\frac{1}{2})^n $$
for Anti-Martingale, with win probabilities modifying the recurrence relations.

## 2. Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulation.py       # Runs Monte Carlo simulations of the game
│   ├── 02_analysis.py         # Computes statistical measures (expected value, variance)
│   ├── 03_visualization.py    # Generates graphs to visualize results
│   ├── 04_strategy.py         # Tests different betting strategies
│   ├── 05_runner.py           # Master script to execute full pipeline
├── outputs/                   # Stores results (CSV, JSON, plots)
│   ├── simulation_results.csv
│   ├── statistics.json
│   ├── strategy_results.csv
│   ├── visualization.png
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
```

## 3. Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

### 2. Run the Simulation:
```sh
python scripts/01_simulation.py
```
Generates `simulation_results.csv` with outcomes.

### 3. Perform Statistical Analysis:
```sh
python scripts/02_analysis.py
```
Computes win probability, expected value, variance, and saves results to `statistics.json`.

### 4. Generate Visualization:
```sh
python scripts/03_visualization.py
```
Creates a histogram of outcomes and saves as `visualization.png`.

### 5. Test Betting Strategies:
```sh
python scripts/04_strategy.py
```
Simulates different betting strategies and outputs `strategy_results.csv`.

### 6. Run Entire Pipeline:
```sh
python scripts/05_runner.py
```
Executes all scripts sequentially and prints a summary.

## 4. Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`