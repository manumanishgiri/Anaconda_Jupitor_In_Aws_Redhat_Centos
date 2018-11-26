# Anaconda_Jupitor_In_Aws_Redhat_Centos
Anaconda_Jupitor_In_Aws_Redhat_Centos

# Download Anaconda 3 installer by typing this command
wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh

# Install Anaconda3 by typing
bash Anaconda3-5.3.1-Linux-x86_64.sh 

# Update bashrc
source ~/.bashrc

# Create your Jupyter/Ipython password using Ipython_Password.py
ipython

# Configure Jupyter/Ipython server
jupyter notebook --generate-config

# generate SSL certificates
mkdir certs
cd certs
sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

# Edit your Jupyter configuration file using jupyter_notebook_config.py and password by Ipython_Password.py
vi .jupyter/jupyter_notebook_config.py

# Create a folder for your notebooks and start Jupyter Notebook
mkdir Test
cd Test
jupyter notebook
