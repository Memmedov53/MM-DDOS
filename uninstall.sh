#!/usr/bin/env bash
# Developed by: Memmedov53
# MM-DDOS v1.0.0
if [[ "$(id -u)" -ne 0 ]]; then
  echo "
Zəhmət olmasa Bu Proqramı root kimi işə salın!
"
  exit 1
fi
main() {
      clear
      echo "Silinir..."
      sleep 2
      cd .. && rm -r MM-DDOS
      echo ""
      echo "Bitdi...!"
      echo "
Sağolun :(
"
      exit 1
}
main
