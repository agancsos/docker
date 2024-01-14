from rockylinux:9.2
run yum -y install epel-release
run yum -y update
run yum -y upgrade
run yum -y install --skip-broken python3 python3-pip java-11-openjdk.x86_64 java-11-openjdk-devel.x86_64 unzip
run pip3 install cryptography requests requests_auth requests_html scrapy paramiko redis
run yum install -y openvpn
run echo -e 'set ruler\nset tabstop=4\nsyntax on\n' > /root/.vimrc
run echo -e 'PS1="<\$PWD>: "' >> /root/.bashrc
run curl -kO http://ag-resume.s3-website-us-east-1.amazonaws.com/jboss-eap-7.4.0.zip
run unzip /jboss-eap-7.4.0.zip
run mv /jboss-eap-7.4 /opt/jboss-eap
run /opt/jboss-eap/bin/add-user.sh -m -u admin -p Welcome123
entrypoint ["bash", "-c", "/opt/jboss-eap/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0"]

