import datetime
from flask import Flask, jsonify
import boto3

app = Flask(__name__)


@app.route('/time')
def get_cuurrent_time():
    return {'time': datetime.datetime.now().isoformat()}
    
@app.route('/list-s3')
def get_list_of_s3_buckets():
    s3 = boto3.resource('s3')
    response = []
    buckets = s3.buckets.all()

    for bucket in buckets:
        
        response.append({
            'name': bucket.name,
            'size': 0 #sum(1 for _ in bucket.objects.all())
        })
    return jsonify(response)

@app.route('/list-ec2')
def get_list_of_ec2_instances():
    ec2 = boto3.resource('ec2')
    response = []

    for instance in ec2.instances.all():
        if (instance.type == 't2.micro'):
            message = 'replace with t3a.micro'
        else:
            message =  'do not replace'
        response.append({
            'id': instance.id,
            'state': instance.state['Name'],
            'public_ip': instance.public_ip_address,
            'private_ip': instance.private_ip_address,
            'public_dns': instance.public_dns_name,
            'launch_time': instance.launch_time.isoformat(),
            'type': instance.instance_type,
            'message': message
        })
    return jsonify(response)

@app.route('/list-available-volumes')
def get_list_of_volumes():
    ec2 = boto3.resource('ec2')
    volumes = ec2.volumes.all().filter(Filters=[{'Name': 'status', 'Values': ['available']}])
    volume_ids = [v.id for v in volumes]
    print(volume_ids)
    return jsonify(volume_ids)
    
