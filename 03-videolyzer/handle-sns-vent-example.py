# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-west-1:548984908025:handleLabelDetectionTopic:b3a70099-3889-4b05-806c-5b3fa9a89823', 'Sns': {'Type': 'Notification', 'MessageId': '89ac017f-b645-5197-a970-57e5b749f68e', 'TopicArn': 'arn:aws:sns:us-west-1:548984908025:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"42a9d99ebb7f37b75170bcef957bea6e4c21a04e6878685e900663e20ec5f386","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1579155147968,"Video":{"S3ObjectName":"beachbus.mp4","S3Bucket":"vincevideolyzervideos12345"}}', 'Timestamp': '2020-01-16T06:12:28.283Z', 'SignatureVersion': '1', 'Signature': 'GxEQGq2k3qP4D3L1rNH7A1InaaBEwc+Rk93OShLU+mx3z8MFdkcpQk7/aYdLjRD7HFJGvTd7O9vhwFwvIs4N+KAL2OzkQzZsPb/lQQdJC8ReC9LnVIRXpAnMEQJSXoXZC8zdTKz57r05FbxcvXh/LOp1o+5GHMauUvq3xJFv/2PUxQxE+fkDNT5AePhg8lNjCb1z5WwMlOKOiVupB1LI/fPK+p9oMNfKqGoqmwl7E9D2PJ5e49ru3vNHkzh4DyAvg5NwmubVYWk6qWAD2frLBxDOOr/aLz65OXDrx3IWbr3DQuCBWFxpEOOmZ0rHwzk+JZMgMRfja1yCaLvfwK/eSQ==', 'SigningCertUrl': 'https://sns.us-west-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.us-west-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-1:548984908025:handleLabelDetectionTopic:b3a70099-3889-4b05-806c-5b3fa9a89823', 'MessageAttributes': {}}}]}
event
event['Records'][0]
event['Records'][0].keys
event['Records'][0].keys()
event['Records'][0]["EventSource']
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion]
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['sns']
event['Records'][0]['Sns']
type(event['Records'][0]['Sns']['Message']['JObId'])
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
