import numpy as np

def moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode='valid')

# Sample data
data = np.array([100, 120, 130, 150, 170, 200])

window = 3

result = moving_average(data, window)

print("Original Data:", data)
print("Moving Average:", result)
# Exponential Smoothing

def exponential_smoothing(data, alpha):
    forecast = [data[0]]  # first value
    
    for t in range(1, len(data)):
        value = alpha * data[t] + (1 - alpha) * forecast[-1]
        forecast.append(value)
    
    return forecast

# call function
alpha = 0.5
exp_result = exponential_smoothing(data, alpha)

print("Exponential Smoothing:", exp_result)
print("Next Forecast (Exp):", exp_result[-1])