# coding: utf-8
inmport boto3
import boto3
session = boto3.session(profile_name='automate')
session = boto3.Session(profile_name='automate')
as_client = session.client{'autoscaling')
as_client = session.client('autoscaling')
as_client.decribe_auto-scaling_groups()
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='notifon example group', PolicyName='scale down')
as_client.execute_policy(AutoScalingGroupName='notifon example group', PolicyName='scale up')
as_client.execute_policy(AutoScalingGroupName='notifon example group', PolicyName='scale up')
