# opsworkscm-monitor

This Lambda example will describe the status of an 
OpsWorks for Puppet Enterprise (OWPE) master server,
and generate a notification.

The intended use is to invoke the Lambda from a periodic CloudWatch
cron-expression rule. Then this Lambda describes the given server
status. The status is checked if it is UNHEALTHY, and if so,
an SNS notification is generated.

Note this code is provided as-is, as an example only. It has not been
tested with any rigor. Please test and modify as you need, before
using on any critical systems.

