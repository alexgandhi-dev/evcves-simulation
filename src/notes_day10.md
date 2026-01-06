# Day 10 - Introducing Advisory Decision Criteria

## Motivation for Advisory Logic
Automatically changing system behavior based on signal characteristics introduces risk if the system's intent is not
clearly communicated to the user. In a medical context, silent changes in processing can alter interpretation without 
clinical awareness. Advisory logic allows the system to surface potential concerns while preserving human oversight and
accountability.

## Chosen Decision Metric
Signal Variability was selected as an advisory trigger because it is simple, interpretable, and directly reflects rapid
changes in the input signal. Increased point-to-point variability may indicate noise, transient events, or changes in 
underlying physiology. As a scalar metric, it provides a transparent basis for reasoning without obscuring system behavior.

## Advisory vs Control Distinction
Advisory logic informs the user that current signal conditions may warrant a different mode of analysis but does not
enforce a change automatically. This preserves clinician agency and prevents agency and prevents unexpected shifts in 
visualization or interpretation. The system communicates evidence rather than taking control.

## Ethical and System Implications
By separating measurement, interpretation, and action, the system maintains clarity about responsibility and intent.
Conservative advisory behavior reduces the risk of false alarms while building trust in system outputs. This design
aligns with early-stage medical systems, where explainability and safety take precedence over autonomy.