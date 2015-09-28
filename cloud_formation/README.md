miniproject.template 
====================
Cloud Formation template to create an AWS web server instance that will display a web page with message. 

Requirements
------------
AWS Account and credentials with sufficient permissions to create resources.
 
AWS CLI tools installed and configured to create the stack from the template.
 
Port 80 http access allowed on your default Security Group. 

Usage
-----
From the directory that contains the miniproject.json file:

aws cloudformation create-stack --stack-name miniproject --template-body file://miniproject.json


*NOTE - Remember to terminate instances after you're done testing. 
