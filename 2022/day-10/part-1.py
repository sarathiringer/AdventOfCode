import pandas as pd
import numpy as np

with open("2022/day-10/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip().split(' ') for l in lines]

cycles = {"noop": 1, "addx" : 2}

df = pd.DataFrame(lines, columns=["add_cycles", "v"]).replace(cycles).fillna(0).astype(int)
df["cycle"] = df["add_cycles"].cumsum()
df["v_cumsum"] = 1 + df["v"].cumsum()

signal_strengths = 0
for cycle in range(20, 220+1, 40):
    X = df.loc[df["cycle"] < cycle, "v_cumsum"].tail(1).values[0]
    signal_strength = X * cycle
    signal_strengths += signal_strength
    print(f"During cycle {cycle}, X is {X} and the signal strenght is thus {signal_strength}")

print(f"The sum of the signal strengths is {signal_strengths}")
