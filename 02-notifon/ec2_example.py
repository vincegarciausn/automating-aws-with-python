# coding: utf-8
import boto3
session = boto3.Session(profile_name='automate')
ec2 = session.resource('ec2)
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path= key_name + '.pem'
key = ec2.create_key+pair(KeyName= key_name)
key = ec2.create_key_pair(KeyName= key_name)
key.key_material
with open (key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation.pem')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filet(Owners=['amazon']

)
ec2.images.filet(Owners=['amazon'])
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
img = ec2.Image('ami-0b2d8d1abb76a53d8')
img.name
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceRype = 't2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType = 't2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType = 't2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermission=[{'fromPort':22, 'IpProtocol': 'TCP', 'IpRanges': [{ 'CidrIp' : '99.53.225.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'fromPort':22, 'IpProtocol': 'TCP', 'IpRanges': [{ 'CidrIp' : '99.53.225.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'IpProtocol': 'TCP', 'IpRanges': [{ 'CidrIp' : '99.53.225.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort' :22, 'IpProtocol': 'TCP', 'IpRanges' : [{ 'CidrIp' : '99.53.225.38/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort' :80, 'IpProtocol': 'TCP', 'IpRanges' : [{ 'CidrIp' : '0.0.0.0/0'}]}])
inst.public_dns_name
