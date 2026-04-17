import numpy as np

def analyze_data(data):
    numeric_data = np.array([row[1:] for row in data])

    avg_runs = np.mean(numeric_data[:, 0])
    max_runs = np.max(numeric_data[:, 0])
    strike_rate = (numeric_data[:, 0] / numeric_data[:, 1]) * 100

    return {
        "average_runs": avg_runs,
        "max_runs": max_runs,
        "strike_rate_sample": strike_rate[:5]
    }