# Day 6 - Comparing Filtering Strategies

## Key Difference Observed
The moving average filter produces a smoother signal but reacts more slowly to changes, while the exponential moving
average responds more quickly but leaves more residual noise.

## Tradeoff Analysis
The moving average prioritizes stability at the cost of responsiveness, whereas the exponential moving average prioritizes
responsiveness at the cost of smoothness

## EVCVES Context
In EVCVES, a slower filter may be more appropriate for observing steady-state cardiac behavior, while a faster filter may
be preferred when detecting transient or rapid physiological events.