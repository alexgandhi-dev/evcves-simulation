# Day 8 - Stress Testing Filtering Choice 

## Observed Failure Mode
When a short-lived transient event is introduced, the moving average filter reduces the peak amplitude and introduces
temporal delay. This causes the transient to appear broader and less sharp than in the raw signal, potentially obscuring
rapid physiological changes. The distortion arises because the moving average blends the transient with surrounding non-
spike values.

## Comparative Insight
The exponential moving average prserves the transient shape differently depending on parameterization. With a low alpha
value, EMA heavily weights past values and can under-represent the spike, while higher alpha values allow the filter to
respond more quickly but increase sensitivity to noise. This demonstrates that filter behavior is driven as much by
parameter choice as by filter type.

## Scoped Conclusion
For early-stage EVCVES visualization, the moving average remains appropriate due to its stability and interpretability
under typical conditions. However, in scenarios where transient or rapidly changing physiological events are clinically
relevant, an alternative filtering strategy or different parameterization would be required. This reinforces the need to
scope filtering choices to specific system goals rather than assuming a single universally optimal method