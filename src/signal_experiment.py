import math
import random
import matplotlib.pyplot as plt

MODE = "visualization"      # options: "visualization", "transient"

def generate_signal(noise_level, num_points=100):
    time = list(range(num_points))
    signal = []

    for t in time:
        value = math.sin(t * 0.1) + random.uniform(-noise_level, noise_level)
        if 40 <= t <= 45:
            value += 1.5
        signal.append(value)

    return time, signal

def moving_average(signal, window_size):
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

def exponential_moving_average(signal, alpha=0.2):
    filtered = [signal[0]]
    for i in range(1, len(signal)):
        filtered.append(alpha * signal[i] + (1 - alpha) * filtered[-1])
    return filtered

def signal_variability(signal):
    diffs = []
    for i in range(1, len(signal)):
        diffs.append(abs(signal[i] - signal[i-1]))
    return sum(diffs) / len(diffs)

if __name__ == "__main__":
    # Generate two signals
    time, signal_low_noise = generate_signal(noise_level=0.1)
    _, signal_high_noise = generate_signal(noise_level=0.5)

    if MODE =="visualization":
        filtered_signal = moving_average(signal_high_noise, window_size=5)
    elif MODE == "transient":
        filtered_signal = exponential_moving_average(signal_high_noise, alpha=0.6)
    else:
        raise ValueError("Unknown MODE selected")

    if MODE == "visualization" and variability > 0.4:
        print("Advisory: High signal variability detected. Transient review mode may be appropriate.")

    variability = signal_variability(signal_high_noise)
    print(f"Signal Variability: {variability}")

    if MODE == "visualization" and variability > 0.4:
        print("Advisory: High signal variability detected. Transient review mode may be appropriate.")

    distortion = mean_absolute_difference(signal_high_noise, filtered_signal)
    print(f"Filtering distortion ({MODE} mode): {distortion}")
    # Plot signals
    plt.figure(figsize=(10, 5))

    plt.plot(time, signal_high_noise, label="Raw High Noise", alpha=0.3)
    plt.plot(time, filtered_signal, label=f"{MODE.capitalize()} Filter", linewidth=2)

    plt.title(f"EVCVES Filtering Mode: {MODE.capitalize()}")
    plt.xlabel("Time")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.show()

