#!/usr/bin/bash
# Developed by: Memmedov53
# MM-DDOS v1.0.0
if [[ "$(id -u)" -ne 0 ]]; 
then
  echo "
PZəhmət olmasa bu proqramı root ilə işə salın!
"
  exit 1
fi
function main() {
        printf '\033]2;Installing\a'
	clear
	echo ""
	echo "Installing... "
	chmod +x MM-DDOS.py
	sleep 1
	print("""███╗   ███╗███╗   ███╗      ██████╗ ██████╗  ██████╗ ███████╗
████╗ ████║████╗ ████║      ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║██╔████╔██║█████╗██║  ██║██║  ██║██║   ██║███████╗
██║╚██╔╝██║██║╚██╔╝██║╚════╝██║  ██║██║  ██║██║   ██║╚════██║
██║ ╚═╝ ██║██║ ╚═╝ ██║      ██████╔╝██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
        echo "   Version: 1.0.0"
        echo ""
	sleep 1
        apt install python3
	apt install python3-pip
	pip3 install --upgrade pip
	chmod +x uninstall.sh
	echo "
Bitdi...!

"
	echo "
usage: 
	python MM-DDOS.py
"
	exit 1
}
main
