from rockylinux:9.2
run yum -y install epel-release
run yum -y update
run yum -y upgrade
run yum -y install --skip-broken  golang python3 python3-pip gcc-c++ awscli clang git cmake vim
run pip3 install cryptography requests requests_auth requests_html scrapy paramiko redis
run yum install -y openvpn
run echo -e 'set ruler\nset tabstop=4\nsyntax on\n' > /root/.vimrc
run echo -e 'PS1="<\$PWD>: "' >> /root/.bashrc
entrypoint ["bash", "-c", "tail -f /dev/null"]

