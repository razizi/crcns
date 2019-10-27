#Generate root password
import os
import random, string
password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

#Download ngrok
os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
#Setup sshd
os.system("apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null")
#Set root password
os.system("echo root:$password | chpasswd")
os.system("mkdir -p /var/run/sshd")
os.system('echo "PermitRootLogin yes" >> /etc/ssh/sshd_config')
os.system('echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config')
os.system('echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc')
os.system('echo "export LD_LIBRARY_PATH" >> /root/.bashrc')

#Run sshd
get_ipython().system_raw('/usr/sbin/sshd -D &')

#Ask token
print("Copy authtoken from https://dashboard.ngrok.com/auth")
#import getpass
#authtoken = getpass.getpass()
authtoken = "2DXURjrUhAZZNMhqN5m1F_6HHzejcfRecP8upwJnNBd"             
#Create tunnel
get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')
#Print root password
print("Root password: {}".format(password))
#Get public address
os.system("curl -s http://localhost:4040/api/tunnels | python3 -c \
    "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"")
