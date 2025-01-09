# Simple script to copy the values from one dimension to a custom property.

Useful when you want to update the data After Ingest and your dimension values are relatively static, but you want all Metrics have unified Dimension, so you can filter/group by etc.

_Example:_

If you have:
- some metrics with dimension _hostname_
and
- some metrics with dimension _host.name_

This script will help you to create a new custom property _host.name_ for each _key:value_ pair of your dimension (_hostname_). The additional cusom property _host.name_ will have the same value as original _hostname_.

Thus you can use the new host.name in ALL filters as it will be present in all metrics that have been ingested.

*Note*: if the new values of hostname will be added - you will need to run this again (it will just replace the custom property, no need to worry about the duplicates).

*Note2*: it can be cleaner to update the dimension name at the source (collector), but this script is to help with the specific case when that is not possible, and update the historical/existing data in Observability Cloud
