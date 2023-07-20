###############################################################################
# Name        : debian-kicks                                                  #
# Author      : Abel Gancsos                                                  #
# Version     : v. 1.0.0.0                                                    #
# Description : Improved, fully orchestrated version of herc-kicks.           #
###############################################################################
from debian:11
run apt-get update -y
run apt-get install -y curl python3 python3-pip libcurl4-openssl-dev openssh-server unzip gawk cmake p7zip-full vim netcat
run python3 -m pip install requests boto3
run mkdir /mvs38
copy bootstrap.py /
copy *.jcl /root
run cd /mvs38; curl --insecure -o tk4-_v1.00_current.zip "https://wotho.ethz.ch/tk4-/tk4-_v1.00_current.zip"
run cd /mvs38; unzip tk4-_v1.00_current.zip -d mvs38
run cd /mvs38; curl --insecure -o kicks-tso-v1r5m0.zip "https://www.jaymoseley.com/hercules/kicks/kicks-tso-v1r5m0.zip"
run cd /mvs38; unzip kicks-tso-v1r5m0.zip; exit 0
entrypoint ["bash", "-c", "cd /mvs38/mvs38; ./mvs; tail -f /dev/null"]
