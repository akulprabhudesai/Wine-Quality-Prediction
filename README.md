# Cloud Computing Assignment 2
1. Create EMR Cluster on AWS using key pair and 4 instances

2. Enable SSH inbould rule for port 22 in security group of EMR Master

3. Conect to Master instance using command:
chmod 400 key-file-name.pem
ssh -i "key-file-name.pem" hadoop@master-public-dns

4. Install following on Master EC2 instance:
sudo pip install --upgrade pip
pip install wheel
sudo yum install python3
pip install pyspark
pip install findspark
pip install findspark
sudo yum install -y docker
sudo yum install python34-setuptools
sudo easy_install pip
pip3.6 install wheel
pip3.6 install pyspark --no-cache-dir
pip3.6 install findspark
pip3.6 install numpy

5. Write python code to read dataset and calculate F1 score and give filename as --> file-name.py. Run the python code using command python3 filename.py

6. Create docker file using nano file-name command.
7. Sign up on docker hub

8. start docker using command:
sudo service docker start

9. Build docker on EC2 instance and create docker image using command:
sudo docker build . -f docker-file-name -t image-name

10. Build docker using command:
sudo docker build . -f docker-file-name -t image-name

11. Run docker image using command:
sudo docker run image-name

12. Create image in docker hub account using command:
sudo docker build . -f docker-id-file -t docker-hub-id/image-name-on-docker-hub

13. Login to Docker hub account using following command and enter password:
sudo docker login -u docker-hub-account-id/docker-id

14. Push files to docker using command:
sudo docker push docker-account-id/docker-image-name

15. Run the image of the Docker within the Docker Hub on EC2 Instance
sudo docker run -t docker-hub-account-id/docker-image-name
