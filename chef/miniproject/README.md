miniproject Cookbook
====================
Chef cookbook/recipe to bootstrap an AWS webserver inside the default VPC/Security Group and display a message web page. 


Requirements
------------
AWS Account and credentials with sufficient permissions to create resources.
 
AWS key-pair name and identity file (.pem file)

Port 80 access open on your default Security Group

ChefDK with knife-ec2 plugin installed on your workstation

Chef Server to upload miniproject cookbook

Usage
-----
1. Copy miniproject cookbook to chef-repo/cookbooks/ on your workstation
2. Upload cookbook to chef server:
   knife cookbook upload miniproject
3. Inside the chef-repo on your workstation execute the following command:
   knife ec2 server create -I ami-e3106686 -f t2.micro --ssh-key awskeypairname -A 'ACCESSKEY' -K "AWSSECRETKEY" --identity-file your-ec2.pem --ssh-user ec2-user --run-list "recipe[miniproject]"

*NOTE - Remember to terminate instances after you're done testing. 
