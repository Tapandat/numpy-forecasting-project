import random

players = ["Virat", "Rohit", "Dhoni", "Gill", "Hardik"]

def generate_dataset(n=50):
    data = []

    for _ in range(n):
        player = random.choice(players)
        runs = random.randint(0, 120)
        balls = random.randint(1, 100)
        fours = random.randint(0, runs // 4 if runs > 0 else 1)
        sixes = random.randint(0, runs // 6 if runs > 0 else 1)

        data.append([player, runs, balls, fours, sixes])

    return data