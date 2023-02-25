#################################################################################################
## To start this container, run the following commands:                                         #
## 1. docker run -d -p 3435:3435 --name <instance> -t cloud-linux:latest                        #
## 2. docker exec -it <instance> /root/stuff/go/bin/cagent &                                    #
#################################################################################################
from debian:10
expose 3435
run export PATH=$PATH:/usr/sbin:/usr/bin
run apt-get update
run apt-get install -y ruby golang rsync vim unixodbc python3 curl unixodbc-dev wget
run useradd operations 
run echo "operations:test123!" | chpasswd
run echo "root:test123!" | chpasswd
run mkdir -p $HOME/stuff/go/src
run mkdir /root/stuff/go/bin
run mkdir /root/stuff/go/dist
run echo "PS1=\"<\\\$PWD>: \"" >> ~/.bashrc
run echo "export GOPATH=$HOME/stuff/go" >> ~/.bashrc

## PowerShell ("Windows")
run wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb
run dpkg -i packages-microsoft-prod.deb
run apt-get update
run apt-get install -y powershell

