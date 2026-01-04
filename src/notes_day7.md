# Day 7 - Filtering Decision

## Chosen Strategy
The moving average filter was selected as the initial default filtering strategy for EVCVES because it prioritizes signal
stability and visual interpretability. It produces a smoother representation of the underlying physiological waveform, 
making overall trends easier to observe. This aligns with the current goal of EVCVES as an early-stage visualization and
evaluation system.

## Justification
At this stage, EVCVES is focused on presenting clear, stable representations of cardiac behavior rather than detecting
rare or transient abnormalities. The moving average reduces high-frequency noise that can distract from overall waveform
and confuse interpretation. As an initial default, it provides predictable and easily explainable behavior, which is
important for trust in early system use.

## Acknowledged Risks
The moving average filter introduces temporal lag and may attenuate or mask short-lived physiological events. Rapid
changes in the signal may appear delayed or smoothed out, potentially obscuring transient dynamics. This limitation is
acceptable for early-stage use but would need to be revisited as system goals expand.

## Reviewer Counterargument
An exponential moving average could be preferable in scenarios where responsiveness to rapid signal changes is critical,
such as detecting transient or abnormal physiological events. EMA preserves more short-term variation and reacts faster
to changes, which may be valuable in later-stage or diagnostic-focused versions of EVCVES.