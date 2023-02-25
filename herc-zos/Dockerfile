from debian:11
expose 3270
expose 3278
expose 8038
run apt-get update
run apt-get upgrade -y
run apt-get install -y curl golang unixodbc unixodbc-dev python3 python3-pip wget libcurl4-openssl-dev openssh-server unzip gawk git cmake
run python3 -m pip install requests boto3
run mkdir /mvs38
copy tk4-_v1.00_current.zip /mvs38
run cd /mvs38; unzip tk4-_v1.00_current.zip -d mvs38
run echo '' | ./mvs38/mvs38/unattended/set_console_mode
entrypoint cd /mvs38/mvs38; ./mvs
