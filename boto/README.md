miniproject with Boto 
====================
Python/Boto script that will create an AWS webserver inside the miniproject Security Group and launch a browser window to display the web page message.  


Requirements
------------
AWS Account and credentials with sufficient permissions to create resources. 
Python 2.7 - 3.3 installed on the machine where the script will run. 
boto==2.38.0 (available in requirements.txt for easy installation via pip). 
*recommend python pip to simplify boto installation. 

Usage
-----
./miniproject.py AWSACCESSKEY AWSSECRETKEY AWSREGION (optional)

example:

./miniproject.py OICU812 LMNOSECRET us-east-1

Omitting AWSREGION will default to us-east-1

*NOTE - Remember to terminate instance and delete miniproject security group after you're done testing. 
