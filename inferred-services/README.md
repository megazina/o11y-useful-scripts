## Inferred Services - assets to help observing

1. [Dashboard Group](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/Dashboard_Group_Inferred%20Services.json)
2. [Detector: Latency Spike (>3s for 90% of 5min)](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/POST_Detector_latency_spike.sh)
3. [Detector: Error Rate (>50%, sudden change)](https://github.com/megazina/o11y-useful-scripts/blob/main/inferred-services/POST_Detector_error_rate.sh)

Learn more about Inferred Services: 
- [What are Inferred Services](https://docs.splunk.com/observability/en/apm/apm-spans-traces/inferred-services.html)
- [Metrics available for Inferred Services](https://docs.splunk.com/observability/en/apm/span-tags/metricsets.html#available-default-mms-metrics-and-dimensions)

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
