# coding: utf-8
import boto3
session = boto3.Session(profile_name='automate')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucker='vincevideolyvervideos')
bucket = s3.create_bucket(Bucket='vincevideolyvervideos')
bucket = s3.create_bucket(Bucket='vincevideolyzervideos', CreateBucketConfiguration= {'"LocationContraint': session.region_name})
bucket = s3.create_bucket(Bucket='vincevideolyzervideos', CreateBucketConfiguration= {'"LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='vincevideolyzervideos', CreateBucketConfiguration= {'LocationConstraint': session.region_name})
from pathlib
from pathlib import path
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/vingarcia/Downloads/*.mp4')
dir /Users/vingarcia/Downloads/*.mp4
dir
get_ipython().run_line_magic('ls', '')
dir \Users\vingarcia\Downloads\*.mp4
get_ipython().run_line_magic('ls', '')
pathname = 'video.mp4'
path= Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognitopn')
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket':bucket.name, 'Name': path.name }})
response
job_id = reponse['JobId']
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result[JobStatus']
result['JobStatus']
result['ResposneMetadata']
result['ResponseMetadata']
result['videoMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
