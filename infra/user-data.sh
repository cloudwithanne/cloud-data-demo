#!/bin/bash
yum update -y
amazon-linux-extras install python3.8 -y
pip3 install flask boto3 gunicorn
cd /home/ec2-user
git clone https://github.com/<your-username>/cloud-data-demo.git
cd cloud-data-demo/backend
gunicorn -w 2 -b 0.0.0.0:5000 app:app --daemon
