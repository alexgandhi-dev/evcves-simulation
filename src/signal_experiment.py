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


if __name__ == "__main__":
    # Generate two signals
    time, signal_low_noise = generate_signal(noise_level=0.1)
    _, signal_high_noise = generate_signal(noise_level=0.5)

    # Print statistics
    print("Low noise average:", sum(signal_low_noise) / len(signal_low_noise))
    print("High noise average:", sum(signal_high_noise) / len(signal_high_noise))

    # Plot signals
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal_low_noise, label="Low Noise")
    plt.plot(time, signal_high_noise, label="High Noise", alpha=0.7)

    plt.title("Simulated Physiological Signal")
    plt.xlabel("Time")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.show()
