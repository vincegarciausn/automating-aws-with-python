# coding: utf-8
{'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-west-1', 'eventTime': '2020-01-14T22:05:40.412Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAX7UQM5D4RH6GITBRJ'}, 'requestParameters': {'sourceIPAddress': '99.53.225.38'}, 'responseElements': {'x-amz-request-id': '76DF7A9C4FA75D53', 'x-amz-id-2': 'RKUty6JHnV/s56wiHysVyWm8BoH6M15vXMZbeNE4qzzShRTFcMQPVo4f8Dm/bHlobwRZc9Lv3zc='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '2cb87c61-b2b4-4256-a801-65f7f3698f41', 'bucket': {'name': 'vincevideolyzervideos12345', 'ownerIdentity': {'principalId': 'A2KH67EYVLHWKL'}, 'arn': 'arn:aws:s3:::vincevideolyzervideos12345'}, 'object': {'key': 'video.mp4', 'size': 14848985, 'eTag': 'ef3fbf897a987e0848cafa526809a0d1-2', 'sequencer': '005E1E3B2DC0CBC6AD'}}}]}
event['Records']['s3']['bucket']['name']
event['Records'][0]['s3']['bucket']['name']
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-west-1', 'eventTime': '2020-01-14T22:05:40.412Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAX7UQM5D4RH6GITBRJ'}, 'requestParameters': {'sourceIPAddress': '99.53.225.38'}, 'responseElements': {'x-amz-request-id': '76DF7A9C4FA75D53', 'x-amz-id-2': 'RKUty6JHnV/s56wiHysVyWm8BoH6M15vXMZbeNE4qzzShRTFcMQPVo4f8Dm/bHlobwRZc9Lv3zc='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '2cb87c61-b2b4-4256-a801-65f7f3698f41', 'bucket': {'name': 'vincevideolyzervideos12345', 'ownerIdentity': {'principalId': 'A2KH67EYVLHWKL'}, 'arn': 'arn:aws:s3:::vincevideolyzervideos12345'}, 'object': {'key': 'video.mp4', 'size': 14848985, 'eTag': 'ef3fbf897a987e0848cafa526809a0d1-2', 'sequencer': '005E1E3B2DC0CBC6AD'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unqoute_plus(event['Records'][0]['s3']['object']['key'])
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
