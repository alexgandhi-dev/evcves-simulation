import math
import random
import matplotlib.pyplot as plt


def generate_signal(noise_level, num_points=100):
    time = list(range(num_points))
    signal = []

    for t in time:
        value = math.sin(t * 0.1) + random.uniform(-noise_level, noise_level)
        signal.append(value)

    return time, signal

def moving_average(signal, window_size=10):
    filtered = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        window = signal[start:i + 1]
        filtered.append(sum(window) / len(window))
    return filtered

def mean_absolute_difference(signal_a, signal_b):
    diffs = []
    for a, b in zip(signal_a, signal_b):
        diffs.append(abs(a-b))
    return sum(diffs) / len(diffs)
if __name__ == "__main__":
    # Generate two signals
    time, signal_low_noise = generate_signal(noise_level=0.1)
    _, signal_high_noise = generate_signal(noise_level=0.5)

    # Print statistics
    print("Low noise average:", sum(signal_low_noise) / len(signal_low_noise))
    print("High noise average:", sum(signal_high_noise) / len(signal_high_noise))

    filtered_low = moving_average(signal_low_noise, window_size=5)
    filtered_high = moving_average(signal_high_noise, window_size=5)

    distortion = mean_absolute_difference(signal_high_noise, filtered_high)
    print(f"Filtering distortion: {distortion}")
    # Plot signals
    plt.figure(figsize=(10,5))

    plt.plot(time, signal_high_noise, label="Raw High Noise", alpha=0.4)
    plt.plot(time, filtered_high, label="Filtered High Noise", linewidth=2)

    plt.title("Signal Filtering Improves Interpretability")
    plt.xlabel("Time")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.show()
