import math
import random

time = list(range(0, 100))

signal = []
for t in time:
    value = math.sin(t * 0.1) + random.uniform(-0.1, 0.1)
    signal.append(value)

print("Min:", min(signal))
print("Max:", max(signal))
print("Average:", sum(signal) / len(signal))
