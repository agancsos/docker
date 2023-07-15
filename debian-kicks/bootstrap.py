#!/user/bin/env python3
###############################################################################
# Name        : bootstrap.py                                                  #
# Author      : Abel Gancsos                                                  #
# Version     : v. 1.0.0.0                                                    #
# Description : Helps prepare the container for KICKS.                        #
###############################################################################
import os, sys, logging, requests, shutil, time;
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level="INFO");
log = logging.getLogger(__name__);

def run_hercules_cmd(cmd):
	rsp = requests.post("http://localhost:8038/cgi-bin/tasks/syslog", data={
		"send": "Send",
		"command": cmd
	}).content.decode();

if __name__ == "__main__":
	params               = {};
	for i in range(0, len(sys.argv) - 1): params[sys.argv[i]] = sys.argv[i + 1];
	if not os.path.exists("/root/GETFILE.jcl") and not os.path.exists("/root/RECVFILE.jcl"):
		log.info("\033[33mKICKS already bootstrapped...\033[m");		
	log.info("\033[36mInitializing tape drive...\033[m");
	run_hercules_cmd("devinit 10c /mvs38/kicks-tso-v1r5m0/kicks-tso-v1r5m0.xmi");
	log.info("\033[36mRunning LOAD/RECV JCL...\033[m");
	loaders = [
		"GETFILE.jcl",
		"RECVFILE.jcl",
		"/V1R5M0.jcl"
	]
	for loader in loaders:
		os.system("nc -w1 localhost 3505 < /root/{0}".format(loader));
		time.sleep(30);
	log.info("\033[36mInstalling PDS...\033[m");
	loaders = [
		#"HERC01.KICKS.V1R5M0.BIGPDS(V1R5M0)",
		"HERC01.KICKS.V1R5M0.INSTLIB(LOADMUR)",
		"HERC01.KICKS.V1R5M0.INSTLIB(LOADTAC)",
		"HERC01.KICKS.V1R5M0.INSTLIB(LOADSDB)"
	];
	for loader in loaders:
		log.info("\033[36mRunning loader: '{0}'\033[m".format(loader));
		shutil.copy("/root/SUBMITINTERNAL.jcl", "/root/SUBMITINTERNAL_temp.jcl");
		temp_data = ""
		with open("/root/SUBMITINTERNAL_temp.jcl", "r") as fh: temp_data = fh.read();
		temp_data = temp_data.replace("$PATH", loader);
		with open("/root/SUBMITINTERNAL_temp.jcl", "w") as fh: fh.write(temp_data);
		os.system("nc -w1 localhost 3505 < /root/SUBMITINTERNAL_temp.jcl");
		time.sleep(30);
		os.remove("/root/SUBMITINTERNAL_temp.jcl");
	os.remove("/root/GETFILE.jcl");
	os.remove("/root/RECVFILE.jcl");

