#!/usr/bin/env python

import sys
import time
import webbrowser
import boto.ec2

# Get command line params

if len(sys.argv) == 4:
    (access_key, secret_key, region) = sys.argv[1:4]
elif len(sys.argv) == 3:
    (access_key, secret_key) = sys.argv[1:3]
    print("Region omitted from startup command. Defaulting to 'us-east-1'.")
    region = 'us-east-1'
elif len(sys.argv) < 3:
    print('ERROR: You must supply AWS ACCESS_KEY and SECRET_KEY values!!')
    sys.exit()

# Instantiate EC2 Connection object
conn = boto.ec2.connect_to_region(region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Create security group for our web server instance
miniproject = conn.create_security_group('mini-project', 'Mini-Project Security Group')
miniproject.authorize('tcp', 80, 80, '0.0.0.0/0')

# Specify our AMI (Generic Amazon/CentOS 64-bit)
ami = 'ami-e3106686'

# userdata to pass to instance on startup
userdata = '''
           #!/usr/bin/env bash
           yum -y install httpd
           echo "<html><head><title>SMP</title></head><body><h1>AUTOMATION FOR THE PEOPLE</h1></body></html>" > /var/www/html/index.html
           chown apache:apache /var/www/html/index.html
           service httpd start
           '''

# Launch our instance
reservation = conn.run_instances(image_id=ami, security_groups=[ miniproject ], user_data=userdata, instance_type='t2.micro') 
instance = reservation.instances[0]
print('Launching instance ' + str(instance.id) + '..')
time.sleep(120)

# Poll for instance state
while True:
    instance.update()
    if instance.state == 'running':
        print('Instance ' + str(instance.id) + ' has entered the running state..')
        break
    else:
        print('Instance ' + str(instance.id) + ' is still iniitalizing..')
        time.sleep(30)

url = 'http://' + instance.public_dns_name

# Poll for instance reachability
while True:
    site_status = conn.get_all_instance_status(instance.id)
    if site_status[0].system_status.details['reachability'] == 'passed':
        print("Mini-project webserver is available.")
        print("Navigating to url " + url )
        break
    else:
        print('Mini-project webserver is still initializing. Sleeping 30 seconds..')
        time.sleep(30)

# Open our webpage
webbrowser.open_new(url)
