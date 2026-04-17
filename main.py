from src.generate_data import generate_dataset
from src.numpy_analysis import analyze_data

# Generate data
data = generate_dataset(50)

# Analyze
results = analyze_data(data)

print("Results:")
for key, value in results.items():
    print(f"{key}: {value}")

print("\nSample Data:")
for row in data[:5]:
    print(row)