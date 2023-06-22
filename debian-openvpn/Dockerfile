from debian:11
run apt-get update -y
run apt-get install -y golang unixodbc unixodbc-dev python3 python3-pip wget libcurl4-openssl-dev
run apt-get install -y openvpn
run python3 -m pip install requests boto3 paramiko
copy *.ovpn /root
entrypoint ["bash", "-c", "openvpn --daemon -config Default.ovpn; tail -f /dev/null"]
