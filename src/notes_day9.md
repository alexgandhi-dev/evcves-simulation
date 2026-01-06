# Day 9 - Introducing System Modes

## Motivation for Multiple Modes
A single filtering strategy cannot satisfy all goals of the EVCVES system because different clinical and educational
tasks prioritize different signal characteristics. Stable visualization and transient event inspection place competing
demands on responsiveness and smoothness. Introducing explicit modes allows the system to behave intentionally rather
than relying on one compromise solution.

## Visualization Mode Behavior
Visualization mode prioritizes stability, interpretability, and reduced noise to support understanding of overall cardiac
behavior. A moving average filter is used to smooth high-frequency noise and present clear waveform trends. This mode is
appropriate for early-stage use cases such as education, system validation, and steady-state observation.

## Transient Review Mode Behavior
Transient review mode prioritizes responsiveness to rapid signal changes that may represent short-lived physiological
events. An exponential moving average with higher alpha is used to reduce lag and preserve transient features, accepting
increased noise sensitivity as a tradeoff. This mode is intended for closer inspection rather than continuous default use.

## System-Level Implication
Explicitly defining operating modes makes system intent clear, reduces ambiguity in interpretation, and improves safety
by aligning behavior with goals. Mode-based design also supports future extensibility, allowing additional logic or
filters to be introduced without altering existing assumptions. This approach mirrors how real medical systems separates
configuration from execution.