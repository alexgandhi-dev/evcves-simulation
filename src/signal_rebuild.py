import math
import random
import matplotlib.pyplot as plt

def signal_generator(noise_level, num_points=100):
    time = list(range(num_points))
    signal = []

    for t in time:
        value = math.sin(t * 0.1) + random.uniform(-noise_level, noise_level)
        signal.append(value)

    return time, signal

if __name__ == "__main__":
    time, signal_low_noise = signal_generator(noise_level=0.1)
    _, signal_high_noise = signal_generator(noise_level=0.5)

    print(f"Low Noise Average: {sum(signal_low_noise)/len(signal_low_noise)}")
    print(f"High Noise Average: {sum(signal_high_noise)/len(signal_high_noise)}")


    plt.figure(figsize=(10,4))
    plt.plot(time, signal_low_noise, label="Low Noise")
    plt.plot(time, signal_high_noise, label="High Noise", alpha=0.7)

    plt.title("Simulated Physiological Signal")
    plt.xlabel("Time")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.show()