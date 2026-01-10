# Day 14 – Run Summaries and System Narratives

## Purpose of Run Summaries
Run summaries provide a concise interpretation of system behavior without requiring users to inspect raw logs or 
visualizations. In both clinical and engineering contexts, quick understanding is often more valuable than exhaustive 
detail. Summaries allow stakeholders to assess whether a run was nominal or noteworthy at a glance.

## Clinician-Facing Summaries
Clinician-facing summaries prioritize clarity and actionable guidance over technical detail. Rather than exposing
metrics or thresholds, summaries describe signal behavior in plain language and indicate whether further review is 
recommended. This approach minimizes cognitive load while maintaining situational awareness.

## Engineer-Facing Summaries
Engineer-facing summaries condense key metrics such as operating mode, variability, thresholds, and distortion into a
short narrative. This enables rapid assessment of system performance and supports debugging and validation without 
requiring inspection of the full audit log. Summaries act as an entry point for deeper technical analysis when needed.

## Implications for EVCVES
Run summaries improve communication and decision-making by aligning system outputs with the needs of different audiences.
They support efficient review during development, testing, and demonstration of EVCVES functionality. As the system
scales, summaries will help ensure consistent understanding across clinical, engineering, and stakeholder contexts.
