from debian:11
run apt-get update -y
run apt-get install -y golang unixodbc unixodbc-dev python3 python3-pip wget libcurl4-openssl-dev
run wget https://dot.net/v1/dotnet-install.sh
run chmod +x ./dotnet-install.sh
run ./dotnet-install.sh
run python3 -m pip install requests boto3 paramiko

# Download and install agent
copy ./vsts-agent-linux-x64-2.170.1.tar.gz /root
run mkdir /root/vsts-agent-linux-x64-2.170.1
run tar -xvf /root/vsts-agent-linux-x64-2.170.1.tar.gz -C /root/vsts-agent-linux-x64-2.170.1
run cp -R /root/vsts-agent-linux-x64-2.170.1 .
run chmod -R 777 /vsts-agent-linux-x64-2.170.1
run useradd builder

# Configure agent
run runuser --user builder -- /vsts-agent-linux-x64-2.170.1/config.sh \
	--unattended --auth negotiate --userName tfsservice --password Dilbert123 \
	--pool Docker --acceptTeeEula --sslskipcertvalidation --url "http://basilea/DefaultCollection"

# Cleanup
run rm /root/vsts-agent-linux-x64-2.170.1.tar.gz

entrypoint ["runuser", "--user", "builder", "--", "/vsts-agent-linux-x64-2.170.1/run.sh"]
