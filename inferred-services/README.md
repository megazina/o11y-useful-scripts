## Inferred Services - assets to help observing

1. Dashboard Group 
2. Detector: Latency Spike (>3s for 90% of 5min)
3. Detector: Error Rate (>50%, sudden change)

# 1. Dashboard Group

*From UI:*
Click on '+' on the top right and select Import->Dashboard Group
Find your dashboard group 'Inferred Services' and use as a starting point to create charts.

Screenshot:
![Dashboard Group 'Inferred Services'](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/screeshots/Inferred-services-DashboardGroup.png)

# 3. Detectors
![Sample Detectors for Latency and Error rate of Inferred Services](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/screeshots/detectors-1.png)

Use curl command to post the detector (replace Token and Realm as required).
These can be used as a starting point to customise signals, thresholds, messaging etc.

Screeshots:
![Error Rate Detector](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/screeshots/detectors-errors.png)
![Latency Spike Detector](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/screeshots/detectors-latency.png)
