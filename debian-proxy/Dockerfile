from debian:11
run apt-get update -y
run apt-get install -y python3 python3-pip wget libcurl4-openssl-dev
run python3 -m pip install requests boto3 paramiko
run apt-get install -y squid apache2-utils
run touch /etc/squid/passwd
run touch /etc/squid/blocked_sites.txt
run echo 'acl block dstdomain "/etc/squid/blocked_sites.txt"\nhttp_access deny block' >> /etc/squid/squid.conf
run sed -i 's/http_access deny all/\#http_access deny all/g' /etc/squid/squid.conf
run echo 'http_access allow all' >> /etc/squid/squid.conf
entrypoint ["bash", "-c", "tail -f /dev/null"]
