import math
import random

def generate_signal(noise_level):

    time = list(range(0, 100))

    signal = []
    for t in time:
        value = math.sin(t * 0.1) + random.uniform(-noise_level, noise_level)
        signal.append(value)
    return signal
if __name__ == "__main__":
   signal_low_noise = generate_signal(0.1)
   signal_high_noise = generate_signal(0.5)

   print(f"Low noise average: {sum(signal_low_noise)/len(signal_low_noise)}")
   print(f"High noise average: {sum(signal_high_noise)/len(signal_high_noise)}")