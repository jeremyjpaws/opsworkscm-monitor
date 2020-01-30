# This Lambda example will describe the status of an 
# OpsWorks for Puppet Enterprise (OWPE) master server,
# and generate a notification.
#
# The intended use is to invoke the Lambda from a periodic CloudWatch
# cron-expression rule. Then this Lambda describes the given server
# status. The status is checked if it is UNHEALTHY, and if so,
# an SNS notification is generated.
#
# Note this code is provided as-is, as an example only. It has not been
# tested with any rigor. Please test and modify as you need, before
# using on any critical systems.
#

import json
import boto3
import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Using https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.publish
def publish_sns(sns_topic, message):
    topic = sns_topic
    msg = message
    sns = client = boto3.client('sns')
    response = "none"
    response = sns.publish(
         TopicArn=topic,
         Message=msg
    )
    logger.info(f'Published message {msg} to topic {topic}, with message ID {response}')

def describe_server(ow_server):
    server = ow_server
    ow = boto3.client('opsworkscm')
    response = "none"
    response = ow.describe_servers(
        ServerName = server    
    )
    status="unknown"
    for server in response["Servers"]:
        status = server["Status"]

    logger.info(f'OW server status is: {status}')

    # TODO describe and filter

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    server = os.environ['SERVER']
    topic = os.environ['TOPIC']
    msg = os.environ['ALERT_MESSAGE']

    describe_server(server)

    #publish_sns(topic, msg)

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function ending.')
    }

