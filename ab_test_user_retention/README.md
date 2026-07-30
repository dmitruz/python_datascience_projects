# ab_test_user_retention

A/B Test Experiment Summary &
Recommendation
Project:

1. Executive Summary & Decision
Final Decision: REJECT THE ROLLOUT & HALT THE TEST
While top-line experiment data displays a tempting +7.87% lift in D7 ARPU, a deep technical
audit reveals that the experiment is fundamentally compromised. The test results cannot be
used for business deployment due to two critical operational flaws: a severe Sample Ratio
Mismatch (SRM) ($p \approx 8.23 \times 10^{-12}$) and an underlying Android
tracking/logging telemetry bug. Moving forward with a rollout based on flawed assignment
parameters poses a massive operational risk.
2. Core Experiment Readout & Methodology
Handling Incomplete Cohorts
The core evaluation metrics rely heavily on 7-day maturation windows (D7 Retention, D7
ARPU). Because the experiment ran until February 25th, users acquiring the app near the tail
end did not have a fully observed 7-day lifecycle. To prevent downward mathematical bias
caused by incomplete data, all cohorts arriving after 2026-02-18 were isolated and excluded
from D7 metrics.
● Total Raw User Dataset: 25,000 users
● Mature D7 Cohorts (Analyzed): 18,081 users
Funnel Conversion Summary
The feature successfully accelerated top-of-funnel activity, prompting statistically significant
improvements in onboarding checkpoints. However, this optimization failed to translate into core
monetization, resulting in lower total payer acquisition.
Metric
Checkpoint

Control Group Test Group Lift (%) P-Value Statistical
Significance

Tutorial
Completion
Rate

71.86% 73.37% +2.11% 0.0080 Significant (p <
0.05)

Level 3
Completion

46.99% 48.84% +3.93% 0.0035 Significant (p <
0.05)

Metric
Checkpoint

Control Group Test Group Lift (%) P-Value Statistical
Significance

Rate
Day 1
Retention

48.80% 49.17% +0.76% 0.5553 Not Significant

Day 7
Retention

24.73% 25.13% +1.61% 0.5375 Not Significant
D7 Payer Rate 2.30% 2.24% -2.34% 0.8087 Not Significant

3. Revenue Stream Breakdown
Isolating the revenue components reveals that total monetization growth is an artifact of forced
ad engagement rather than systemic core buying behavior. The bundle failed to safely scale
premium financial conversions.
● Ad Revenue ARPU (+10.63% Lift | p = 0.0000): High statistical significance. The
onboarding workflow aggressively integrated or exposed ad systems, multiplying
impression volume per user early on.
● In-App Purchase (IAP) ARPU (+7.03% Lift | p = 0.5456): Statistically directionless. The
feature failed to unlock robust premium transactional behavior.
● Total Revenue ARPU (+7.87% Lift | p = 0.3777): Statistically neutral. Because the core
user sample is structurally unbalanced, this variance remains inside regular probability
limits and cannot be safely scaled up.

4. Market Segmentation Deep-Dive
Reviewing user behavior across core system segments highlights a severe divergence between
platform types and hardware configurations.
Segment Identifier Control D7 ARPU Test D7 ARPU Net Segment Lift (%)
Platform: Android $0.2500 $0.2340 -6.41%
Platform: iOS $0.2814 $0.3497 +24.25%
Device Tier: High $0.2944 $0.3084 +4.74%
Device Tier: Low $0.2727 $0.2415 -11.45%
Device Tier: Mid $0.2501 $0.2966 +18.58%

5. Data Quality, Anomalies & Sanity Checks
● Fatal Sample Ratio Mismatch (SRM): The assignment architecture systematically
misallocated cohorts (Control: 8,581 users vs. Test: 9,500 users). A Chi-Square variance
test confirms a systemic breakdown in user traffic assignment ($p = 8.23 \times
10^{-12}$). This mathematically proves that allocation was not random, invalidating
top-line results.

● Android Telemetry Bug: In-depth historical slice analysis reveals that on February 10th
and 11th, 100% of Android Test variant users possess null/missing values for
tutorial_complete, while the corresponding Control group registered data normally. The
feature deployment likely induced application crashes or completely froze analytics
logging frameworks across Android configurations during those dates.
● Severe Platform Polarization: The massive degradation on Android (-6.41% ARPU)
contrasted against a surging iOS footprint (+24.25% ARPU) confirms that the feature's
visual layout, monetization interface, or system optimization is deeply flawed on specific
mobile operating environments.

6. Prescribed Next Steps
1. Code Audit via Engineering: Deliver tracking diagnostics to QA and Development teams
to isolate and correct the event-logging failure observed on Android across the Feb 10–11
window.
2. Re-balance the Randomization Layer: Audit and patch the internal client/server
gateway assigning buckets to stop assignment skewing and eradicate SRM flaws.
3. Relaunch Stratified Test Framework: Once systemic platform bugs are repaired, launch
a clean \"Phase 2\" experiment. Treat iOS and Android as independent, completely
isolated experimental swimlanes.
